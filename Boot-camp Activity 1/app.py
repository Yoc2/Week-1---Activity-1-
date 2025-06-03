import os
import datetime

from flask import (
    Flask, render_template, request,
    redirect, url_for, session, flash
)
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# ─── App Configuration ──────────────────────────────────────────────────────────
app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
app.secret_key = 'your_secret_key'  # ← Replace with a secure random string

# MySQL (XAMPP) Configuration
app.config['MYSQL_HOST']       = 'localhost'
app.config['MYSQL_USER']       = 'root'
app.config['MYSQL_PASSWORD']   = ''               # default on XAMPP is empty
app.config['MYSQL_DB']         = 'aact1'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'    # fetch results as dictionaries

mysql = MySQL(app)

# Upload folder for profile pictures
UPLOAD_FOLDER = os.path.join(app.static_folder, 'profile_pics')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed image extensions for profile upload
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


# ─── Utility: Check file extension ──────────────────────────────────────────────
def allowed_file(filename):
    return (
        '.' in filename
        and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ─── ROUTES ────────────────────────────────────────────────────────────────────

# “/” is now the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        raw_password = request.form.get('password')

        if not (username and raw_password):
            flash('Both username and password are required.', 'danger')
            return redirect(url_for('login'))

        # Fetch matching user from `user` table
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT * FROM user WHERE username = %s",
            (username,)
        )
        account = cursor.fetchone()
        cursor.close()

        if account and check_password_hash(account['password'], raw_password):
            session['user_id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('dashboard'))

        flash('Invalid credentials. Try again.', 'danger')
        return redirect(url_for('login'))

    # GET → show login form
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # 1) Retrieve form data
        name         = request.form.get('name')
        birthday_str = request.form.get('birthday')  # format: YYYY-MM-DD
        address      = request.form.get('address')
        username     = request.form.get('username')
        raw_password = request.form.get('password')

        # 2) Process uploaded profile picture (optional)
        file = request.files.get('profile_pic')
        profile_filename = None
        if file and file.filename != '' and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            profile_filename = f"{timestamp}_{filename}"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], profile_filename))

        # 3) Basic validation
        if not (name and birthday_str and address and username and raw_password):
            flash('Please fill in all required fields.', 'danger')
            return redirect(url_for('register'))

        # 4) Parse birthday
        try:
            birthday = datetime.datetime.strptime(birthday_str, '%Y-%m-%d').date()
        except ValueError:
            flash('Invalid date format. Use YYYY-MM-DD.', 'danger')
            return redirect(url_for('register'))

        # 5) Check if username already exists in `register`
        cursor = mysql.connection.cursor()
        cursor.execute(
            "SELECT id FROM register WHERE username = %s",
            (username,)
        )
        existing = cursor.fetchone()
        if existing:
            flash('Username already taken. Choose another.', 'warning')
            cursor.close()
            return redirect(url_for('register'))

        # 6) Hash the password
        hashed_pw = generate_password_hash(raw_password)

        # 7) Insert into `register` table
        cursor.execute(
            """
            INSERT INTO register 
              (profile, name, birthday, address, username, password)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (profile_filename, name, birthday, address, username, hashed_pw)
        )
        mysql.connection.commit()

        # 8) Insert into `user` table (for login)
        cursor.execute(
            "INSERT INTO user (username, password) VALUES (%s, %s)",
            (username, hashed_pw)
        )
        mysql.connection.commit()
        cursor.close()

        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    # GET → show registration form
    return render_template('register.html')


from datetime import date

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    cursor = mysql.connection.cursor()
    cursor.execute(
        "SELECT * FROM register WHERE username = %s",
        (session['username'],)
    )
    profile = cursor.fetchone()
    cursor.close()

    # Calculate age in years:
    birth = profile['birthday']  # a Python date object
    today = date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))

    # Attach age to the profile dict so the template can use it
    profile['age'] = age

    return render_template('dashboard.html', profile=profile)



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))


# ─── Run the App ────────────────────────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)

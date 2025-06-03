-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 03, 2025 at 05:40 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aact1`
--

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `id` int(11) NOT NULL,
  `profile` varchar(255) DEFAULT NULL,
  `name` varchar(150) NOT NULL,
  `birthday` date NOT NULL,
  `address` varchar(255) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`id`, `profile`, `name`, `birthday`, `address`, `username`, `password`) VALUES
(1, '20250603105607_119843945_2055336104596329_689069106721664863_n.jpg', '123', '2025-06-16', '123123', 'clyde@gmail.com', 'scrypt:32768:8:1$QdXvOBXFZ4a2ziDX$a515b9aa801c5b1996172f3eb9abbd8a19d7e8edb55c688bebde66bcbbfb4453c638600d3714dceeba61405675f9ad9958dcf1b881e25e04f8a8b94929c0c2c4'),
(2, NULL, '123', '2025-06-24', '123', '123123123', 'scrypt:32768:8:1$jvO8of6xZwd0py2F$9f054e3e655f1b9b03d66f17122e811379514b88ed4dc399204dfb10fd5ca68203060dd9c1be527109905ef5e3ebc3dde7c454f06fd13ef98cbc504a11db1001'),
(3, '20250603113241_bcf6b2b0-53d6-4373-8278-52a6966315c9.jpg', 'Andre Bayot', '2025-06-19', 'San Vicente, Butuan City', 'james123', 'scrypt:32768:8:1$dvXHH5yYApua5dCa$385b7269daf18dbe6899f97bd975d559097bca3e0f779bb04bfb784a41ec8070d665805b954e9396b1df0a5d131a96fd6a62093b07b1260a83fb9342df1581bf');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `password`) VALUES
(1, 'clyde@gmail.com', 'scrypt:32768:8:1$QdXvOBXFZ4a2ziDX$a515b9aa801c5b1996172f3eb9abbd8a19d7e8edb55c688bebde66bcbbfb4453c638600d3714dceeba61405675f9ad9958dcf1b881e25e04f8a8b94929c0c2c4'),
(2, '123123123', 'scrypt:32768:8:1$jvO8of6xZwd0py2F$9f054e3e655f1b9b03d66f17122e811379514b88ed4dc399204dfb10fd5ca68203060dd9c1be527109905ef5e3ebc3dde7c454f06fd13ef98cbc504a11db1001'),
(3, 'james123', 'scrypt:32768:8:1$dvXHH5yYApua5dCa$385b7269daf18dbe6899f97bd975d559097bca3e0f779bb04bfb784a41ec8070d665805b954e9396b1df0a5d131a96fd6a62093b07b1260a83fb9342df1581bf');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

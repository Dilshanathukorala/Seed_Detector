-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 29, 2020 at 02:58 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.4.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `seeddb`
--

-- --------------------------------------------------------

--
-- Table structure for table `germination`
--

CREATE TABLE `germination` (
  `id` int(11) NOT NULL,
  `timestamp` datetime NOT NULL,
  `first_count` int(10) NOT NULL,
  `second_count` int(10) NOT NULL,
  `dormant` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `germination`
--

INSERT INTO `germination` (`id`, `timestamp`, `first_count`, `second_count`, `dormant`) VALUES
(1, '2020-07-29 17:33:07', 75, 25, 50),
(2, '2020-07-29 17:34:41', 185, 0, 185),
(3, '2020-07-29 17:35:17', 192, 120, 72);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `germination`
--
ALTER TABLE `germination`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `germination`
--
ALTER TABLE `germination`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

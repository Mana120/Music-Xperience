-- phpMyAdmin SQL Dump
-- version 4.7.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 29, 2018 at 05:19 PM
-- Server version: 10.1.25-MariaDB
-- PHP Version: 7.1.7
use music1;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `spotify-clone`
--

-- --------------------------------------------------------

--
-- Table structure for table `albums`
--

CREATE TABLE `albums` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `artist` int(11) NOT NULL,
  `genre` int(11) NOT NULL,
  `artworkPath` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `albums`
--

INSERT INTO `albums` (`id`, `title`, `artist`, `genre`, `artworkPath`) VALUES
(1, 'Bacon and Eggs', 2, 4, 'assets/images/artwork/clearday.jpg'),
(2, 'Pizza Head', 5, 10, 'assets/images/artwork/energy.jpg'),
(3, 'Summer Hits', 3, 1, 'assets/images/artwork/goinghigher.jpg'),
(4, 'The movie soundtrack', 2, 9, 'assets/images/artwork/funkyelement.jpg'),
(5, 'Best of the Worst', 1, 3, 'assets/images/artwork/popdance.jpg'),
(6, 'Hello World', 3, 6, 'assets/images/artwork/ukulele.jpg'),
(7, 'Best beats', 4, 7, 'assets/images/artwork/sweet.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `artists`
--

CREATE TABLE `artists` (
  `id` int  NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `artists`
--

INSERT INTO `artists` (`id`, `name`) VALUES
(1, 'Mickey Mouse'),
(2, 'Goofy'),
(3, 'Bart Simpson'),
(4, 'Homer'),
(5, 'Bruce Lee');

-- --------------------------------------------------------

--
-- Table structure for table `genres`
--

CREATE TABLE `genres` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `genres`
--

INSERT INTO `genres` (`id`, `name`) VALUES
(1, 'Rock'),
(2, 'Pop'),
(3, 'Hip-hop'),
(4, 'Rap'),
(5, 'R & B'),
(6, 'Classical'),
(7, 'Techno'),
(8, 'Jazz'),
(9, 'Folk'),
(10, 'Country');

-- --------------------------------------------------------

--
-- Table structure for table `playlists`
--

CREATE TABLE `playlists` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `owner` int(11) NOT NULL,
  `dateCreated` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `playlistssongs`
--

CREATE TABLE `playlistssongs` (
  `id` int(11) NOT NULL,
  `songId` int(11) NOT NULL,
  `playlistId` int(11) NOT NULL,
  `playlistOrder` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `songs`
--

CREATE TABLE `songs` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `artist` int(11) NOT NULL,
  `album` int(11) NOT NULL,
  `genre` int(11) NOT NULL,
  `duration` varchar(8) NOT NULL,
  `path` varchar(500) NOT NULL,
  `albumOrder` int(11) NOT NULL,
  `plays` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `songs`
--

INSERT INTO `songs` (`id`, `title`, `artist`, `album`, `genre`, `duration`, `path`, `albumOrder`, `plays`) VALUES
(1, 'Acoustic Breeze', 1, 5, 8, '2:37', 'assets/music/bensound-acousticbreeze.mp3', 1, 8),
(2, 'A new beginning', 1, 5, 1, '2:35', 'assets/music/bensound-anewbeginning.mp3', 2, 6),
(3, 'Better Days', 1, 5, 2, '2:33', 'assets/music/bensound-betterdays.mp3', 3, 3),
(4, 'Buddy', 1, 5, 3, '2:02', 'assets/music/bensound-buddy.mp3', 4, 7),
(5, 'Clear Day', 1, 5, 4, '1:29', 'assets/music/bensound-clearday.mp3', 5, 4),
(6, 'Going Higher', 2, 1, 1, '4:04', 'assets/music/bensound-goinghigher.mp3', 1, 9),
(7, 'Funny Song', 2, 4, 2, '3:07', 'assets/music/bensound-funnysong.mp3', 2, 11),
(8, 'Funky Element', 2, 1, 3, '3:08', 'assets/music/bensound-funkyelement.mp3', 2, 6),
(9, 'Extreme Action', 2, 1, 4, '8:03', 'assets/music/bensound-extremeaction.mp3', 3, 9),
(10, 'Epic', 2, 4, 5, '2:58', 'assets/music/bensound-epic.mp3', 3, 8),
(11, 'Energy', 2, 1, 6, '2:59', 'assets/music/bensound-energy.mp3', 4, 5),
(12, 'Dubstep', 2, 1, 7, '2:03', 'assets/music/bensound-dubstep.mp3', 5, 3),
(13, 'Happiness', 3, 6, 8, '4:21', 'assets/music/bensound-happiness.mp3', 5, 4),
(14, 'Happy Rock', 3, 6, 9, '1:45', 'assets/music/bensound-happyrock.mp3', 4, 7),
(15, 'Jazzy Frenchy', 3, 6, 10, '1:44', 'assets/music/bensound-jazzyfrenchy.mp3', 3, 3),
(16, 'Little Idea', 3, 6, 1, '2:49', 'assets/music/bensound-littleidea.mp3', 2, 12),
(17, 'Memories', 3, 6, 2, '3:50', 'assets/music/bensound-memories.mp3', 1, 3),
(18, 'Moose', 4, 7, 1, '2:43', 'assets/music/bensound-moose.mp3', 5, 5),
(19, 'November', 4, 7, 2, '3:32', 'assets/music/bensound-november.mp3', 4, 0),
(20, 'Of Elias Dream', 4, 7, 3, '4:58', 'assets/music/bensound-ofeliasdream.mp3', 3, 3),
(21, 'Pop Dance', 4, 7, 2, '2:42', 'assets/music/bensound-popdance.mp3', 2, 4),
(22, 'Retro Soul', 4, 7, 5, '3:36', 'assets/music/bensound-retrosoul.mp3', 1, 2),
(23, 'Sad Day', 5, 2, 1, '2:28', 'assets/music/bensound-sadday.mp3', 1, 2),
(24, 'Sci-fi', 5, 2, 2, '4:44', 'assets/music/bensound-scifi.mp3', 2, 6),
(25, 'Slow Motion', 5, 2, 3, '3:26', 'assets/music/bensound-slowmotion.mp3', 3, 4),
(26, 'Sunny', 5, 2, 4, '2:20', 'assets/music/bensound-sunny.mp3', 4, 5),
(27, 'Sweet', 5, 2, 5, '5:07', 'assets/music/bensound-sweet.mp3', 5, 6),
(28, 'Tenderness ', 3, 3, 7, '2:03', 'assets/music/bensound-tenderness.mp3', 4, 2);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(32) NOT NULL,
  `signUpDate` datetime NOT NULL,
  `profilePic` varchar(500) NOT NULL,
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `firstName`, `lastName`, `email`, `password`, `signUpDate`, `profilePic`) VALUES
(1, 'kamal', 'Kamal', 'Alyyyy', 'Kamal@yahoo.com', '827ccb0eea8a706c4c34a16891f84e7b', '2018-11-05 00:00:00', 'assets/images/profile-pics/user.jpg');



CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `email` varchar(200) NOT NULL,
  `password` varchar(32) NOT NULL,
 
PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `admin` (`id`, `username`, `firstName`, `lastName`, `email`, `password`) VALUES
(1, 'kamal', 'Kamal', 'Alyyyy', 'Kamal@yahoo.com', '12345');

--
-- Indexes for dumped tables
--

-- Create a table to store notifications
CREATE TABLE `notifications` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `message` varchar(255) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `fk_user_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Create a trigger to send notifications after a new user is created
DELIMITER //

CREATE TRIGGER `after_insert_user` AFTER INSERT ON `users`
FOR EACH ROW
BEGIN
  DECLARE target_user_id INT;
  SET target_user_id = NEW.id;  -- Assuming you want to track notifications for the newly inserted user

  IF NEW.id = target_user_id THEN
    INSERT INTO `notifications` (`user_id`, `message`) VALUES (target_user_id, 'Welcome! You have a new notification.');
  END IF;
END //

DELIMITER ;


--
-- Indexes for table `albums`
--
ALTER TABLE `albums`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `artists`
--
ALTER TABLE `artists`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `genres`
--
ALTER TABLE `genres`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlists`
--
ALTER TABLE `playlists`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `playlistssongs`
--
ALTER TABLE `playlistssongs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `songs`
--
ALTER TABLE `songs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
-- ALTER TABLE `users`
--   ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `albums`
--
ALTER TABLE `albums`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `artists`
--
-- ALTER TABLE `artists`
--   MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `genres`
--
ALTER TABLE `genres`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT for table `playlists`
--
ALTER TABLE `playlists`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `playlistssongs`
--
ALTER TABLE `playlistssongs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `songs`
--
ALTER TABLE `songs`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int  NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;COMMIT;
ALTER TABLE playlists
ADD FOREIGN KEY (owner) REFERENCES users(id);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;


-- DELIMITER //

-- CREATE TRIGGER `after_insert_song` AFTER INSERT ON `songs`
-- FOR EACH ROW
-- BEGIN
--   DECLARE user_id INT;
--   DECLARE message VARCHAR(255);
--   
--   -- Assuming you want to send a notification to all users
--   DECLARE user_cursor CURSOR FOR SELECT id FROM users;
--   OPEN user_cursor;
--   
--   read_loop: LOOP
--     FETCH user_cursor INTO user_id;
--     IF user_id IS NULL THEN
--       LEAVE read_loop;
--     END IF;
--     
--     SET message = CONCAT('New song added: ', NEW.title);
--     
--     INSERT INTO `notifications` (`user_id`, `message`) VALUES (user_id, message);
--   END LOOP;
--   
--   CLOSE user_cursor;
-- END //

-- DELIMITER ;

-- DELIMITER //

-- CREATE TRIGGER `after_insert_album` AFTER INSERT ON `albums`
-- FOR EACH ROW
-- BEGIN
--   DECLARE user_id INT;
--   DECLARE message VARCHAR(255);
--   
--   -- Assuming you want to send a notification to all users
--   DECLARE user_cursor CURSOR FOR SELECT id FROM users;
--   OPEN user_cursor;
--   
--   read_loop: LOOP
--     FETCH user_cursor INTO user_id;
--     IF user_id IS NULL THEN
--       LEAVE read_loop;
--     END IF;
--     
--     SET message = CONCAT('New album created: ', NEW.title);
--     
--     INSERT INTO `notifications` (`user_id`, `message`) VALUES (user_id, message);
--   END LOOP;
--   
--   CLOSE user_cursor;
-- END //

-- DELIMITER ;

-- DELIMITER //

-- CREATE TRIGGER `after_insert_artist` AFTER INSERT ON `artists`
-- FOR EACH ROW
-- BEGIN
--   DECLARE user_id INT;
--   DECLARE message VARCHAR(255);
  
--   -- Assuming you want to send a notification to all users
--   DECLARE user_cursor CURSOR FOR SELECT id FROM users;
--   OPEN user_cursor;
  
--   read_loop: LOOP
--     FETCH user_cursor INTO user_id;
--     IF user_id IS NULL THEN
--       LEAVE read_loop;
--     END IF;
    
--     SET message = CONCAT('New artist added: ', NEW.name);
    
--     INSERT INTO `notifications` (`user_id`, `message`) VALUES (user_id, message);
--   END LOOP;
  
--   CLOSE user_cursor;
-- END //

-- DELIMITER ;
CREATE TABLE `subscriptions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `planname` varchar(255) NOT NULL,
  `price` decimal(10, 2) NOT NULL,
  `startdate` date NOT NULL,
  `enddate` date NOT NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`userid`) REFERENCES `users`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Example data for the subscriptions table
INSERT INTO `subscriptions` (`userid`, `planname`, `price`, `startdate`, `enddate`) VALUES
(1, 'FREE', 0.00, '2023-01-01', '2030-12-31')
-- Add more subscription records as needed
;

-- Add foreign key constraint for the subscriptions table
ALTER TABLE `subscriptions`
  ADD FOREIGN KEY (`userid`) REFERENCES `users`(`id`);
-- Create a table for advertisements
-- Create a table for advertisements
-- Create a table for advertisements
CREATE TABLE `advertisements` (
  `ad_id` int(11) NOT NULL AUTO_INCREMENT,
  `userid` int(11) NOT NULL,
  `ad_name` varchar(255) NOT NULL,
  `company_name` varchar(255) NOT NULL,
  `ad_description` text NOT NULL,
  `ad_url` varchar(255) NOT NULL,
  `ad_clicks` int(11) DEFAULT 0,
  PRIMARY KEY (`ad_id`),
  FOREIGN KEY (`userid`) REFERENCES `users`(`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Example data for the advertisements table
INSERT INTO `advertisements` (`userid`, `ad_name`, `ad_description`, `ad_url`, `company_name`, `ad_clicks`) VALUES
(1, 'Ad1', 'Description for Ad1', 'https://wall.alphacoders.com/by_sub_category.php?id=172966&name=City+Wallpapers', 'ABC', 0);


-- Add foreign key constraint for the advertisements table
ALTER TABLE `advertisements`
  ADD FOREIGN KEY (`userid`) REFERENCES `users`(`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

DELIMITER //
CREATE TRIGGER after_insert_artist
AFTER INSERT ON artists
FOR EACH ROW
BEGIN
    -- Insert a notification for each user
    INSERT INTO notifications (user_id, message, timestamp)
    SELECT id, CONCAT('New artist added: ', NEW.name), NOW()
    FROM users;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER after_insert_song
AFTER INSERT ON songs
FOR EACH ROW
BEGIN
    -- Insert a notification for each user
    INSERT INTO notifications (user_id, message, timestamp)
    SELECT id, CONCAT('New song added: ', NEW.title), NOW()
    FROM users;
END;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER after_insert_album
AFTER INSERT ON albums
FOR EACH ROW
BEGIN
    -- Insert a notification for each user
    INSERT INTO notifications (user_id, message, timestamp)
    SELECT id, CONCAT('New album created: ', NEW.title), NOW()
    FROM users;
END;
//
DELIMITER ;






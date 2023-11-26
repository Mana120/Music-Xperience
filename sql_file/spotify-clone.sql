create database if not exists music;
use music;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";

-- Enable the event scheduler if not already enabled
SET GLOBAL event_scheduler = ON;


CREATE TABLE `albums` (
  `id` int(11) NOT NULL,
  `title` varchar(250) NOT NULL,
  `artist` int(11) NOT NULL,
  `genre` int(11) NOT NULL,
  `artworkPath` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO `albums` (`id`, `title`, `artist`, `genre`, `artworkPath`) VALUES
(1, 'Bacon and Eggs', 2, 4, '../images_music/images/artwork/clearday.jpg'),
(2, 'Pizza Head', 5, 10, '../images_music/images/artwork/energy.jpg'),
(3, 'Summer Hits', 3, 1, '../images_music/images/artwork/goinghigher.jpg'),
(4, 'The movie soundtrack', 2, 9, '../images_music/images/artwork/funkyelement.jpg'),
(5, 'Best of the Worst', 1, 3, '../images_music/images/artwork/popdance.jpg'),
(6, 'Hello World', 3, 6, '../images_music/images/artwork/ukulele.jpg'),
(7, 'Best beats', 4, 7, '../images_music/images/artwork/sweet.jpg');

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
(1, 'Acoustic Breeze', 1, 5, 8, '2:37', '../images_music/music/bensound-acousticbreeze.mp3', 1, 8),
(2, 'A new beginning', 1, 5, 1, '2:35', '../images_music/music/bensound-anewbeginning.mp3', 2, 6),
(3, 'Better Days', 1, 5, 2, '2:33', '../images_music/music/bensound-betterdays.mp3', 3, 3),
(4, 'Buddy', 1, 5, 3, '2:02', '../images_music/music/bensound-buddy.mp3', 4, 7),
(5, 'Clear Day', 1, 5, 4, '1:29', '../images_music/music/bensound-clearday.mp3', 5, 4),
(6, 'Going Higher', 2, 1, 1, '4:04', '../images_music/music/bensound-goinghigher.mp3', 1, 9),
(7, 'Funny Song', 2, 4, 2, '3:07', '../images_music/music/bensound-funnysong.mp3', 2, 11),
(8, 'Funky Element', 2, 1, 3, '3:08', '../images_music/music/bensound-funkyelement.mp3', 2, 6),
(9, 'Extreme Action', 2, 1, 4, '8:03', '../images_music/music/bensound-extremeaction.mp3', 3, 9),
(10, 'Epic', 2, 4, 5, '2:58', '../images_music/music/bensound-epic.mp3', 3, 8),
(11, 'Energy', 2, 1, 6, '2:59', '../images_music/music/bensound-energy.mp3', 4, 5),
(12, 'Dubstep', 2, 1, 7, '2:03', '../images_music/music/bensound-dubstep.mp3', 5, 3),
(13, 'Happiness', 3, 6, 8, '4:21', '../images_music/music/bensound-happiness.mp3', 5, 4),
(14, 'Happy Rock', 3, 6, 9, '1:45', '../images_music/music/bensound-happyrock.mp3', 4, 7),
(15, 'Jazzy Frenchy', 3, 6, 10, '1:44', '../images_music/music/bensound-jazzyfrenchy.mp3', 3, 3),
(16, 'Little Idea', 3, 6, 1, '2:49', '../images_music/music/bensound-littleidea.mp3', 2, 12),
(17, 'Memories', 3, 6, 2, '3:50', '../images_music/music/bensound-memories.mp3', 1, 3),
(18, 'Moose', 4, 7, 1, '2:43', '../images_music/music/bensound-moose.mp3', 5, 5),
(19, 'November', 4, 7, 2, '3:32', '../images_music/music/bensound-november.mp3', 4, 0),
(20, 'Of Elias Dream', 4, 7, 3, '4:58', '../images_music/music/bensound-ofeliasdream.mp3', 3, 3),
(21, 'Pop Dance', 4, 7, 2, '2:42', '../images_music/music/bensound-popdance.mp3', 2, 4),
(22, 'Retro Soul', 4, 7, 5, '3:36', '../images_music/music/bensound-retrosoul.mp3', 1, 2),
(23, 'Sad Day', 5, 2, 1, '2:28', '../images_music/music/bensound-sadday.mp3', 1, 2),
(24, 'Sci-fi', 5, 2, 2, '4:44', '../images_music/music/bensound-scifi.mp3', 2, 6),
(25, 'Slow Motion', 5, 2, 3, '3:26', '../images_music/music/bensound-slowmotion.mp3', 3, 4),
(26, 'Sunny', 5, 2, 4, '2:20', '../images_music/music/bensound-sunny.mp3', 4, 5),
(27, 'Sweet', 5, 2, 5, '5:07', '../images_music/music/bensound-sweet.mp3', 5, 6),
(28, 'Tenderness ', 3, 3, 7, '2:03', '../images_music/music/bensound-tenderness.mp3', 4, 2);

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
CREATE TABLE `likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `song_id` int(11) NOT NULL,
  `like_count` int(11) NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `firstName`, `lastName`, `email`, `password`, `signUpDate`, `profilePic`) VALUES
(1, 'kamal', 'Kamal', 'Alyyyy', 'Kamal@yahoo.com', '827ccb0eea8a706c4c34a16891f84e7b', '2018-11-05 00:00:00', 'assets/images/profile-pics/user.jpg');

--
-- Indexes for dumped tables
--
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
    INSERT INTO `notifications` (`user_id`, `message`) VALUES (target_user_id, 'Welcome! To MusicXperience.');
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
ALTER TABLE `albums`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

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
ALTER TABLE songs ADD COLUMN likes INT DEFAULT 0;

ALTER TABLE `users`
  MODIFY `id` int  NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;COMMIT;
ALTER TABLE playlists
ADD FOREIGN KEY (owner) REFERENCES users(id);


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


--Artist Notification
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

--Song Notification
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

--Album notification
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

--Subscription notification
DELIMITER //
CREATE TRIGGER after_insert_subscription
AFTER UPDATE ON subscriptions
FOR EACH ROW
BEGIN
    -- Insert a notification for each user
    INSERT INTO notifications (user_id, message, timestamp)
    SELECT id, CONCAT('Subscription changed to: ', NEW.planname), NOW()
    FROM users;
END;
//
DELIMITER ;

-- Create a trigger that fires after an insert on the likes table
DELIMITER //
CREATE TRIGGER after_like_insert
AFTER INSERT ON likes
FOR EACH ROW
BEGIN
    -- Increment the like count in the song table
    UPDATE songs
    SET likes = likes + 1
    WHERE id = NEW.song_id;
END;
//
DELIMITER ;



-- Create an event to delete old notifications every day
CREATE EVENT delete_old_notifications
  ON SCHEDULE
    EVERY 1 DAY
    STARTS TIMESTAMP(CURRENT_DATE, '00:00:00')
  DO
    DELETE FROM notifications
    WHERE timestamp < NOW() - INTERVAL 1 DAY;








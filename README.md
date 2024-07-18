# Music-Xperience

The MusicXperience project is a comprehensive music management system that integrates a
robust relational database to efficiently organize and store diverse music-related data,
including albums, artists, genres, songs, playlists, and user information. Users can create
accounts with unique usernames, providing personal details such as first and last names,
email addresses, and profile pictures. The system incorporates user authentication and
password protection to ensure secure access.

The music library is enriched with a vast collection of songs, each containing essential details
like title, artist, album, genre, duration, path, album order, and play count. Users can explore
and enjoy music across various genres and artists. The project facilitates playlist
management, allowing users to create and customize playlists with the ability to add songs
and define playlist orders. The likes tracking feature records user preferences, with a trigger
automatically updating the like count in the songs table after each insertion.

Notifications play a crucial role in keeping users informed about significant events, such as
the addition of new artists, songs, or albums, as well as changes in user subscriptions. The
subscription management system enables users to subscribe to different plans, each
associated with a specific price, start date, and end date. Changes in subscription plans trigger
notifications to inform users about modifications.

Additionally, an event scheduler is implemented to automatically delete old notifications
daily, ensuring a streamlined and up-to-date notification system. Overall, MusicXperience
aims to provide users with a feature-rich platform for managing and enjoying their music
preferences, while keeping them informed about relevant activities and updates within the
music library.

## Overview

Music Xperience is a music streaming web application made using MySQL database. It enables users to sign up, log in, create playlists, search for songs, view albums, and manage their music subscriptions. Administrators have additional functionalities to manage users and the music database.

## ER Diagram

<img width="1325" alt="350109135-cb118d12-ee7a-40e2-af09-f53833a4aebd" src="https://github.com/user-attachments/assets/0cd08acc-be8f-40ca-bf62-cc415d9cb161">

## Relational Schema

<img width="838" alt="350109269-c9c9ebb2-4a01-4f10-bfa8-729ae817367f" src="https://github.com/user-attachments/assets/0d8b9e6f-791f-4f72-a196-724e6c742503">

## Features

- **User Authentication:** Secure sign-up, login, and password recovery.
- **Admin and User Roles:** Distinct functionalities for administrators and regular users.
- **Music Management:** Create and manage playlists, search for songs, view albums, and play tracks.
- **Subscription Management:** Users can manage their subscriptions with different plans.
- **Custom Styling:** Personalized interface styling for an enhanced user experience.
- **Notifications:** Keep users informed about new content and subscription changes.

## Main Modules

### `app.py`

The main script that runs the Streamlit application. It handles user authentication, displays the main interface, and coordinates other functions based on user interaction.

### `login_signup.py`

Manages user authentication processes, including login, sign-up, password recovery, and admin login functionalities.

### `admin_operations.py`

Contains functions for administrative tasks such as managing users and the music database.

### `song_playlists_operations.py`

Handles operations related to songs, albums, and playlists, including searching for songs, displaying albums, and managing playlists.

### `notifications.py`

Manages user notifications, keeping users informed about important events like new content and subscription updates.



Login Page 

![image](https://github.com/Mana120/Music-Xperience/assets/90771545/2ca87102-e874-4bb3-93fa-58aa3d3a5ded)


User Page

![image](https://github.com/Mana120/Music-Xperience/assets/90771545/5ebec33c-620d-450b-b455-ab4079de9a79)

Admin Page

![image](https://github.com/Mana120/Music-Xperience/assets/90771545/f785914a-db6b-45fd-a867-af961dc2f7ce)

## Contributors
- Shreya Kashyap ([@Shreya241103](https://github.com/shreya241103))
- Sai Manasa Nadimpalli ([@Mana120](https://github.com/Mana120))




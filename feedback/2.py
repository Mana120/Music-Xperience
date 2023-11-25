import streamlit as st
import mysql.connector

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@1989",
    database="music1"
)

# Example 1: Get Songs by Artist
def get_songs_by_artist(artist_name):
    cursor = conn.cursor(buffered=True)
    args = (artist_name,)
    cursor.callproc("GetSongsByArtist", args)
    songs = cursor.fetchall()
    cursor.close()  
    return [song[0] for song in songs]

# Example 2: Get Playlists Count for User
def get_playlists_count_for_user(user_id):
    cursor = conn.cursor(buffered=True)
    args = (user_id,)
    cursor.callproc("GetPlaylistsCountForUser", args)
    playlist_count = cursor.fetchone()[0]
    cursor.close()
    return playlist_count

# Example 3: Get Top Songs by Genre
def get_top_songs_by_genre(genre_name, limit_count):
    cursor = conn.cursor(buffered=True)
    args = (genre_name, limit_count)
    cursor.callproc("GetTopSongsByGenre", args)
    top_songs = cursor.fetchall()
    cursor.close()
    return top_songs

# Example 4: Get User Subscriptions
def get_user_subscriptions(user_id):
    cursor = conn.cursor(buffered=True)
    args = (user_id,)
    cursor.callproc("GetUserSubscriptions", args)
    subscriptions = cursor.fetchall()
    cursor.close()
    return subscriptions

# Example 5: Get Advertisements
def get_advertisements():
    cursor = conn.cursor(buffered=True)
    cursor.callproc("GetAdvertisements")
    advertisements = cursor.fetchall()
    cursor.close()
    return advertisements

# Example usage
st.title("Music App Analytics")

# Example 1
artist_name = "Mickey Mouse"
st.header(f"Songs by {artist_name}")
songs = get_songs_by_artist(artist_name)
st.write(songs)

# # Example 2
# user_id = 1
# playlist_count = get_playlists_count_for_user(user_id)
# st.header(f"Playlists Count for User {user_id}")
# st.write(f"Number of playlists: {playlist_count}")

# # Example 3
# genre_name = "Rock"
# limit_count = 5
# st.header(f"Top Songs in {genre_name}")
# top_songs = get_top_songs_by_genre(genre_name, limit_count)
# st.write(top_songs)

# # Example 4
# st.header("User Subscriptions")
# user_subscriptions = get_user_subscriptions(user_id)
# st.write(user_subscriptions)

# # Example 5
# st.header("Advertisements")
# advertisements = get_advertisements()
# st.write(advertisements)

# # Close the MySQL connection
# conn.close()

import streamlit as st
import mysql.connector
import pandas as pd
from pydub import AudioSegment
from io import BytesIO
from PIL import Image
from datetime import datetime
import random
import hashlib

from artists import get_unique_artists

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@1989",
    database="music"
)

def is_procedure_exists(cursor, procedure_name):
    cursor.execute(
        "SHOW PROCEDURE STATUS WHERE Db = DATABASE() AND Name = %s", (procedure_name,))
    return cursor.rowcount > 0


def get_user_playlists(user_id):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT name FROM playlists WHERE owner = %s", (user_id,))
    playlists = cursor.fetchall()
    cursor.close()
    conn.commit()
    return [playlist[0] for playlist in playlists]


def get_playlist_id_by_name(playlist_name):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT id FROM playlists WHERE name = %s",
                   (playlist_name,))
    result = cursor.fetchone()
    cursor.close()
    conn.commit()
    return result[0] if result else None


def create_playlist(name, owner):
    date_created = datetime.now()
    cursor = conn.cursor(buffered=True)

    if is_procedure_exists(cursor, 'InsertPlaylist'):
        # If it exists, call the procedure
        cursor.callproc('InsertPlaylist', (name, owner, date_created))
        # Commit the changes
        cursor.fetchall()
        cursor.close()
        conn.commit()
    else:
        cursor.execute('''CREATE PROCEDURE InsertPlaylist(IN playlistName VARCHAR(255), IN playlistOwner INT, IN playlistDateCreated DATE)
                    BEGIN
                        INSERT INTO playlists (name, owner, dateCreated) VALUES (playlistName, playlistOwner, playlistDateCreated);
                    END;''')
        cursor.callproc('InsertPlaylist', (name, owner, date_created))
        # Commit the changes
        cursor.fetchall()
        cursor.close()
        conn.commit()
    st.success(f"Playlist '{name}' created successfully!")


def get_playlist_names(user_id):
    cursor = conn.cursor(buffered=True)
    cursor.execute(
        "SELECT id, name FROM playlists WHERE owner = %s", (user_id,))
    playlists = cursor.fetchall()
    cursor.close()
    conn.commit()
    return {playlist[1]: playlist[0] for playlist in playlists}


def add_songs_to_playlist(playlist_id, song_titles):
    cursor = conn.cursor(buffered=True)
    for song_title in song_titles:
        # Look up the song_id based on the song_title
        cursor.execute("SELECT id FROM songs WHERE title = %s", (song_title,))
        result = cursor.fetchone()

        if result:
            song_id = result[0]
            cursor.execute(
                "INSERT INTO playlistssongs (songId, playlistId, playlistOrder) VALUES (%s, %s, %s)", (song_id, playlist_id, 0))
        else:
            st.warning(f"Song not found: {song_title}")

    cursor.close()
    conn.commit()
    st.success("Songs added to the playlist successfully!")


def create_playlist_page(user_id):
    st.header("Create Playlist")
    playlist_name = st.text_input("Enter Playlist Name:")
    if st.button("Create Playlist"):
        create_playlist(playlist_name, user_id)


def display_all_albums():
    cursor = conn.cursor(buffered=True)
    query = "SELECT * FROM albums;"
    cursor.execute(query)
    albums = cursor.fetchall()
    cursor.close()
    conn.commit()
    return albums


def get_song_names():
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT id, title FROM songs")
    songs = cursor.fetchall()
    cursor.close()
    conn.commit()
    return {song[1]: song[0] for song in songs}


def get_songs_by_artist(artist_name):
    cursor = conn.cursor(buffered=True)
    query = "SELECT * FROM songs WHERE artist = (SELECT id FROM artists WHERE name = %s)"
    cursor.execute(query, (artist_name,))
    songs = cursor.fetchall()
    cursor.close()
    conn.commit()
    return songs


def render_songs_by_artist(songs, user_id):
    a = len(songs)
    i = 0
    col1, col2 = st.columns(2)
    for song in songs:
        if (i < a/2):
            with col1:
                st.write(f"**{song[1]} - {song[5]}**")

                # Play the song using st.audio
                audio_path = song[6]
                st.audio(audio_path, format="audio/mp3", start_time=0)

                # Use a unique key for each like button
                random_key = random.randint(1, 1000000)
                if st.button("Like", key=random_key):
                    handle_like(song[0], user_id)
        else:
            with col2:
                st.write(f"**{song[1]} - {song[5]}**")

                # Play the song using st.audio
                audio_path = song[6]
                st.audio(audio_path, format="audio/mp3", start_time=0)

                # Use a unique key for each like button
                like_button_key = f"like_button_{song[0]}_{user_id}"
                if st.button("Like", key=like_button_key):
                    handle_like(song[0], user_id)
        i = i+1


def display_songs_by_artist(user_id):

    # Get the unique artist names
    artist_names = get_unique_artists()

    # Let the user select an artist from the dropdown
    selected_artist = st.selectbox("Select an artist", artist_names)

    # Display songs by the selected artist
    songs = get_songs_by_artist(selected_artist)
    if songs:
        render_songs_by_artist(songs, user_id)
    else:
        st.info(f"No songs found for {selected_artist}.")
# Function to add songs to a playlist


def search_song(query):
    cursor = conn.cursor(buffered=True)
    # search_query = f"SELECT * FROM songs WHERE title LIKE '%{query}%' OR artist LIKE '%{query}%';"
    search_query = f"""
        SELECT songs.*, albums.artworkPath as albumArtworkPath
        FROM songs
        JOIN albums ON songs.album = albums.id
        WHERE songs.title LIKE '%{query}%' OR songs.artist LIKE '%{query}%';
    """
    cursor.execute(search_query)
    results = cursor.fetchall()
    cursor.close()
    conn.commit()

    return results


def handle_like(song_id, user_id):
    # print(song_id)
    cursor = conn.cursor(buffered=True)
    # cursor.execute("UPDATE songs SET likes = likes + 1 WHERE id = %s", (song_id,))
    cursor.execute("INSERT INTO likes (user_id, song_id, like_count) VALUES (%s, %s, 1) ON DUPLICATE KEY UPDATE like_count = like_count + 1",
                   (user_id, song_id))
    cursor.close()
    conn.commit()


def is_procedure_exists(cursor, procedure_name):
    cursor = conn.cursor(buffered=True)
    cursor.execute(
        "SHOW PROCEDURE STATUS WHERE Db = DATABASE() AND Name = %s", (procedure_name,))
    cursor.close()
    conn.commit()
    return cursor.rowcount > 0


def play_song(song_path):
    st.audio(song_path, format="audio/mp3", start_time=0)
    cursor = conn.cursor(buffered=True)
    if is_procedure_exists(cursor, 'IncrementSongPlays'):
        # If it exists, call the procedure
        cursor.callproc('IncrementSongPlays', (song_path,))
        # Commit the changes
        cursor.fetchall()
        conn.commit()
        cursor.close()
    else:
        cursor.execute('''CREATE PROCEDURE IncrementSongPlays(IN songPath VARCHAR(255))
                        BEGIN
                            DECLARE currentPlays INT;

                            -- Get the current number of plays
                            SELECT plays INTO currentPlays FROM songs WHERE path = songPath;

                            -- Update the 'plays' column by incrementing it by one
                            UPDATE songs SET plays = currentPlays + 1 WHERE path = songPath;

                            -- Commit the changes
                            COMMIT;
                        END''')
        cursor.callproc('IncrementSongPlays', (song_path,))
        cursor.fetchall()

        conn.commit()
        cursor.close()


def render_playlist_songs(songs, user_id):
    a = len(songs)
    i = 0
    col1, col2 = st.columns(2)
    for song in songs:
        if (i < a/2):
            with col1:
                # Display song title and genre
                st.write(f"**{song[1]} - {song[3]}**")
                st.audio(song[2], format="audio/mp3")

                # Use a unique key for each like button
                random_key = random.randint(1, 1000000)
                if st.button("Like", key=random_key):
                    handle_like(song[0], user_id)
        else:
            with col2:
                # Display song title and genre
                st.write(f"**{song[1]} - {song[3]}**")
                st.audio(song[2], format="audio/mp3")

            # Use a unique key for each like button
                random_key = random.randint(1, 1000000)
                like_button_key = f"like_button_{song[0]}_{user_id}_{random_key}"
                if st.button("Like", key=like_button_key):
                    handle_like(song[0], user_id)
        i = i+1


def play_all_songs(playlist_id, user_id, shuffle=False):
    cursor = conn.cursor(buffered=True)
    cursor.execute("""
        SELECT songs.id,songs.title, songs.path, genres.name as genre_name
        FROM songs
        JOIN playlistssongs ON songs.id = playlistssongs.songId
        JOIN genres ON songs.genre = genres.id
        WHERE playlistssongs.playlistId = %s
    """, (playlist_id,))
    songs = cursor.fetchall()

    if shuffle:
        random.shuffle(songs)  # Shuffle the songs if shuffle is True

    render_playlist_songs(songs, user_id)
    cursor.close()
    conn.commit()


def render_songs_in_album(songs, user_id):
    a = len(songs)
    i = 0
    col1, col2 = st.columns(2)
    for song in songs:
        if (i < a/2):
            with col1:
                st.write(f"**{song[1]} - {song[5]}**")
                audio_path = song[6].strip()
                st.audio(audio_path, format="audio/mp3", start_time=0)
                like_button_key = f"like_button_{song[0]}_{user_id}"

                if st.button("Like Song", key=like_button_key):
                    handle_like(song[0], user_id)
        else:
            with col2:
                st.write(f"**{song[1]} - {song[5]}**")
                audio_path = song[6].strip()
                st.audio(audio_path, format="audio/mp3", start_time=0)
                like_button_key = f"like_button_{song[0]}_{user_id}"

                if st.button("Like Song", key=like_button_key):
                    handle_like(song[0], user_id)
        i = i+1


def display_all_songs_in_album(album_id, user_id):
    cursor = conn.cursor(buffered=True)
    query = "SELECT * FROM songs WHERE album = %s"
    cursor.execute(query, (album_id,))
    songs = cursor.fetchall()
    query = "SELECT * FROM albums WHERE id = %s"
    cursor.execute(query, (album_id,))
    album_info = cursor.fetchone()
    cursor.close()
    conn.commit()

    st.subheader("Songs in the Album:")
    if songs:
        render_songs_in_album(songs, user_id)
    else:
        st.info("No songs found for this album.")


def render_songs_by_genre(songs, user_id):
    a = len(songs)
    i = 0
    col1, col2 = st.columns(2)
    for song in songs:
        if (i < a/2):
            with col1:
                st.write(f"**{song[1]}**")
                st.audio(song[2], format="audio/mp3")
                like_button_key = f"like_button_{song[0]}_{user_id}"
                if st.button("Like", key=like_button_key):

                    handle_like(song[0], user_id)
        else:
            with col2:
                st.write(f"**{song[1]}**")
                st.audio(song[2], format="audio/mp3")

                # Use a unique key for each like button
                like_button_key = f"like_button_{song[0]}_{user_id}"
                if st.button("Like", key=like_button_key):

                    handle_like(song[0], user_id)
        i = i+1


def display_songs_by_genre(user_id):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM genres")
    genres = cursor.fetchall()
    genre_names = [genre[1] for genre in genres]

    # Display genre selection dropdown
    selected_genre = st.selectbox("Select Genre", genre_names)

    # Find the genre_id based on the selected genre name
    genre_id = [genre[0] for genre in genres if genre[1] == selected_genre][0]
    cursor = conn.cursor(buffered=True)
    cursor.execute("""
        SELECT songs.id,songs.title, songs.path
        FROM songs
        WHERE songs.genre = %s
    """, (genre_id,))
    songs = cursor.fetchall()

    st.write(f"**Genre Songs:**")

    if songs:
        render_songs_by_genre(songs, user_id)
    else:
        st.info("No songs found for this genre.")
    cursor.close()
    conn.commit()


def add_songs_to_playlist_page(user_id):
    st.header("Add Songs to Playlist")
    playlist_id = st.selectbox(
        "Select Playlist", get_playlist_names(st.session_state.user_id))
    playlist_id = get_playlist_id_by_name(playlist_id)
    selected_songs = st.multiselect("Select Songs", get_song_names())
    return playlist_id, selected_songs


def get_like_playlists(user_id):
    cursor = conn.cursor(buffered=True)
    cursor.execute("""
        SELECT likes.song_id 
        FROM likes
        WHERE likes.user_id = %s
    """, (user_id,))
    songs = cursor.fetchall()
    cursor.close()
    conn.commit()
    return songs


def play_liked_songs(songs):
    a = len(songs)
    i = 0
    cursor = conn.cursor(buffered=True)
    col1, col2 = st.columns(2)
    for song in songs:
        if (i < a/2):
            with col1:
                cursor.execute("""
                    SELECT songs.path,songs.title
                    FROM songs
                    WHERE songs.id = %s
                """, (song[0],))
                songs_1 = cursor.fetchall()
                audio_path = songs_1[0][0]
                st.write(f"**{songs_1[0][1]}**")
                st.audio(audio_path, format="audio/mp3", start_time=0)
        else:
            with col2:
                cursor.execute("""
                SELECT songs.path,songs.title
                FROM songs
                WHERE songs.id = %s
                """, (song[0],))
                songs_1 = cursor.fetchall()
                audio_path = songs_1[0][0]
                st.write(f"**{songs_1[0][1]}**")
                st.audio(audio_path, format="audio/mp3", start_time=0)
        i = i+1
    cursor.close()
    conn.commit()


def display_recommmendation_genre(genre_id, user_id):
    cursor = conn.cursor(buffered=True)
    cursor = conn.cursor(buffered=True)
    cursor.execute("""
        SELECT songs.id,songs.title, songs.path
        FROM songs
        WHERE songs.genre = %s
    """, (genre_id,))
    songs = cursor.fetchall()

    st.write(f"**Genre Songs:**")

    if songs:
        render_songs_by_genre(songs, user_id)
    else:
        st.info("No songs found for this genre.")
    cursor.close()
    conn.commit()


def get_recommendation(user_id):
    cursor = conn.cursor(buffered=True)
    query = """
                SELECT genre, COUNT(*) as genre_count
                FROM (
                    SELECT genre FROM songs WHERE id IN (SELECT song_id FROM likes)
                    UNION ALL
                    SELECT genre FROM songs WHERE id IN (
                        SELECT songID FROM playlistssongs WHERE playlistId IN (
                            SELECT id FROM playlists WHERE owner = 2
                        )
                    )
                ) AS combined_genres
                GROUP BY genre
                ORDER BY genre_count DESC
                LIMIT 1;
            """

    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    cursor.close()
    conn.commit()

    return result


def play_all_songs_page(user_id):
    # Fetch playlists owned by the user
    user_playlists = get_user_playlists(user_id)
    like_playlist = get_like_playlists(user_id)
    genre_recommendation = get_recommendation(user_id)

    # Initialize session state variables
    if "button8" not in st.session_state:
        st.session_state.button8 = False

    if "button12" not in st.session_state:
        st.session_state.button12 = False

    # Play Liked Songs Playlist Button
    if like_playlist:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("Play Liked Songs Playlist", key=f"{user_id}_like"):
            st.markdown("<br>", unsafe_allow_html=True)
            st.session_state.button8 = not st.session_state.button8
    if st.session_state.button8:
        play_liked_songs(like_playlist)
        st.markdown("<br>", unsafe_allow_html=True)
    # Play Recommendation Button
    if genre_recommendation:
        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        random_key = random.randint(1, 1000000)
        if st.button("Play Recommendation", key=f"{user_id}_recommendation"):
            st.markdown("<br>", unsafe_allow_html=True)
            st.session_state.button12 = not st.session_state.button12

    # Execute actions based on button state

    if st.session_state.button12:
        # print("ji")
        display_recommmendation_genre(genre_recommendation['genre'], user_id)
        st.markdown("<br>", unsafe_allow_html=True)

    # Rest of your code for selecting and playing playlists
    if not user_playlists or not like_playlist:
        st.info("You haven't created any playlists yet. Create one to get started!")
        return

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    playlist_name = st.selectbox("Select Playlist", user_playlists)
    playlist_id = get_playlist_id_by_name(playlist_name)
    shuffle_button = st.button("Shuffle Songs")

    # Check if the shuffle button is pressed
    if (not (st.session_state.button12) and not (st.session_state.button8)):
        if shuffle_button:
            if st.session_state.plan_name != "FREE":
                play_all_songs(playlist_id, user_id, shuffle=True)
            else:
                styled_text = f"<p style='font-size: 24px; color: red;'>You are a FREE user. Buy GOLD and SILVER subscriptions to avail premium features</p>"
                st.markdown(styled_text, unsafe_allow_html=True)
                play_all_songs(playlist_id, user_id)
        else:
            play_all_songs(playlist_id, user_id)

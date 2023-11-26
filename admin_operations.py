import streamlit as st
import mysql.connector
from datetime import datetime
import hashlib
import matplotlib as plt
import plotly.express as px
import pandas as pd
from tabulate import tabulate
# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="music"
)
def is_procedure_exists(cursor, procedure_name):
    cursor.execute("SHOW PROCEDURE STATUS WHERE Db = DATABASE() AND Name = %s", (procedure_name,))
    return cursor.rowcount > 0
def add_song(song_id, title, artist, album, genre, duration, path, album_order, plays):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO songs (id, title, artist, album, genre, duration, path, albumOrder, plays)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (song_id, title, artist, album, genre, duration, path, album_order, plays))
    conn.commit()
    st.success("Song added successfully!")

def delete_song(song_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM songs WHERE id = %s", (song_id,))
    conn.commit()
    st.success("Song deleted successfully!")

def admin_options():
    st.subheader("Admin Options:")
    option = st.radio("Select an admin option", ["Add Song", "Delete Song", "Create Album", "Delete Album", "Add Artist", "Delete Artist","Subscrption Deatils","statistics"])
    
    if option == "Add Song":
        add_song_page()
    elif option == "Delete Song":
        delete_song_page()
    elif option == "Create Album":
        create_album_page()
    elif option == "Delete Album":
        delete_album_page()
    elif option == "Add Artist":
        add_artist_page()
    elif option == "Delete Artist":
        delete_artist_page()
    elif option == "Subscrption Deatils":
        subscription()
    elif option == "statistics":
        most_listened_graphs()

def create_album_page():
    st.markdown('<p style="color: black; font-size: 38px; font-weight: bold;">Create Album</p>', unsafe_allow_html=True)
    album_id = st.text_input("Album ID:")
    title = st.text_input("Title:")
    artist = st.text_input("Artist:")
    genre = st.text_input("Genre:")
    artwork_path = st.text_input("Artwork Path:")

    if st.button("Create Album"):
        create_album(album_id, title, artist, genre, artwork_path)

def delete_album_page():
    st.markdown('<p style="color: black; font-size: 38px; font-weight: bold;">Delete Album</p>', unsafe_allow_html=True)

    # Fetch the list of albums for deletion
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM albums")
    albums = cursor.fetchall()
    
    # Display checkboxes for each album
    selected_albums = st.multiselect("Select albums to delete:", [f"{id} - {title}" for id, title in albums])

    if st.button("Delete Selected Albums"):
        for selected_album in selected_albums:
            album_id = int(selected_album.split(" - ")[0])
            delete_album(album_id)

def add_artist_page():
    st.markdown('<p style="color: black; font-size: 38px; font-weight: bold;">Add Artist</p>', unsafe_allow_html=True)
    # st.title("Add Artist")
    artist_id = st.text_input("Artist ID:")
    name = st.text_input("Name:")

    if st.button("Add Artist"):
        add_artist(artist_id, name)

def delete_artist_page():
    st.markdown('<p style="color: black; font-size: 38px; font-weight: bold;">Delete Artist</p>', unsafe_allow_html=True)

    # st.title("Delete Artist")
    # Fetch the list of artists for deletion
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM artists")
    artists = cursor.fetchall()
    
    # Display checkboxes for each artist
    selected_artists = st.multiselect("Select artists to delete:", [f"{id} - {name}" for id, name in artists])

    if st.button("Delete Selected Artists"):
        for selected_artist in selected_artists:
            artist_id = int(selected_artist.split(" - ")[0])
            delete_artist(artist_id)

def create_album(album_id, title, artist, genre, artwork_path):
    
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO albums (id, title, artist, genre, artworkPath)
        VALUES (%s, %s, %s, %s, %s)
    """, (album_id, title, artist, genre, artwork_path))
    conn.commit()
    st.success("Album created successfully!")

def delete_album(album_id):
    cursor = conn.cursor(buffered=True)
    if is_procedure_exists(cursor, 'DeleteAlbum'):
        # If it exists, call the procedure
        cursor.callproc('DeleteAlbum', (album_id,))
            # Commit the changes
        cursor.fetchall()
        cursor.close()
        conn.commit()
    else:
        cursor.execute('''CREATE PROCEDURE DeleteAlbum(IN album_id INT)
                        BEGIN
                            DELETE FROM albums WHERE id= album_id;
                        END;''')
        cursor.callproc('DeleteArtist', (album_id,))
            # Commit the changes
        cursor.fetchall()
        cursor.close()
        conn.commit()
    st.success("Album deleted successfully!")

def add_artist(artist_id, name):
    cursor = conn.cursor()

    # Check if the artist with the given ID already exists
    cursor.execute("SELECT * FROM artists WHERE id = %s", (artist_id,))
    existing_artist = cursor.fetchone()

    if existing_artist:
        # Artist already exists, update the name
        cursor.execute("UPDATE artists SET name = %s WHERE id = %s", (name, artist_id))
        st.success("Artist updated successfully!")
    else:
        # Artist doesn't exist, insert a new record
        cursor.execute("INSERT INTO artists (id, name) VALUES (%s, %s)", (artist_id, name))
        st.success("Artist added successfully!")

    conn.commit()


def delete_artist(artist_id):
    cursor = conn.cursor(buffered=True)
    if is_procedure_exists(cursor, 'DeleteArtists'):
        # If it exists, call the procedure
        cursor.callproc('DeleteArtist', (artist_id,))
            # Commit the changes
        cursor.fetchall()
        cursor.close()
        conn.commit()
    else:
        cursor.execute('''CREATE PROCEDURE DeleteArtist(IN artistId INT)
                        BEGIN
                            DELETE FROM artists WHERE id = artistId;
                        END;''')
        cursor.callproc('DeleteArtist', (artist_id,))
            # Commit the changes
        cursor.fetchall()
        cursor.close()
        conn.commit()
    st.success("Artist deleted successfully!")


def add_song_page():
    st.markdown('<p style="color: forestgreen; font-size: 38px; font-weight: bold;">Add Song</p>', unsafe_allow_html=True)
    song_id = st.text_input("Song ID:")
    title = st.text_input("Title:")
    artist = st.text_input("Artist:")
    album = st.text_input("Album:")
    genre = st.text_input("Genre:")
    duration = st.text_input("Duration:")
    path = st.text_input("Path:")
    album_order = st.number_input("Album Order:", min_value=1, step=1, value=1)
    plays = st.number_input("Plays:", min_value=0, step=1, value=0)

    if st.button("Add Song"):
        add_song(title, artist, album, genre, duration, path, album_order, plays)

def delete_song_page():
    st.markdown('<p style="color: forestgreen; font-size: 38px; font-weight: bold;">Delete Song</p>', unsafe_allow_html=True)
    # Fetch the list of songs for deletion
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM songs")
    songs = cursor.fetchall()
    
    # Display checkboxes for each song
    selected_songs = st.multiselect("Select songs to delete:", [f"{id} - {title}" for id, title in songs])

    if st.button("Delete Selected Songs"):
        for selected_song in selected_songs:
            song_id = int(selected_song.split(" - ")[0])
            delete_song(song_id)

def most_listened_graphs():
    st.subheader("Most Listened Graphs:")
    option = st.selectbox("Select an option", ["Most Listened Songs", "Most Listened Artists", "Most Listened Albums","popular songs per genre"])

    if option == "Most Listened Songs":
        display_most_listened_songs()
    elif option == "Most Listened Artists":
        display_most_listened_artists()
    elif option == "Most Listened Albums":
        display_most_listened_albums()
    elif option == "popular songs per genre":
        popular_songs_gener()


def display_most_listened_songs():
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, plays FROM songs ORDER BY plays DESC LIMIT 5")
    songs_data = cursor.fetchall()
    
    df = pd.DataFrame(songs_data, columns=['Song ID', 'Title', 'Plays'])
    st.dataframe(df)
    fig = px.bar(df, x='Title', y='Plays', title='Most Listened Songs')
    fig.update_layout(height=600, width=1370)  # Adjust the height and width as needed
    st.plotly_chart(fig)
    


def get_most_listened_artists():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT artists.name, SUM(songs.plays) as total_plays
        FROM artists
        JOIN songs ON artists.id = songs.artist
        GROUP BY artists.name
        ORDER BY total_plays DESC
        LIMIT 5
    """)
    artists_data = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(artists_data, columns=['Name', 'Total Plays'])
    return df

def display_most_listened_artists():
    # Get the most listened artists
    most_listened_artists_df = get_most_listened_artists()

    # Display the dataframe
    st.dataframe(most_listened_artists_df)

    fig = px.bar(most_listened_artists_df, x='Name', y='Total Plays', title='Most Listened Artists')
    fig.update_layout(height=600, width=1370)  # Adjust the height and width as needed
    st.plotly_chart(fig)

def get_most_listened_albums():
    cursor = conn.cursor()
    cursor.execute("""
        SELECT albums.title, SUM(songs.plays) as total_plays
        FROM albums
        JOIN songs ON albums.id = songs.album
        GROUP BY albums.title
        ORDER BY total_plays DESC
        LIMIT 5
    """)
    albums_data = cursor.fetchall()
    cursor.close()

    df = pd.DataFrame(albums_data, columns=['Title', 'Total Plays'])
    return df

def display_most_listened_albums():
    # Get the most listened albums
    most_listened_albums_df = get_most_listened_albums()

    # Display the dataframe
    st.dataframe(most_listened_albums_df)

    fig = px.bar(most_listened_albums_df, x='Title', y='Total Plays', title='Most Listened Albums')
    fig.update_layout(height=600, width=1370)  # Adjust the height and width as needed
    st.plotly_chart(fig)

def popular_songs_gener():
    cursor = conn.cursor()
    cursor.execute('''SELECT genres.name AS genre_name, songs.title AS song_name, artists.name AS artist_name, songs.plays
FROM songs
JOIN (
    SELECT genre, MAX(plays) AS max_plays
    FROM songs
    GROUP BY genre
) AS max_plays_per_genre ON songs.genre = max_plays_per_genre.genre AND songs.plays = max_plays_per_genre.max_plays
JOIN genres ON songs.genre = genres.id
JOIN artists ON songs.artist = artists.id
ORDER BY genres.name, songs.plays DESC;''')
    results = cursor.fetchall()
    columns = ["genre_name","Song_name","Artist","plays"]
    df = pd.DataFrame(results, columns=columns)

        # Display results using Streamlit data table
    st.dataframe(df)
    
    
def free_sub():
    cursor = conn.cursor(buffered=True)

        # Execute the SQL query
    query = """
            SELECT id, username, firstName, lastName, signUpDate
            FROM users
            WHERE id IN (
                SELECT userid
                FROM subscriptions
                WHERE planname = 'FREE'
            ) AND id <> 1;
        """
    cursor.execute(query)
    results = cursor.fetchall()

        # Create a DataFrame
    columns = ["ID", "Username", "First Name", "Last Name", "Sign-Up Date"]
    df = pd.DataFrame(results, columns=columns)

        # Display results using Streamlit data table
    st.dataframe(df)
    cursor.execute('''SELECT COUNT(username) AS user_count
                FROM users
                WHERE id IN (
                    SELECT userid
                    FROM subscriptions
                    WHERE planname = 'FREE'
                )AND id <> 1;''')
        # Fetch the results'
    result = cursor.fetchone()


    # Display the result using Streamlit
    st.write(f"Number of users with FREE subscription: {result[0]}")
    cursor.close()
    conn.commit()

    

def silver_sub():
    cursor = conn.cursor(buffered=True)

        # Execute the SQL query
    query = """
            SELECT  id, username, firstName, lastName, signUpDate
            FROM users
            WHERE id IN (
                SELECT userid
                FROM subscriptions
                WHERE planname = 'Silver'
            );
        """
    cursor.execute(query)

        # Fetch the results
    results = cursor.fetchall()

        # Create a DataFrame
    columns = ["ID", "Username", "First Name", "Last Name", "Sign-Up Date"]
    df = pd.DataFrame(results, columns=columns)

        # Display results using Streamlit data table
    st.dataframe(df)
    cursor.execute('''SELECT COUNT(username) AS user_count
                FROM users
                WHERE id IN (
                    SELECT userid
                    FROM subscriptions
                    WHERE planname = 'Silver'
                );''')
        # Fetch the results'
    result = cursor.fetchone()


    # Display the result using Streamlit
    st.write(f"Number of users with Silver subscription: {result[0]}")
    cursor.close()
    conn.commit()

def gold_sub():
    cursor = conn.cursor(buffered=True)

        # Execute the SQL query
    query = """
            SELECT  id, username, firstName, lastName, signUpDate
            FROM users
            WHERE id IN (
                SELECT userid
                FROM subscriptions
                WHERE planname = 'Gold'
            );
        """
    cursor.execute(query)

        # Fetch the results
    results = cursor.fetchall()

        # Create a DataFrame
    columns = ["ID", "Username", "First Name", "Last Name", "Sign-Up Date"]
    df = pd.DataFrame(results, columns=columns)

        # Display results using Streamlit data table
    st.dataframe(df)
    cursor.execute('''SELECT COUNT(username) AS user_count
                FROM users
                WHERE id IN (
                    SELECT userid
                    FROM subscriptions
                    WHERE planname = 'Gold'
                );''')
        # Fetch the results'
    result = cursor.fetchone()


    # Display the result using Streamlit
    st.write(f"Number of users with Gold subscription: {result[0]}")
    cursor.close()
    conn.commit()
def subscription():
    st.subheader("Subscrption details:")
    option = st.selectbox("Select an option", ["FREE", "Gold", "Silver"])
    if option == "FREE":
        free_sub()
    elif option == "Gold":
        gold_sub()
    elif option == "Silver":
        silver_sub()





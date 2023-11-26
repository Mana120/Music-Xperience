from datetime import datetime, date, timedelta
import base64
import hashlib
import random
from PIL import Image
from io import BytesIO
from pydub import AudioSegment
import pandas as pd
import mysql.connector
from notifications import notifications_page
from login_signup import (
    logout, create_user, verify_user, login_page, signup_page, delete_user_and_entries, admin_login_page, forgot_password
)
from admin_operations import *
import streamlit as st
from song_playlists_operations import (
    display_all_albums, get_song_names, get_songs_by_artist, display_songs_by_artist,
    search_song, play_song, play_all_songs, display_all_songs_in_album, display_songs_by_genre,
    add_songs_to_playlist_page, play_all_songs_page, get_user_playlists, get_playlist_id_by_name,
    create_playlist, get_playlist_names, add_songs_to_playlist, create_playlist_page, handle_like
)

st.set_page_config(layout="wide")
temp = 0
var1 = []
# from subscription import s

temp = 0
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="music"
)
custom_css = """
    <style>
        /* Add your custom styles here */
        .stButton>button {
            background-color: purple;
            color: white;
            padding: 3px 8px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .stButton>button:hover {
            background-color: #CBC3E3;
        }

        .album-image {
            max-width: 200px;
            max-height: 200px;
            object-fit: cover;
            border-radius: 5px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: black !important;
        }

        [data-testid=stSidebar] {
            background-color: #008000;
        }
    </style>
"""

st.markdown(custom_css, unsafe_allow_html=True)
st.markdown("""
<style>
/* Add your custom styles here */
.stButton {
    background-color: #CBC3E3;
    color: white;
    padding: 3px 8px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-right: 4px;
    margin-top:0px;
}



h1, h2, h3, h4, h5, h6 {
    color: black !important;
}
</style>
<script>
function buttonClick(page) {
    // You can handle button click events here
    console.log(page + " clicked");
}
</script>
""", unsafe_allow_html=True)
custom_css = """
<style>
audio::-webkit-media-controls-panel,
audio::-webkit-media-controls-enclosure {
background-color:#CBC3E3;
}

audio::-webkit-media-controls-time-remaining-display,
audio::-webkit-media-controls-current-time-display {

color: black;
text-shadow: none;
}

audio::-webkit-media-controls-play-button {
background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAApgAAAKYB3X3/OAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAANCSURBVEiJtZZPbBtFFMZ/M7ubXdtdb1xSFyeilBapySVU8h8OoFaooFSqiihIVIpQBKci6KEg9Q6H9kovIHoCIVQJJCKE1ENFjnAgcaSGC6rEnxBwA04Tx43t2FnvDAfjkNibxgHxnWb2e/u992bee7tCa00YFsffekFY+nUzFtjW0LrvjRXrCDIAaPLlW0nHL0SsZtVoaF98mLrx3pdhOqLtYPHChahZcYYO7KvPFxvRl5XPp1sN3adWiD1ZAqD6XYK1b/dvE5IWryTt2udLFedwc1+9kLp+vbbpoDh+6TklxBeAi9TL0taeWpdmZzQDry0AcO+jQ12RyohqqoYoo8RDwJrU+qXkjWtfi8Xxt58BdQuwQs9qC/afLwCw8tnQbqYAPsgxE1S6F3EAIXux2oQFKm0ihMsOF71dHYx+f3NND68ghCu1YIoePPQN1pGRABkJ6Bus96CutRZMydTl+TvuiRW1m3n0eDl0vRPcEysqdXn+jsQPsrHMquGeXEaY4Yk4wxWcY5V/9scqOMOVUFthatyTy8QyqwZ+kDURKoMWxNKr2EeqVKcTNOajqKoBgOE28U4tdQl5p5bwCw7BWquaZSzAPlwjlithJtp3pTImSqQRrb2Z8PHGigD4RZuNX6JYj6wj7O4TFLbCO/Mn/m8R+h6rYSUb3ekokRY6f/YukArN979jcW+V/S8g0eT/N3VN3kTqWbQ428m9/8k0P/1aIhF36PccEl6EhOcAUCrXKZXXWS3XKd2vc/TRBG9O5ELC17MmWubD2nKhUKZa26Ba2+D3P+4/MNCFwg59oWVeYhkzgN/JDR8deKBoD7Y+ljEjGZ0sosXVTvbc6RHirr2reNy1OXd6pJsQ+gqjk8VWFYmHrwBzW/n+uMPFiRwHB2I7ih8ciHFxIkd/3Omk5tCDV1t+2nNu5sxxpDFNx+huNhVT3/zMDz8usXC3ddaHBj1GHj/As08fwTS7Kt1HBTmyN29vdwAw+/wbwLVOJ3uAD1wi/dUH7Qei66PfyuRj4Ik9is+hglfbkbfR3cnZm7chlUWLdwmprtCohX4HUtlOcQjLYCu+fzGJH2QRKvP3UNz8bWk1qMxjGTOMThZ3kvgLI5AzFfo379UAAAAASUVORK5CYII=");
}

audio::-webkit-media-controls-timeline {
background-color:#CBC3E3;

}
</style>
"""


def is_stored_procedure_exists(cursor, procedure_name):
    query = """
    SELECT COUNT(*)
    FROM information_schema.ROUTINES
    WHERE ROUTINE_TYPE = 'PROCEDURE' AND ROUTINE_NAME = %s;
    """
    cursor.execute(query, (procedure_name,))
    result = cursor.fetchone()
    return result[0] > 0


stored_procedure = """
CREATE PROCEDURE UpdateUserSubscription(IN userId INT, IN planName VARCHAR(255), IN price DECIMAL(10, 2), IN startDate DATE, IN endDate DATE)
BEGIN
    INSERT INTO subscriptions (userid, planname, price, startdate, enddate)
    VALUES (userId, planName, price, startDate, endDate)
    ON DUPLICATE KEY UPDATE
        planname = VALUES(planname),
        price = VALUES(price),
        startdate = VALUES(startdate),
        enddate = VALUES(enddate);
END
"""
cursor = conn.cursor()
if not is_stored_procedure_exists(cursor, "UpdateUserSubscription"):
    # Execute the stored procedure creation if it doesn't exist
    cursor.execute(stored_procedure)


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
        st.markdown(
            f"""
                    <style>
                    .stApp {{
                    background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
                    background-size: cover
                    }}
                    </style>
                    """,
            unsafe_allow_html=True
        )


add_bg_from_local('../images_music/images/q.jpg')
# Display the audio with custom styling
st.markdown(custom_css, unsafe_allow_html=True)


def main():

    if 'user_id' not in st.session_state:
        st.session_state.user_id = None
        st.session_state.username = None
        st.session_state.admin_id = None
        st.session_state.adname = None

    if st.session_state.user_id is None:
        st.markdown("# Music Xperience Login/Signup")
        useadmin = st.selectbox("Select an option", ["User", "Admin"])
        if useadmin == "User":
            page = st.radio("Select an option", [
                            "Login", "Signup", "Forgot Password"])
            if page == "Login":
                login_page()
            if page == "Signup":
                signup_page()
            if page == "Forgot Password":
                forgot_password()
        else:
            admin_login_page()
    else:
        if st.session_state.user_id == 1:  # Admin user_id
            cursor = conn.cursor(buffered=True)
            st.title(f"Welcome Admin,{st.session_state.username} !")
            cursor.execute(
                f"CREATE USER IF NOT EXISTS '{st.session_state.username}'@'%';")
            cursor.execute("CREATE ROLE IF NOT EXISTS 'admin';")
            cursor.execute("GRANT ALL PRIVILEGES ON *.* TO 'admin';")
            cursor.execute(
                f"GRANT admin TO '{st.session_state.username}'@'%';")
            admin_options()

            cursor.close()
        else:
            cursor = conn.cursor(buffered=True)
            cursor.execute(
                f"CREATE USER IF NOT EXISTS'{st.session_state.username}'@'%';")
            cursor.execute("CREATE ROLE IF NOT EXISTS 'user';")
            cursor.execute(
                "GRANT SELECT, INSERT, UPDATE, DELETE ON music.* TO 'user';")
            cursor.execute(f"GRANT user TO '{st.session_state.username}'@'%';")
            cursor.close()
            st.title(f"Welcome, {st.session_state.username}!")
            if 'user_settings_open' not in st.session_state:
                st.session_state.user_settings_open = False
            if 'create_playlist_open' not in st.session_state:
                st.session_state.create_playlist_open = False
            if 'play_song' not in st.session_state:
                st.session_state.play_song = False
            if 'play_album' not in st.session_state:
                st.session_state.play_album = True
            if 'add_song' not in st.session_state:
                st.session_state.add_song = False
            if 'play_playlist' not in st.session_state:
                st.session_state.play_playlist = False
            if 'song_artist' not in st.session_state:
                st.session_state.song_artist = False
            if 'song_genre' not in st.session_state:
                st.session_state.song_genre = False
            if 'sub' not in st.session_state:
                st.session_state.sub = False
            if 'search' not in st.session_state:
                st.session_state.search = False

            # Render User Settings dropdown button
            user_settings = st.button("User Settings")

            # Display buttons when User Settings is clicked
            if user_settings:
                st.session_state.user_settings_open = not st.session_state.user_settings_open

            if st.session_state.user_settings_open:

                # Buttons for Logout, Delete Account, and Notifications
                if st.button("Logout"):
                    # Handle Logout logic
                    logout()
                    st.session_state.user_id = None
                    st.session_state.username = None

                if st.button("Delete Account"):
                    # Handle Delete Account logic
                    delete_user_and_entries(st.session_state.user_id)
                    st.session_state.user_id = None
                    st.session_state.username = None

                if st.button("Notifications"):
                    # Handle Notifications logic
                    notifications_page(st.session_state.user_id)
                    st.session_state.user_settings_open = not st.session_state.user_settings_open

            col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
            container1 = st.empty()
            container2 = st.empty()

            with col1:
                button1 = st.button('Search a Song')

            with col2:
                button2 = st.button('All Albums')

            with col3:
                button3 = st.button('Create Playlist')
            with col4:
                button4 = st.button('Add Songs')
            with col5:
                button5 = st.button('Play Songs')
            with col6:
                button6 = st.button('Songs by Artist')
            with col7:
                button7 = st.button('Songs by Genre')
            with col8:
                button8 = st.button('Subscriptiom')

            if button1:
                # container1.clear()
                st.session_state.play_song = not st.session_state.play_song
                st.session_state.play_album = False
                st.session_state.create_playlist_open = False
                st.session_state.add_song = False
                st.session_state.play_playlist = False
                st.session_state.song_artist = False
                st.session_state.song_genre = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button2:
                st.session_state.play_song = False
                st.session_state.play_album = not st.session_state.play_album
                st.session_state.create_playlist_open = False
                st.session_state.add_song = False
                st.session_state.play_playlist = False
                st.session_state.song_artist = False
                st.session_state.song_genre = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button3:
                st.session_state.create_playlist_open = not st.session_state.user_settings_open
                st.session_state.play_song = False
                st.session_state.play_album = False
                st.session_state.add_song = False
                st.session_state.play_playlist = False
                st.session_state.song_artist = False
                st.session_state.song_genre = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button4:
                st.session_state.add_song = not st.session_state.add_song
                st.session_state.play_song = False
                st.session_state.play_album = False
                st.session_state.create_playlist_open = False
                st.session_state.play_playlist = False
                st.session_state.song_artist = False
                st.session_state.song_genre = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button5:
                st.session_state.play_playlist = not st.session_state.play_playlist
                st.session_state.play_song = False
                st.session_state.play_album = False
                st.session_state.create_playlist_open = False
                st.session_state.add_song = False
                st.session_state.song_artist = False
                st.session_state.song_genre = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button6:
                st.session_state.song_artist = not st.session_state.song_artist
                st.session_state.play_playlist = False
                st.session_state.play_song = False
                st.session_state.play_album = False
                st.session_state.create_playlist_open = False
                st.session_state.add_song = False
                st.session_state.song_genre = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button7:
                st.session_state.song_genre = not st.session_state.song_genre
                st.session_state.play_playlist = False
                st.session_state.play_song = False
                st.session_state.play_album = False
                st.session_state.create_playlist_open = False
                st.session_state.add_song = False
                st.session_state.song_artist = False
                st.session_state.sub = False
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            if button8:
                st.session_state.song_genre = False
                st.session_state.play_playlist = False
                st.session_state.play_song = False
                st.session_state.play_album = False
                st.session_state.create_playlist_open = False
                st.session_state.add_song = False
                st.session_state.song_artist = False
                st.session_state.sub = not st.session_state.sub
                st.session_state.search = False
                st.session_state["button1"] = False
                st.session_state["button2"] = False
                st.session_state["button3"] = False
                st.session_state["button4"] = False
                st.session_state["button5"] = False

            def render_song_results(results):
                for index, row in enumerate(results):
                    col1, col2 = st.columns([1, 1])
                    with col1:
                        st.image(row[10], caption=row[1], width=200)

                    with col2:
                        st.write(f"**{index + 1}. {row[1]}** by {row[2]}")
                        play_song(row[6])

                        # Use a unique key for each like button
                        like_button_key = f"like_button_{row[0]}_{st.session_state.user_id}"
                        if st.button(f"Like {row[1]}", key=like_button_key):
                            handle_like(row[0], st.session_state.user_id)

            if "button1" not in st.session_state:
                st.session_state["button1"] = False
            if "button12" not in st.session_state:
                st.session_state["button12"] = False

            global temp
            if st.session_state.play_song:
                st.header("Search a Song")
                search_query = st.text_input("Enter the title or artist:")
                temp = search_query
                # button9=st.button("search")
                if st.button("search"):
                    st.session_state["button1"] = not st.session_state["button1"]
            if st.session_state["button1"]:
                results = search_song(temp)
                if results:
                    st.subheader("Search Results")
                    render_song_results(results)

                else:
                    st.info("No results found.")

            # st.session_state.play_song = False
            if "button2" not in st.session_state:
                st.session_state["button2"] = False
            global var1
            if st.session_state.play_album:
                st.session_state.play_song = False
                st.header("All Albums")

                albums = display_all_albums()
                var1 = albums

                if albums:
                    for album in albums:
                        if st.button(album[1]):
                            st.session_state["button2"] = not st.session_state["button2"]
                            # display_all_songs_in_album(album[0])
                else:
                    st.info("No albums found.")
            if (st.session_state["button2"]):
                # display_all_songs_in_album(var1[0])
                # for album in var1:
                display_all_songs_in_album(album[0], st.session_state.user_id)

            # Display buttons when User Settings is clicked

            if st.session_state.create_playlist_open:
                # st.subheader("User Settings")
                st.header("Create Playlist")
                playlist_name = st.text_input("Enter Playlist Name:")
                if st.button("Create playlist"):
                    create_playlist(playlist_name, st.session_state.user_id)

            if st.session_state.add_song:
                playlist_id = st.selectbox(
                    "Select Playlist", get_playlist_names(st.session_state.user_id))
                playlist_id = get_playlist_id_by_name(playlist_id)
                selected_songs = st.multiselect(
                    "Select Songs", get_song_names())

                if st.button("Add Songs to Playlist"):
                    add_songs_to_playlist(playlist_id, selected_songs)
            if "button3" not in st.session_state:
                st.session_state["button3"] = False
            if st.session_state.play_playlist:
                # st.session_state["button3"]=not st.session_state["button3"]
                # if st.session_state["button3"]:
                play_all_songs_page(st.session_state.user_id)
            if "button4" not in st.session_state:
                st.session_state["button4"] = False
            if st.session_state.song_artist:
                # st.session_state["button4"] = not st.session_state["button4"]
                # if st.session_state["button4"]:
                display_songs_by_artist(st.session_state.user_id)
            if "button5" not in st.session_state:
                st.session_state["button5"] = False
            if st.session_state.song_genre:
                # st.session_state["button5"]= not st.session_state["button5"]
                # if st.session_state["button5"]:

                # Display and play songs of the selected genre
                display_songs_by_genre(st.session_state.user_id)

                # Add other User Settings options as needed
            if st.session_state.sub:
                cursor = conn.cursor()
                st.header("User Subscriptions")
                cursor.execute(
                    "SELECT id, planname, enddate FROM subscriptions WHERE UserID = %s", (st.session_state.user_id,))
                subscriptions = cursor.fetchall()
                remaining_days = 0
                plan_name = ""
                # Display user subscriptions
                if subscriptions:
                    st.subheader("Your Subscriptions:")
                    # Calculate when the subscriptions will get over
                    today = date.today()
                    for subscription in subscriptions:
                        subscription_id, plan_name, end_date = subscription
                        remaining_days = (end_date - today).days
                        st.write(f"Subscription ID: {subscription_id}")
                        st.write(f"Plan: {plan_name}")
                        st.write(f"Days Remaining: {remaining_days} days")

                else:
                    st.write("You don't have any active subscriptions.")
                    st.subheader("Buy Subscrption")
                if remaining_days > 0 and (plan_name == 'Gold' or plan_name == 'Silver'):
                    styled_text = f"<p style='font-size: 24px; color: red;'>You already have an active subscrption think before you proceed</p>"
                    st.markdown(styled_text, unsafe_allow_html=True)
                    styled_text = f"<p style='font-size: 24px; color: red;'>You still have {remaining_days} remaining</p>"
                    st.markdown(styled_text, unsafe_allow_html=True)
                selected_option = st.selectbox(
                    "select an option", ['Gold', 'Silver'])
                price = 0
                today = date.today()
                end_date = date.today()
                plan_name = " "
                if selected_option == "Gold":
                    price = 1000
                    plan_name = "Gold"
                    end_date = today + timedelta(days=365)
                if selected_option == "Silver":
                    price = 500
                    plan_name = "Silver"
                    end_date = today + timedelta(days=180)
                styled_text = f"<p style='font-size: 24px; color: red;'>Total cost is {price}</p>"
                st.markdown(styled_text, unsafe_allow_html=True)
                st.image(
                    "../images_music/images/a12.jpeg", caption="pay by scanning this code", width=200)
                today = date.today()
                con = st.button("Confirm Payment")
                if (con):
                    cursor.execute("UPDATE subscriptions SET PlanName = %s, EndDate = %s, StartDate = %s, Price =%s WHERE UserID = %s ", (
                        plan_name, end_date, today, price, st.session_state.user_id))
                    conn.commit()
                    st.session_state.plan_name = plan_name
                    st.success(
                        f"Payment for {plan_name} successful! Enjoy your subscription!")

                cursor.close()
                conn.commit()


if __name__ == "__main__":
    main()

import streamlit as st
import mysql.connector

# Assuming you have the user_id stored in session_state
# current_user_id = st.session_state.user_id

# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@1989",
    database="music"
)

def display_notifications(user_id):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM notifications WHERE user_id = %s ORDER BY timestamp DESC", (user_id,))
    notifications = cursor.fetchall()
    print(notifications)
    if not notifications:
        st.info("No notifications available.")
    else:
        for notification in notifications:
            st.write(f"**Timestamp:** {notification[3]}")
            st.write(f"**Message:** {notification[2]}")
            st.write("---")
    cursor.close()
    conn.commit()

# Page layout
def notifications_page(current_user_id):
    # st.title("Notifications")
    display_notifications(current_user_id)


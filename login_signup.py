import streamlit as st
import mysql.connector
import pandas as pd
from pydub import AudioSegment
from io import BytesIO
from PIL import Image
from datetime import datetime,date,time
import random
import hashlib
import re
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@1989",
    database="music"
)
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
cursor = conn.cursor(buffered=True)
if not is_stored_procedure_exists(cursor, "UpdateUserSubscription"):
        # Execute the stored procedure creation if it doesn't exist
        cursor.execute(stored_procedure)
#making user_id and username none for loggin out 
def logout():
        st.session_state.user_id = None
        st.session_state.username = None
        st.experimental_rerun()

def is_valid_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None
def create_user(username, password, first_name, last_name, email):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    cursor = conn.cursor(buffered=True)
    if is_valid_email(email):
        cursor.execute("""
            INSERT INTO users (id,username, password, firstName, lastName, email, signUpDate, profilePic)
            VALUES (NULL,%s, %s, %s, %s, %s, NOW(), 'assets/images/profile-pics/user.jpg')
        """, (username, hashed_password, first_name, last_name, email))
        conn.commit()
        st.success("User created successfully!")
    else:
        st.error("Invalid email id")

def verify_user(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    result = cursor.fetchone()
    return result

def verify_user(username, password):
    hashed_password = hashlib.md5(password.encode()).hexdigest()
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
    result = cursor.fetchone()
    return result

def verify_admin(username, password):
    cursor = conn.cursor(buffered=True)
    cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()
    return result


def user_has_subscription(user_id, cursor):
    query = "SELECT * FROM subscriptions WHERE userid = %s"
    cursor.execute(query, (user_id,))
    return cursor.fetchone() is not None
def add_subscription(user_id, planname, price, startdate, enddate, cursor, connection):
    query = "INSERT INTO subscriptions (userid, planname, price, startdate, enddate) VALUES (%s, %s, %s, %s, %s)"
    data = (user_id, planname, price, startdate, enddate)
    cursor.execute(query, data)
    connection.commit()

def get_user_plan_name(user_id, cursor):
    query = "SELECT planname FROM subscriptions WHERE userid = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    return result[0] 
def check_user_credentials(username, email):
    
    cursor = conn.cursor(buffered=True)

    # Execute a query to check if the credentials match
    query = "SELECT * FROM users WHERE username = %s AND email = %s"
    cursor.execute(query, (username, email))

    # Fetch the result
    result = cursor.fetchone()

    # Close the cursor and connection
    cursor.close()
    return result
def update_password_in_database(user_id, new_password):
    cursor=conn.cursor(buffered=True)
    update_query = "UPDATE users SET password = %s WHERE id = %s"
    cursor.execute(update_query, (new_password, user_id))
    conn.commit()
    cursor.close()

def forgot_password():
    st.title("Forgot Password")
    username = st.text_input("Username:")
    email = st.text_input("Email")
    new_password = st.text_input("Enter new password:", type="password")
    confirm_password = st.text_input("Confirm new password:", type="password")
    submit=st.button('Change Password')

    if submit:
        user_data = check_user_credentials(username, email)
        if user_data:
            if new_password == confirm_password:
                hashed_password = hashlib.md5(new_password.encode()).hexdigest()
                update_password_in_database(user_data[0], hashed_password)
                st.success("Password updated successfully!")
            else:
                st.error("Passwords do not match. Please try again.")
        else:
            st.error("Invalid username or email. Please check your credentials.")


    

def login_page():
    st.title("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    if st.button("Login"):
        
        user = verify_user(username, password)
        if user:
            st.success(f"Welcome, {username}!")
            st.session_state.user_id = user[0]
            st.session_state.username = username
            user_id = user[0]
            cursor = conn.cursor(buffered=True)
            if not user_has_subscription(st.session_state.user_id, cursor):
                today=date.today()
                add_subscription(st.session_state.user_id, "FREE", 0.00, today, "2030-12-31", cursor, conn)
            user_plan_name = get_user_plan_name(st.session_state.user_id, cursor)
            st.session_state.plan_name = user_plan_name
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")
def admin_login_page():
    st.title("Login")
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")
    if st.button("Login"):
        
        user = verify_admin(username, password)
        if user:
            st.success(f"Welcome, {username}!")
            st.session_state.user_id = user[0]
            st.session_state.username = username
            user_id = user[0]
            st.experimental_rerun()
        else:
            st.error("Invalid username or password")

def signup_page():
    st.title("Signup")
    new_username = st.text_input("New Username:")
    new_password = st.text_input("New Password:", type="password")
    first_name = st.text_input("First Name:")
    last_name = st.text_input("Last Name:")
    email = st.text_input("Email:")
    if st.button("Create Account"):
        create_user(new_username, new_password, first_name, last_name, email)
        # login_page()

    # Increment ad clicks
    cursor = conn.cursor(buffered=True)
    cursor.execute(f"UPDATE Advertisements SET ad_clicks = ad_clicks + 1 WHERE ad_id = {ad['ad_id']}")
    conn.commit()

    
def delete_user_and_entries(user_id):
    cursor = conn.cursor(buffered=True)
    cursor.execute("DELETE FROM subscriptions WHERE userid = %s", (user_id,))
    # Delete songs from playlists
    cursor.execute("DELETE FROM playlistssongs WHERE playlistId IN (SELECT id FROM playlists WHERE owner = %s)", (user_id,))
    # Delete playlists
    cursor.execute("DELETE FROM playlists WHERE owner = %s", (user_id,))
    # Delete user
    cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
    conn.commit()
    st.success("Account deleted successfully!")
    st.session_state.user_id = None
    st.session_state.username = None

    # Redirect to login/signup pages
    st.experimental_rerun()
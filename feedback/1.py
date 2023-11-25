import streamlit as st
import mysql.connector

# Streamlit app
def main():
    # Page title
    st.title("Feedback Form")

    # Collect user input for feedback
    user_name = st.text_input("Your Name:")
    email = st.text_input("Your Email:")
    feedback_text = st.text_area("Feedback:")

    # Button to submit feedback
    if st.button("Submit Feedback"):
        if user_name and feedback_text:
            try:
                # Connect to the MySQL database
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="Shreya@1989",
                    database="demo"
                )

                # Create a MySQL cursor
                cursor = conn.cursor()

                # Call the stored procedure
                cursor.callproc("insert_feedback_proc", (user_name, email, feedback_text))

                # Commit and close the connection
                conn.commit()
                conn.close()

                st.success("Feedback submitted successfully!")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
        else:
            st.warning("Please enter your name and feedback before submitting.")

if __name__ == '__main__':
    main()

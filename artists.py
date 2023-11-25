import streamlit as st
import mysql.connector
import pandas as pd
from pydub import AudioSegment
from io import BytesIO
from PIL import Image
from datetime import datetime
import random
import hashlib


# MySQL connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="music"
)
def get_unique_artists():
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT name FROM artists")
    artists = cursor.fetchall()
    return [artist[0] for artist in artists]
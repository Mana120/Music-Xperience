import mysql.connector

from admin_operations import *
import streamlit as st
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shreya@1989",
    database="music"
)
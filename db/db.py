

"""
This file will manage interactions with our data store.
At first, it will just contain stubs that return fake data.
Gradually, we will fill in actual calls to our datastore.
"""

import json
import psycopg2
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
import os

load_dotenv()

ROOMS_DB = "/home/anna/website_project/myBackend/db/db/rooms.json"

DB_ENV = os.getenv("DB_ENV", "local") #deafults to local if not set
# Fetch variables
USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT", "5432")
DBNAME = os.getenv("DB_NAME")
DATABASE_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    """
    Establishes and returns a connection to the PostgreSQL database.
    """
    if DB_ENV == "remote":
        conn = psycopg2.connect(DATABASE_URL)
    else:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
    return conn

def create_user(username, password, email):
    """
    Creates a new user in the database with a hashed password.
    """
    hashed_password = generate_password_hash(password)
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username, password, email) VALUES (%s, %s, %s) RETURNING id",
        (username, hashed_password, email)
    )
    user_id = cursor.fetchone()[0]
    conn.commit()
    cursor.close()
    conn.close()
    return user_id

def get_rooms():
    try:
        with open(ROOMS_DB) as file:
            return json.loads(file.read())
    except FileNotFoundError:
        return None


def fetch_pets():
    """
    A function to return all pets in the data store.
    """
    return {"tigers": 2, "lions": 3, "zebras": 1}
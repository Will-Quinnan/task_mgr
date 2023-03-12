from flask import g
import sqlite3

DATABASE_URL = "main.db"

def get_db():
    db = getattr(g, "_databse", None)
    if not db:
        db = g.database = sqlite3.connect(DATABASE_URL)
    return db

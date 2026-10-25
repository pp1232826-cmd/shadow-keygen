import os
import sqlite3

DB_PATH = os.environ.get("DB_PATH", "licenses.db")

def connect():
    db = sqlite3.connect(DB_PATH, timeout=10)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with connect() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS licenses (
                key TEXT PRIMARY KEY,
                status TEXT NOT NULL DEFAULT 'active',
                expires_at TEXT,
                device_id TEXT
            )
        """)
        db.commit()

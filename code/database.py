# database.py
import sqlite3

def init_db():
    conn = sqlite3.connect("sweeps.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS bonuses (
            site TEXT PRIMARY KEY,
            last_claimed TEXT,
            balance REAL,
            threshold REAL,
            status TEXT
        )
    ''')
    conn.commit()
    conn.close()

def fetch_all_bonuses():
    conn = sqlite3.connect("sweeps.db")
    c = conn.cursor()
    c.execute("SELECT site, last_claimed, balance, threshold, status FROM bonuses")
    rows = c.fetchall()
    conn.close()
    return rows

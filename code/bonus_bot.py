# bonus_bot.py
import sqlite3
from datetime import datetime

def claim_site_bonus(site):
    print(f"Claiming bonus for {site}...")
    return {
        "site": site,
        "last_claimed": datetime.now().isoformat(timespec='seconds'),
        "balance": 10.0,
        "threshold": 5.0,
        "status": "Claimed"
    }

def claim_daily_bonus():
    sites = ["Stake", "Pulsz", "Wow Vegas", "High 5"]
    conn = sqlite3.connect("sweeps.db")
    c = conn.cursor()

    for site in sites:
        data = claim_site_bonus(site)
        c.execute('''
            INSERT INTO bonuses (site, last_claimed, balance, threshold, status)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(site) DO UPDATE SET
                last_claimed=excluded.last_claimed,
                balance=excluded.balance,
                threshold=excluded.threshold,
                status=excluded.status
        ''', (data['site'], data['last_claimed'], data['balance'], data['threshold'], data['status']))

    conn.commit()
    conn.close()

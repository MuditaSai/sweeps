# app.py
import streamlit as st
from database import init_db, fetch_all_bonuses
from bonus_bot import claim_daily_bonus

st.set_page_config(page_title="Sweeps Dashboard", layout="wide")

st.title("🎁 Sweeps Daily Bonus Dashboard")

# Initialize DB
init_db()

if st.button("Claim Bonuses"):
    claim_daily_bonus()
    st.success("Bonuses claimed!")

data = fetch_all_bonuses()

st.subheader("Current Bonus Status")
st.table(
    {
        "Site": [row[0] for row in data],
        "Last Claimed": [row[1] for row in data],
        "Balance": [row[2] for row in data],
        "Threshold": [row[3] for row in data],
        "Status": [row[4] for row in data],
    }
)

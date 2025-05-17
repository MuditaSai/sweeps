# sweeps
automation to keep track of and collect daily sign on bonuses from sweepstakes / social casinos

# Feeatures
1. Tabular layout
    - Site
    - Timer
    - Balance / Threshold
    - Status
2. Going on discord channels and collecting freebies via discord bot (key word detection)

# Tech stack
# Sweeps Automation Dashboard - Tech Stack

| Layer      | Technology                 | Description                                          |
|------------|---------------------------|------------------------------------------------------|
| Frontend   | Streamlit                 | Python-based, simple web app framework for dashboards |
| Backend    | Python (Flask optional)   | Logic for automation and API (optional, currently using Streamlit) |
| Automation | Playwright (or custom)    | Browser automation for claiming bonuses              |
| Database   | SQLite                    | Lightweight local database to store bonus info       |
| Scheduler  | (Optional) APScheduler    | For running periodic automation tasks (if needed)   |
| Discord    | discord.py / nextcord     | To collect freebies from Discord channels            |
| Deployment | Streamlit Cloud / Vercel  | Hosting the dashboard and backend                     |

# Libraries
discord.py (https://discordpy.readthedocs.io/en/stable/)
playwright
flask

# Frontend setup

npm create vite@latest frontend --template react
cd frontend
npm install
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

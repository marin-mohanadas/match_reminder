# 🏏 WhatsApp Match Reminder App

Automatically scrapes cricket match schedules and sends WhatsApp reminders via Twilio every Wednesday at noon (EST).

---

# 📋 Purpose

- This app scrapes a cricket team's match schedule from a public website and sends **WhatsApp reminders** for upcoming **Saturday** and **Sunday** matches.  
- It ensures that players (or groups) are notified **every Wednesday at 12:00 PM EST**, keeping everyone informed without manual effort.

---

# ⚙️ How It Works

1. **Schedule Scraping (`scrape_schedule.py`)**
   - Runs every Wednesday at 11:55 AM EST.
   - Scrapes the latest match schedule from the website.
   - Filters:
     - Skips old matches (past dates).
     - Correctly identifies opponents (excluding Gladiators).
     - Cleans venue names.
   - Saves the result into `schedule_tasks.json`.

2. **WhatsApp Notifications (`send_reminders.py`)**
   - Runs every Wednesday at 12:00 PM EST.
   - Reads from `schedule_tasks.json`.
   - Finds upcoming matches on Saturday or Sunday.
   - Sends formatted WhatsApp messages using Twilio's API.

---

# 🛡 Security

| Security Measure | Description |
|:---|:---|
| Secrets Hidden | Twilio SID, Auth Token, and Phone Numbers are **hidden** via GitHub Secrets and local `.env` files. |
| .gitignore | `.env` is excluded from version control to prevent leaks. |
| GitHub Actions | Secrets injected automatically during deployment. |

---

# 🛠 Technology Stack

| Component | Technology |
|:---|:---|
| Language | Python 3.x |
| Web Scraping | BeautifulSoup4 |
| Messaging | Twilio WhatsApp API |
| Scheduling | GitHub Actions (cron jobs) |
| Secrets Management | GitHub Secrets & `.env` |

---

# 📅 Deployment Timing

| Task | EST Local Time | GitHub Actions Cron (UTC) |
|:---|:---|:---|
| Scrape Schedule | Wednesday 11:55 AM | `'55 16 * * 3'` |
| Send WhatsApp Reminder | Wednesday 12:00 PM | `'0 17 * * 3'` |

---

# 🚀 Bonus Features
- Automatically cleans past matches every week.
- Highly customizable for new message formats (emojis, player names, etc.).
- Fast, serverless operation with no extra hosting costs.
- Fully free-tier compatible using GitHub + Twilio sandbox!

---

# ✅ Status: Production-Ready!
- Fully automated and serverless — no manual hosting or servers needed.

---

# 📈 Future Improvements (Optional)
- Add Slack notifications for successful deployments.
- Log sent messages into a logs/ folder.
- Allow multiple teams/leagues support.

---

# 🎉 Thanks for using WhatsApp Match Reminder App!


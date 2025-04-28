import json
import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# Load secrets
ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
FROM_NUMBER = os.environ["TWILIO_FROM_NUMBER"]
TO_NUMBER = os.environ["TWILIO_TO_NUMBER"]

# Load match schedule
with open('schedule_tasks.json') as f:
    schedule = json.load(f)

# Init Twilio
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_whatsapp_reminders():
    today = datetime.now().date()

    for match in schedule:
        match_date = datetime.strptime(match['date'], "%m/%d/%Y")
        day_of_week = match_date.strftime("%A")
        days_since_wednesday = (match_date.weekday() - 2) % 7
        previous_wednesday = match_date - timedelta(days=days_since_wednesday)

        # Send reminder Wednesday before the match day
        if today == previous_wednesday.date():
            message_body = (
                f"🏏 Match Reminder: Match #{match['match_no']} vs {match['opponent']}\n"
                f"📅 Date: {day_of_week}({match_date.strftime("%m/%d")}) at {match['time']}\n"
                f"📍 Venue: {match['venue']}\n\n"
                f"Please poll your availability:\n"
            )

            message = client.messages.create(
                from_=FROM_NUMBER,
                to=TO_NUMBER,
                body=message_body
            )

            print(f"Message sent: {message.sid}")


# Run it
if __name__ == "__main__":
    send_whatsapp_reminders()

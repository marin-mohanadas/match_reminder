import json
import os
from datetime import datetime, timedelta

from twilio.rest import Client

from config import get_twilio_sid, get_twilio_token, get_twilio_from, get_twilio_to

ACCOUNT_SID = get_twilio_sid()
AUTH_TOKEN = get_twilio_token()
FROM_NUMBER = get_twilio_from()
TO_NUMBER = get_twilio_to()

if not all([ACCOUNT_SID, AUTH_TOKEN, FROM_NUMBER, TO_NUMBER]):
    raise Exception("Twilio credentials missing")

# Load match schedule. Use absolute path
script_dir = os.path.dirname(os.path.abspath(__file__))
schedule_file = os.path.join(script_dir, "schedule_tasks.json")
with open(schedule_file) as f:
    schedule = json.load(f)

# Init Twilio
client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_whatsapp_reminders():
    today = datetime.now().date()

    if not schedule:
        print("No upcoming matches found.")
        return

    for match in schedule:
        match_date = datetime.strptime(match['date'], "%m/%d/%Y")
        day_of_week = match_date.strftime("%A")
        days_to_previous_wednesday = (match_date.weekday() - 2) % 7
        previous_wednesday = match_date - timedelta(days=days_to_previous_wednesday)

        # Send reminder Wednesday before the match day
        if today == previous_wednesday.date():
            message_body = (
                f"🏏 Match Reminder: Match #{match['match_no']} vs {match['opponent']}\n"
                f"📅 Date: {day_of_week}({match_date.strftime('%m/%d')}) at {match['time']}\n"
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

import os

from dotenv import load_dotenv

# Load environment variables once
load_dotenv()

# Scraper settings
URL = os.environ["URL"]
TEAM_NAME = os.environ["TEAM_NAME"]

# Twilio credentials
TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_FROM_NUMBER = os.environ["TWILIO_FROM_NUMBER"]
TWILIO_TO_NUMBER = os.environ["TWILIO_TO_NUMBER"]

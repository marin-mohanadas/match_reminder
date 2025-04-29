import os
from dotenv import load_dotenv

load_dotenv()


# Scraper settings
def get_url():
    return os.getenv("URL")


def get_team_name():
    return os.getenv("TEAM_NAME")


# Twilio credentials
def get_twilio_sid():
    return os.getenv("TWILIO_SID")


def get_twilio_token():
    return os.getenv("TWILIO_AUTH_TOKEN")


def get_twilio_from():
    return os.getenv("TWILIO_FROM_NUMBER")


def get_twilio_to():
    return os.getenv("TWILIO_TO_NUMBER")

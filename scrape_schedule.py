import json
import os
import re

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Load secrets
URL = os.environ["URL"]
TEAM_NAME = os.environ["TEAM_NAME"]


def fetch_schedule(url, team_name):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch page")

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')  # You might need to adjust this selector
    rows = table.find_all('tr')[1:]  # Skip the header

    tasks = []

    for row in rows:
        cols = [col.get_text(strip=True) for col in row.find_all('td')]
        if not cols or len(cols) < 5:
            continue

        task = {
            "match_no": cols[0],
            "date": cols[2],
            "time": cols[3],
            "venue": re.sub(r'[()]', '', cols[6]).strip(),
            "opponent": cols[4] if cols[4] != team_name else cols[5]
        }
        tasks.append(task)

    return tasks


if __name__ == "__main__":
    schedule_tasks = fetch_schedule(URL, TEAM_NAME)

    with open('schedule_tasks.json', 'w') as f:
        json.dump(schedule_tasks, f, indent=2)
    print("Tasks saved to schedule_tasks.json")

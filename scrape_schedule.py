import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

import config

URL = config.URL
TEAM_NAME = config.TEAM_NAME


def fetch_schedule(url, team_name):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='table')
    if table is None:
        raise Exception("Could not find schedule table on page")

    rows = table.find_all('tr')[1:]  # Skip the header
    tasks = []

    for row in rows:
        cols = [col.get_text(strip=True) for col in row.find_all('td')]
        if not cols or len(cols) < 7:
            continue

        try:
            match_date = datetime.strptime(cols[2], "%m/%d/%Y").date()
        except ValueError:
            continue

        # Skip past matches
        if match_date < datetime.today().date():
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

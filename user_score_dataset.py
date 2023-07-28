# Integrating both formatting in one code

import csv
import requests
from bs4 import BeautifulSoup
import json
import time
import random

def scrape_user_profile(username, user_id, status_code):
    url = f"https://myanimelist.net/animelist/{username}?status={status_code}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        table_1 = soup.find("table", {"data-items": True})
        table_2 = soup.find_all("table", {"border": "0", "cellpadding": "0", "cellspacing": "0", "width": "100%"})

        if table_1:
            data_items = table_1["data-items"]
            try:
                data_items_parsed = json.loads(data_items)
            except json.JSONDecodeError:
                return None

            data = []
            for data_item in data_items_parsed:
                anime_id = data_item["anime_id"]
                title = data_item["anime_title"]
                score = data_item["score"]
                if score != 0:
                    data.append([user_id, username, anime_id, title, score])

            return data

        elif table_2:
            data = []

            for table in table_2:
                row = table.find("tr")

                if row:
                    cells = row.find_all("td")

                    if len(cells) >= 5:
                        anime_title_cell = cells[1]
                        score_cell = cells[2]

                        anime_title_link = anime_title_cell.find("a", class_="animetitle")
                        anime_id = anime_title_link["href"].split("/")[2] if anime_title_link else ""
                        anime_title = anime_title_link.find("span").text.strip() if anime_title_link else ""

                        score_label = score_cell.find("span", class_="score-label")
                        score = score_label.text.strip() if score_label else "-"

                        if anime_title and score != "-":
                            data.append([user_id, username, anime_id, anime_title, score])

            return data

    return None


def fetch_user_scores():
    with open('userlist/userlist.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        usernames = [row['username'] for row in rows]
        user_ids = [row['user_id'] for row in rows]

    user_scores = []
    status_code = 7
    batch_size = 50  # Number of usernames to fetch in each batch
    min_delay_seconds = 90  # Minimum delay duration between requests in seconds
    max_delay_seconds = 120  # Maximum delay duration between requests in seconds

    with open('user_score.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["User ID", "Username", "Anime ID", "Anime Title", "Score"])  # Write column names

        for i in range(0, len(usernames), batch_size):
            usernames_batch = usernames[i:i + batch_size]
            user_ids_batch = user_ids[i:i + batch_size]

            for username, user_id in zip(usernames_batch, user_ids_batch):
                data = scrape_user_profile(username, user_id, status_code)
                if data:
                    user_scores.extend(data)
                    print(f"User details fetched successfully for username: {username}")
                    writer.writerows(data)
                else:
                    print(f"No user details found for username: {username}")

            if i + batch_size < len(usernames):
                # Add random delay between requests
                delay_seconds = random.randint(min_delay_seconds, max_delay_seconds)
                time.sleep(delay_seconds)
                print(f"Waiting for {delay_seconds} seconds before the next batch...")
                time.sleep(delay_seconds)

    if user_scores:
        print("All user details fetched successfully.")
    else:
        print("No user details found.")

fetch_user_scores()
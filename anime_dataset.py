import csv
import re
import requests
import json

output_file = 'anime_dataset.csv'

start_id = 1  # Starting anime ID
end_id = 100  # Ending anime ID

count = 0  # keep count of anime for the current session
animes = []  # list to store anime data

anime_id = start_id

while anime_id <= end_id:
    apiUrl = 'https://api.jikan.moe/v4/anime/' + str(anime_id)  # base url for API

    # API call
    page = requests.get(apiUrl)

    # I will do 5 retries
    tries = 0
    while tries < 5 and page.status_code != 200:
        tries += 1
        page = requests.get(apiUrl)

    # if status code is 200 then process the response
    if page.status_code == 200:
        jsonData = page.json()

        # Check if 'data' key is present in the response
        if 'data' in jsonData:
            anime = {}

            # Fetching animeID
            anime['animeID'] = anime_id

            # Fetching Name of the anime
            anime['Name'] = jsonData['data'].get('title')

            # Fetching english title of the anime
            anime['English name'] = jsonData['data'].get('title_english')

            # Fetching japanese title of the anime
            anime['Japanese name'] = jsonData['data'].get('title_japanese')

            # Fetching Score of the anime
            anime['Score'] = jsonData['data'].get('score')

            # Fetching Genres of the anime
            anime['Genres'] = ', '.join([genre['name'] for genre in jsonData['data'].get('genres', [])])

            # Fetching and cleaning the Synopsis of the anime
            synopsis = jsonData['data'].get('synopsis')
            if synopsis is not None:
                cleaned_synopsis = re.sub(r'\[.*?\]', '', synopsis).strip()
                anime['Synopsis'] = cleaned_synopsis
            else:
                anime['Synopsis'] = ""

            # Fetching Type of the anime
            anime['Type'] = jsonData['data'].get('type')

            # Fetching Episodes of the anime
            anime['Episodes'] = jsonData['data'].get('episodes')

            # Fetching Aired dates of the anime
            anime['Aired'] = jsonData['data'].get('aired', {}).get('string')

            # Fetching season and year and then combining them in the Premiered column
            premiered = jsonData['data'].get('season')
            year = jsonData['data'].get('year')
            if year is not None:
                premiered += ' ' + str(year)
            anime['Premiered'] = premiered

            # Fetching Status dates of the anime
            anime['Status'] = jsonData['data'].get('status')

            # Fetching Producers of the anime
            anime['Producers'] = ', '.join([producer['name'] for producer in jsonData['data'].get('producers', [])])

            # Fetching Licensors of the anime
            anime['Licensors'] = ', '.join([license['name'] for license in jsonData['data'].get('licensors', [])])

            # Fetching Studios of the anime
            anime['Studios'] = ', '.join([studio['name'] for studio in jsonData['data'].get('studios', [])])

            # Fetching Source of the anime
            anime['Source'] = jsonData['data'].get('source')

            # Fetching Duration of the anime
            anime['Duration'] = jsonData['data'].get('duration')

            # Fetching Rating of the anime
            anime['Rating'] = jsonData['data'].get('rating')

            # Fetching Rank of the anime
            anime['Rank'] = jsonData['data'].get('rank')

            # Fetching Popularity of the anime
            anime['Popularity'] = jsonData['data'].get('popularity')

            # Fetching Favorites of the anime
            anime['Favorites'] = jsonData['data'].get('favorites')

            # Fetching Scored By of the anime
            anime['Scored By'] = jsonData['data'].get('scored_by')

            # Fetching Members of the anime
            anime['Members'] = jsonData['data'].get('members')

            animes.append(anime)

            count += 1

            # Writing the dataset to a CSV file after processing each anime
            if count % 200 == 0:
                print('{} anime processed, writing to file'.format(count))
                if animes:
                    fieldnames = list(animes[0].keys())  # Get the fieldnames from the first anime
                    mode = 'a' if count > 0 else 'w'  # Choose the mode based on the count
                    with open(output_file, mode, newline='', encoding='utf-8') as csvfile:
                        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                        if count == 200:  # Write the header row only for the first batch
                            writer.writeheader()
                        writer.writerows(animes)
                    animes.clear()

        else:
            print('Skipping anime {}: Invalid data'.format(anime_id))

    anime_id += 1

# Writing the remaining dataset to a CSV file
if animes:
    print('Writing the final dataset to a CSV file')
    fieldnames = list(animes[0].keys())  # Get the fieldnames from the first anime
    with open(output_file, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerows(animes)

print('Total', count, 'anime data fetched. Done.')
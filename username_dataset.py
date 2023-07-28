import csv
import requests
import json

output_file = 'userlist/userlist.csv'

start_id = 1  # Starting user ID
end_id = 10  # Ending user ID

count = 0  # keep count of users for the current session
users = []  # list to store user data

for user_id in range(start_id, end_id + 1):
    apiUrl = f'https://api.jikan.moe/v4/users/userbyid/{user_id}'

    # API call with retries
    tries = 0
    while tries < 5:
        response = requests.get(apiUrl)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            break  # Successful response, exit the retry loop

        tries += 1

    # Check if the request was successful after retries
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        # Check if the 'data' field exists in the response
        if 'data' in data:
            # Extract the user details
            user_url = data['data']['url']
            username = data['data']['username']

            # Create a dictionary for the user
            user = {
                'user_id': user_id,
                'username': username,
                'user_url': user_url
            }

            # Append the user dictionary to the list
            users.append(user)
            count += 1

        else:
            print(f'No user data found for ID: {user_id}')
    # else:
    #     print(f'Error occurred while fetching user data for ID: {user_id}')

# Save the user details in a CSV file
if users:
    fieldnames = list(users[0].keys())  # Get the fieldnames from the first user
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)

print('Total', count, 'user data fetched. Done.')
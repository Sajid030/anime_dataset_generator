import requests
import csv
import time

# Read usernames from CSV file
usernames = []
with open("userlist.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        usernames.append(row["username"])

# Prepare headers for the user_details.csv file
headers = [
    "Mal ID", "Username", "Gender", "Birthday", "Location", "Joined",
    "Days Watched", "Mean Score", "Watching",
    "Completed", "On Hold", "Dropped",
    "Plan to Watch", "Total Entries", "Rewatched",
    "Episodes Watched"
]

# Create a list to store user details
user_details = []

# Initialize counter and timer variables
total_usernames = len(usernames)
fetch_count = 0
total = 0
start_time = time.time()

# Set batch size and delay between batches
batch_size = 3
batch_delay = 1.0  # Delay in seconds between batches

# Set maximum runtime to 11 hours (in seconds)
max_runtime = 2 * 60

# Iterate over usernames in batches
for i in range(0, total_usernames, batch_size):
    batch_usernames = usernames[i:i+batch_size]

    batch_user_details = []

    # Fetch user details for each username in the batch
    for username in batch_usernames:
        url = f"https://api.jikan.moe/v4/users/{username}/full"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            user_data = data.get("data", {})

            mal_id = user_data.get("mal_id")
            username = user_data.get("username")
            gender = user_data.get("gender")
            birthday = user_data.get("birthday")
            location = user_data.get("location")
            joined = user_data.get("joined")

            anime_statistics = user_data.get("statistics", {}).get("anime", {})
            days_watched = anime_statistics.get("days_watched")
            mean_score_anime = anime_statistics.get("mean_score")
            watching = anime_statistics.get("watching")
            completed_anime = anime_statistics.get("completed")
            on_hold = anime_statistics.get("on_hold")
            dropped = anime_statistics.get("dropped")
            plan_to_watch = anime_statistics.get("plan_to_watch")
            total_entries_anime = anime_statistics.get("total_entries")
            rewatched = anime_statistics.get("rewatched")
            episodes_watched = anime_statistics.get("episodes_watched")

            batch_user_details.append([
                mal_id, username, gender, birthday, location, joined,
                days_watched, mean_score_anime, watching,
                completed_anime, on_hold, dropped,
                plan_to_watch, total_entries_anime, rewatched,
                episodes_watched
            ])

            fetch_count += 1
            total += 1
            time.sleep(0.35)

        else:
            print(f"Error occurred while fetching 'full' data for username: {username}")
            print(f"HTTP Error {response.status_code}: {response.reason}")
            print(f"Error message: {response.text}")

    # Add batch user details to the main user details list
    user_details.extend(batch_user_details)

    # Calculate and display progress
    if fetch_count >= 1000:
        progress = (i + len(batch_usernames)) / total_usernames * 100
        print(f"Progress: {progress:.2f}%")
        fetch_count = 0

    # Wait for the batch delay
    time.sleep(batch_delay)

    # Check elapsed time and exit loop if exceeding maximum runtime
    elapsed_time = time.time() - start_time
    if elapsed_time > max_runtime:
        print("Maximum runtime exceeded. Stopping the process.")
        break

# Calculate elapsed time and usernames fetched per second
elapsed_time = time.time() - start_time
usernames_per_second = total / elapsed_time

# Save user details to a csv file
with open("user_details.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(user_details)

print("User details saved to user_details.csv.")
print(f"Fetched {total} usernames in {elapsed_time:.2f} seconds.")
print(f"Average usernames fetched per second: {usernames_per_second:.2f}")
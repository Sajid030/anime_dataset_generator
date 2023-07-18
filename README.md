# Anime Dataset Generator

This project aims to generate an anime dataset by utilizing the Jikan API. It retrieves information about anime such as title, score, genres, synopsis, producers, studios, and more. Additionally, it includes functionality to generate a list of usernames from MyAnimeList and fetch user details and anime scores for those usernames.

## Prerequisites

- Python 3.7 or higher
- requests library
- csv library
- re library
- json library
- BeautifulSoup library

## Usage

1. Clone the repository:

   ```
   git clone https://github.com/your-username/anime-dataset-generator.git
   ```
2. Install the required dependencies:
   
   ```
   pip install requests beautifulsoup4 
   ```
3. Run the 4 python files:
   
   There are total 4 python files and their functions are:-

   ## Anime Details Generator

     This Python script `anime_dataset.py` allows you to generate an anime dataset by utilizing the Jikan API. It fetches anime information such as title, score, 
     genres, synopsis, producers, studios, and more. The data is then stored in a CSV file `anime_dataset.csv` for further analysis and use.

     #### How it Works:-

     1. Specify the range of anime IDs you want to retrieve by setting the `start_id` and `end_id` variables.
     2. The script makes API calls to retrieve data for each anime ID.
     3. It processes the API responses, extracting relevant information such as anime titles, scores, genres, and more.
     4. The fetched data is cleaned and stored in a list of dictionaries, where each dictionary represents an anime entry.
     5. After processing a certain number of anime entries (controlled by the `count` variable), the data is written to the output CSV file.
     6. Finally, the script prints the total number of anime data fetched.

     The generated anime dataset (anime_dataset.csv) will contain the following columns:
     - `animeID`: Unique identifier for each anime
     - `Name`: Name of the anime
     - `English name`: English name of the anime
     - `Japanese name`: Japanese name of the anime
     - `Score`: Score of the anime
     - `Genres`: Genres of the anime
     - `Synopsis`: Synopsis of the anime
     - `Type`: Type of the anime
     - `Episodes`: Number of episodes
     - `Aired`: Airing dates of the anime
     - `Premiered`: Premiered season and year
     - `Status`: Current status of the anime
     - `Producers`: Producers of the anime
     - `Licensors`: Licensors of the anime
     - `Studios`: Studios of the anime
     - `Source`: Source material of the anime
     - `Duration`: Duration of each episode
     - `Rating`: Age rating of the anime
     - `Rank`: Rank of the anime
     - `Popularity`: Popularity ranking of the anime
     - `Favorites`: Number of users who favorited the anime
     - `Scored By`: Number of users who scored the anime
     - `Members`: Number of members in the anime's community

     Run the script to generate the anime list:
      ```
      python anime_dataset.py
      ```
     
   ## User List Generator

     This Python script `username_dataset.py` allows you to generate a list of users by utilizing the Jikan API. It retrieves user information such as username and 
     user URL for a specified range of user IDs. The user details are then stored in a CSV file `userlist.csv` for further analysis and use.

      #### How it Works:-

      1. Specify the range of user IDs you want to retrieve by setting the `start_id` and `end_id` variables.
      2. The script makes API calls to retrieve user data for each user ID.
      3. It checks the response status code and retries the API call up to 5 times if it fails.
      4. If the response is successful (status code 200), the script parses the JSON response and extracts the user details such as username and user URL.
      5. The user details are stored as dictionaries in a list.
      6. After processing all the user IDs in the specified range, the user details are written to the output CSV file.
      7. Finally, the script prints the total number of user data fetched.

      Run the script to generate the User list:
      ```
      python username_dataset.py
      ```

   ## User Scores Fetcher

      This Python script `user_scores_dataset.py` integrates the user list generated from the userlist.py script with the anime scoring data fetched from MyAnimeList.       It retrieves the anime scores for each user in the user list and stores the data in a CSV file `user_score.csv` for further analysis and use.

      #### How it Works:-

      1. The script reads the user list from the `userlist.csv` file, which should be generated using the `username_dataset.py` script.
      2. It iterates through the user list and calls the `scrape_user_profile()` function to fetch the anime scores for each user.
      3. The `scrape_user_profile()` function performs web scraping on the respective user's anime list page to extract the anime scores.
      4. It uses the BeautifulSoup library to parse the HTML response and extract relevant data.
      5. The function handles two different HTML structures found on differnet users animelist page to retrieve the anime scores.
      6. For each user, the fetched anime scores are stored in a list of lists, where each inner list contains the user ID, username, anime ID, anime title, and score.
      7. The script writes the fetched anime scores to the `user_score.csv` file, including column names.
      8. To prevent overwhelming the MyAnimeList servers, the script implements a delay between batches of user requests, randomly chosen within a specified range of           seconds.
      9. After processing all the users in the user list, the script prints a success message if anime scores were fetched successfully, or a failure message if no             scores were found.
   
      `NOTE` :- There are some users who have chose to hide their list so score list of those users can't be fetched for obvious reason.
      Also I was trying to fetch the score list using `jikan`. Using jikan v4 we can now fetch each user's anime scores . However, the issue with the Jikan API was          that it only fetched scores for users who had rated a limited number of anime (usually 4-5), skipping users who had rated more than that. Maybe they can resolve 
      the issue in future so you can also use jikan to do the same.

      Run the script to generate the User-Score list:
      ```
      python user_score_dataset.py
      ```

   ## User Details Fetcher
   
      This Python script `user_details_dataset.py` fetches detailed information for a list of usernames from MyAnimeList using the Jikan API. It retrieves user- 
      specific data such as gender, birthday, location, join date, anime statistics, and more. The fetched user details are then stored in a CSV file                
      `user_details.csv` for further analysis and use.

      #### How it Works:-
The script reads a list of usernames from the userlist.csv file, which should be generated using the userlist.py script.

It prepares the headers for the user_details.csv file, specifying the columns for each user detail.

The script initializes variables to keep track of the progress, fetch count, and total usernames.

It sets the batch size and delay between batches to manage the API requests and prevent overwhelming the servers.

The script iterates over the list of usernames in batches.

For each batch, it sends API requests to fetch the detailed user information using the Jikan API.

If the API response is successful (status code 200), the script extracts the relevant user details from the JSON response.

The fetched user details are stored in a list of lists, where each inner list contains the user details in the specified order.

The script tracks the fetch count and total usernames processed, displaying the progress periodically.

It also incorporates a batch delay to introduce a pause between batches to comply with API usage guidelines.

The script calculates the elapsed time and usernames fetched per second to provide performance metrics.

Finally, it saves the user details to the user_details.csv file, including the headers and the fetched user data.


   

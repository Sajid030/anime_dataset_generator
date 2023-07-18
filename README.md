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
   
   There are total 4 python files and they are:-

   ## - anime_dataset.py
     
     The script will fetch anime data and save it in a CSV file specified by the output_file variable.

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

     Modify the following variables in the anime_dataset.py file according to your preferences:
     - `start_id`: Starting anime ID
     - `end_id`: Ending anime ID
     - `output_file`: Output file name (default: anime_dataset.csv)


      Run the script to generate the anime dataset:
      ```
      python anime_dataset.py
      ```
     

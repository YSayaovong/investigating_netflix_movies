# Importing necessary libraries
import pandas as pd

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")

# Filter data for movies from the 1990s
netflix_1990s = netflix_df[(netflix_df['release_year'] >= 1990) & (netflix_df['release_year'] < 2000)]

# Task 1: Find the most frequent movie duration in the 1990s
# Mode of the 'duration' column
duration = netflix_1990s['duration'].mode()[0]
print(f"Most frequent movie duration in the 1990s: {duration} minutes")

# Task 2: Count the number of short action movies released in the 1990s
# Short movies have a duration < 90 minutes and are of genre 'Action'
short_movie_count = netflix_1990s[(netflix_1990s['duration'] < 90) & (netflix_1990s['genre'] == 'Action')].shape[0]
print(f"Number of short action movies in the 1990s: {short_movie_count}")
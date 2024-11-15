# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the file
# Replace 'netflix_data.csv' with the correct path if it's in a folder (e.g., 'data/netflix_data.csv')
netflix_df = pd.read_csv('netflix_data.csv')

# Filter for 1990s movies based on 'release_year' column
netflix_90s = netflix_df[netflix_df['release_year'].between(1990, 1999)]

# 1. Most frequent movie duration in the 1990s
duration = netflix_90s['duration'].mode()[0]
print(f"Most Frequent Duration: {duration} minutes")

# 2. Counting short action movies
short_action_movies = netflix_90s[(netflix_90s['genre'] == 'Action') & (netflix_90s['duration'] < 90)]
short_movie_count = short_action_movies.shape[0]
print(f"Short Action Movies: {short_movie_count}")

# 3. Plotting the relationship between release year and movie duration (Scatter plot)
plt.figure(figsize=(8, 6))  # Size of the figure
plt.scatter(netflix_90s['release_year'], netflix_90s['duration'], color='skyblue', edgecolor='black')  # Scatter plot
plt.title('Movie Duration vs. Release Year in the 1990s')  # Title of the plot
plt.xlabel('Release Year')  # X-axis label
plt.ylabel('Duration (minutes)')  # Y-axis label

# Save the plot as an image
plt.savefig('scatter_plot_duration_vs_year.png')

# Show the plot
plt.show()

# 4. Plotting the number of movies per genre (Bar chart)
genre_counts = netflix_90s['genre'].value_counts()  # Get the count of movies per genre
plt.figure(figsize=(8, 6))  # Size of the figure
genre_counts.plot(kind='bar', color='coral')  # Bar plot for genre counts
plt.title('Number of Movies by Genre in the 1990s')  # Title of the plot
plt.xlabel('Genre')  # X-axis label
plt.ylabel('Number of Movies')  # Y-axis label

# Save the plot as an image
plt.savefig('bar_chart_genres.png')

# Show the plot
plt.show()

import pandas as pd
import time

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

movies_list = list(movies_df.columns)
index = 0

print('\nindex and columns in movies_df:')
for cols in movies_list:
    print(index, cols)
    index += 1

ratings_list = list(ratings_df.columns)
index = 0

print('\nindex and columns in ratings_df:')
for cols in ratings_list:
    print(index, cols)
    index += 1

start_time = time.time()
print('\nread movies.csv and ratings.csv -', time.time() - start_time)

print(f'\nmovies_df:\n{movies_df}')

# merge both movies_df and ratings_df based on movie_id column
movies_and_ratings_merged_df = pd.merge(ratings_df, movies_df, on='movieId')

print(f'\nmovies_and_ratings_merged_df:\n{movies_and_ratings_merged_df}')

print('\nratings_df and movies_df merged -', time.time() - start_time, '\n')

print('movies_and_ratings_merged_df:\n',movies_and_ratings_merged_df, '\n')

# calcuating average rating of all movies
movie_ratings_averages = movies_and_ratings_merged_df.groupby('title')['rating'].mean().sort_values(ascending=False).head(30)

print(f'\nmovie_ratings_averages:\n{movie_ratings_averages}')

# how many times each movie has been rated
movie_ratings_count = movies_and_ratings_merged_df.groupby('title')['rating'].count().sort_values(ascending=False).head(30)

print(f'\nmovie_ratings_count:\n{movie_ratings_count}')


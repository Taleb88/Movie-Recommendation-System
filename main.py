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

# merge both movies_df and ratings_df based on movie_id column
movies_merge_df = pd.merge(ratings_df, movies_df, on='movieId')

print(f'\n{movies_merge_df}')

print('\nratings_df and movies_df merge -', time.time() - start_time, '\n')


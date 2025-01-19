import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns

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

# calcuating average rating of all movies
movie_ratings_averages = movies_and_ratings_merged_df.groupby('title')['rating'].mean().sort_values(ascending=False).head(30)

print(f'\nmovie_ratings_averages:\n{movie_ratings_averages}')

print('\nrating averages per movie -', time.time() - start_time, '\n')

# how many times each movie has been rated
movie_ratings_count = movies_and_ratings_merged_df.groupby('title')['rating'].count().sort_values(ascending=False).head(30)

print(f'\nmovie_ratings_count:\n{movie_ratings_count}')

print('\nquanity of ratings per movie -', time.time() - start_time, '\n')

# new dataframe countaining number of ratings per movie
num_of_ratings_per_movie_df = pd.DataFrame(movies_and_ratings_merged_df.groupby('title')['rating'].mean())

num_of_ratings_per_movie_df['ratings_count'] = movies_and_ratings_merged_df.groupby('title')['rating'].count().sort_values(ascending=False)

print(f'\nnum_of_ratings_per_movie:\n{num_of_ratings_per_movie_df.head(50)}')

print('\nquanity of ratings per movie -', time.time() - start_time, '\n')

# charts developed
sns.set_style('white')
plt.figure(figsize=(8, 2))
num_of_ratings_per_movie_df['rating'].hist(bins=70)
plt.show()

sns.jointplot(x=num_of_ratings_per_movie_df['rating'],
              y=num_of_ratings_per_movie_df['ratings_count'],
              data=num_of_ratings_per_movie_df,
              color='red',
              height=15)
plt.show()

print('charts developed -', time.time() - start_time, '\n')


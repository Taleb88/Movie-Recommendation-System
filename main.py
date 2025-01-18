import pandas as pd

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

#print(ratings_df.head())
#print(movies_df.head())

# merge both movies_df and ratings_df based on movie_id column
movies_merge_df = pd.merge(ratings_df, movies_df, on='movieId')

print(movies_merge_df)
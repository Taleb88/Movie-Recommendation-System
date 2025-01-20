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

index = 0
for values in movies_df['genres'].head(50).unique(): # searching only for first 50 unique values
    print(index, values)
    index += 1

print('\ndisplaying unique genre values from movies_df -', time.time() - start_time)

print(f'\nmovies_df:\n{movies_df}')

# merge both movies_df and ratings_df based on movie_id column
movies_and_ratings_merged_df = pd.merge(ratings_df, movies_df, on='movieId')

# decimal point will only be 2 spaces to the right
movies_and_ratings_merged_df['rating'] = movies_and_ratings_merged_df['rating'].round(2)

print(f'\nmovies_and_ratings_merged_df:\n{movies_and_ratings_merged_df}')

print('\nratings_df and movies_df merged -', time.time() - start_time, '\n')

# calcuating average rating of all movies
movie_ratings_averages = movies_and_ratings_merged_df.groupby('title')['rating'].mean().sort_values(ascending=False).head(100)

print(f'\nmovie_ratings_averages:\n{movie_ratings_averages}')

print('\nrating averages per movie -', time.time() - start_time, '\n')

# how many times each movie has been rated
movie_ratings_count = movies_and_ratings_merged_df.groupby('title')['rating'].count().sort_values(ascending=False).head(100)

print(f'\nmovie_ratings_count:\n{movie_ratings_count}')

print('\nquanity of ratings per movie -', time.time() - start_time, '\n')

# new dataframe countaining number of ratings per movie
num_of_ratings_per_movie_df = pd.DataFrame(movies_and_ratings_merged_df.groupby('title')['rating'].mean())

num_of_ratings_per_movie_df['rating'] = num_of_ratings_per_movie_df['rating'].round(2)

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

'''ratings_pivot_table = pd.pivot_table(movies_and_ratings_merged_df,
                                     values='rating',
                                     index='userId',
                                     columns='title')

print(ratings_pivot_table)

print('ratings pivot table developed -', time.time() - start_time, '\n')'''

movie_genres_values = list(movies_and_ratings_merged_df['genres'].values)
movie_ratings_values = list(movies_and_ratings_merged_df['rating'].values)

while True:
    try: 
        movie_genres_answer = input('\nplease put in a name of a genre:\n')        
        movie_ratings_answer = float(input('\nplease put in a rating:\n'))
        
        if movie_genres_answer == 'exit' or movie_ratings_answer == -1:
            break

        if (movie_genres_answer in movie_genres_values) and (movie_ratings_answer == 5.0 in movie_ratings_values):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  (movies_and_ratings_merged_df['rating']==movie_ratings_answer)]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 4.5 in movie_ratings_values):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 4.5) & (movies_and_ratings_merged_df['rating'] <= 4.99))]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 4.0 in movie_ratings_values and movie_ratings_answer <= 4.49):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 4.0) & (movies_and_ratings_merged_df['rating'] <= 4.49))]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 3.5 in movie_ratings_values and movie_ratings_answer <= 3.99):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 3.5) & (movies_and_ratings_merged_df['rating'] <= 3.99))]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 3.0 in movie_ratings_values and movie_ratings_answer <= 3.49):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 3.0) & (movies_and_ratings_merged_df['rating'] <= 3.49))]}')   
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 2.5 in movie_ratings_values and movie_ratings_answer <= 2.99):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 2.5) & (movies_and_ratings_merged_df['rating'] <= 2.99))]}')    
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 2.0 in movie_ratings_values and movie_ratings_answer <= 2.49):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 2.0) & (movies_and_ratings_merged_df['rating'] <= 2.49))]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 1.5 in movie_ratings_values and movie_ratings_answer <= 1.99):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 1.5) & (movies_and_ratings_merged_df['rating'] <= 1.99))]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 1.0 in movie_ratings_values and movie_ratings_answer <= 1.49):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 1.0) & (movies_and_ratings_merged_df['rating'] <= 1.49))]}')
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 0.5 in movie_ratings_values and movie_ratings_answer <= 0.99):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 0.5) & (movies_and_ratings_merged_df['rating'] <= 0.99))]}')    
        elif (movie_genres_answer in movie_genres_values) and (movie_ratings_answer >= 0.0 in movie_ratings_values and movie_ratings_answer <= 0.49):
            print(f'{movies_and_ratings_merged_df[(movies_and_ratings_merged_df['genres']==movie_genres_answer) & \
                                                  ((movies_and_ratings_merged_df['rating'] >= 0.0) & (movies_and_ratings_merged_df['rating'] <= 0.49))]}')                                                                                        
        elif movie_genres_answer.isnumeric():
            print('please enter a string value only')
        elif (movie_ratings_answer not in movie_ratings_values) and (movie_genres_answer not in movie_genres_values):
            print('no result')
    except ValueError:
        print('please enter a valid title or numerical figure only')
        continue

print('user input feature developed -', time.time() - start_time, '\n')
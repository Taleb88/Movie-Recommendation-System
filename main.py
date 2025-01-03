import pandas as pd

movies_df = pd.read_csv('movies.csv')
ratings_df = pd.read_csv('ratings.csv')

#print(ratings_df.head())
#print(movies_df.head())

# merge both movies_df and ratings_df based on movie_id column
movies_merge_df = pd.merge(ratings_df, movies_df, on='movieId')

#print(movies_merge.head())

# calculate mean of number of ratings per movie title 
print(movies_merge_df.groupby('title')['rating'].mean().sort_values(
        ascending=False).head()
        )

# calculate count of number of ratings movie title - top 5 results
print(movies_merge_df.groupby('title')['rating'].count().sort_values(
        ascending=False).head()
        )

# creating new dataframes and adding 2 new columns to them
ratings_mean_count_data_df = pd.DataFrame(
    movies_merge_df.groupby('title')['rating'].mean()
    )
#creating a new column "review_count" based on ratings count per movie title
ratings_mean_count_data_df['rating_count'] = pd.DataFrame(
    movies_merge_df.groupby('title')['rating'].count()
    )

print(ratings_mean_count_data_df)

# creating a pivot table to see each user's rating on each movie title
user_rating_pivot_table = movies_merge_df.pivot_table(
    index='userId', columns='title', values='rating'
)

#print(user_rating.head())

# ratings for movies submitted per user (user_id) 
casino_1995_ratings_list_df = user_rating_pivot_table['Casino (1995)']
ace_ventura_when_nature_calls_1995_ratings_list_df = user_rating_pivot_table['Ace Ventura: When Nature Calls (1995)']

print(casino_1995_ratings_list_df.head(15))
print(ace_ventura_when_nature_calls_1995_ratings_list_df.head(15))


# finding movies which correlate with "Casino (1995)"
movies_like_casino_1995 = user_rating_pivot_table.corrwith(casino_1995_ratings_list_df)
corr_casino_1995_df = pd.DataFrame(movies_like_casino_1995, columns=['Correlation']) # adding 'Correlation' column to dataframe
corr_casino_1995_df.head(30).dropna(inplace=True) # remove the n/a values from the dataframe
print(corr_casino_1995_df.sort_values('Correlation',ascending=False).head(30))

movies_like_ace_ventura_when_nature_calls_1995 = user_rating_pivot_table.corrwith(ace_ventura_when_nature_calls_1995_ratings_list_df)
corr_ace_ventura_when_nature_calls_1995_df = pd.DataFrame(movies_like_casino_1995, columns=['Correlation']) # adding 'Correlation' column to dataframe
corr_ace_ventura_when_nature_calls_1995_df.head(30).dropna(inplace=True) # remove the n/a values from the dataframe
print(corr_ace_ventura_when_nature_calls_1995_df.sort_values('Correlation',ascending=False).head(30))

# add a column of "rating_count" from ratings_mean_count_data_df 
#   to the correlation movie dataframe via a join
corr_casino_1995_count_df = \
    corr_casino_1995_df.join(ratings_mean_count_data_df['rating_count'])

corr_ace_ventura_when_nature_calls_1995_count_df = \
    corr_ace_ventura_when_nature_calls_1995_df.join(ratings_mean_count_data_df['rating_count'])


# defining a function that filters out the most correlated movies with ratings from more
#   than 100 users
def rating_count_greater_than_100(df):
    return df[df['rating_count'] > 100].sort_values(
        'Correlation', ascending=False).head()

rating_count_greater_than_100(corr_casino_1995_count_df)
rating_count_greater_than_100(corr_ace_ventura_when_nature_calls_1995_count_df)

corr_casino_1995_count_df = corr_casino_1995_count_df.reset_index()
corr_ace_ventura_when_nature_calls_1995_count_df = corr_ace_ventura_when_nature_calls_1995_count_df.reset_index()

print(corr_casino_1995_count_df)
print(corr_ace_ventura_when_nature_calls_1995_count_df)


# utilizing matplotlib to create graphs
import matplotlib.pyplot as plt 

# "Casino (1995)"
plt.figure(figsize=(10, 4)) 
plt.barh(corr_casino_1995_count_df['title'].head(10), 
         abs(corr_casino_1995_count_df['Correlation'].head(10)),  
         align='center', 
         color='purple') 
plt.xlabel("Popularity") 
plt.title("Top 10 Popular Movies") 
plt.gca().invert_yaxis()
plt.show() # produces bar graph

# "Ace Ventura: When Nature Calls (1995)"
plt.figure(figsize=(10, 4)) 
plt.barh(corr_ace_ventura_when_nature_calls_1995_count_df['title'].head(10), 
         abs(corr_ace_ventura_when_nature_calls_1995_count_df['Correlation'].head(10)),  
         align='center', 
         color='purple') 
plt.xlabel("Popularity") 
plt.title("Top 10 Popular Movies") 
plt.gca().invert_yaxis()
plt.show() # produces bar graph

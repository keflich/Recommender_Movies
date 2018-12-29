import sys
import pandas
import numpy as np


#Reading ratings file:
r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings_df = pandas.read_csv('ratings.dat', sep='::', names=r_cols,
 encoding='latin-1', engine = 'python')
''''
 #Reading users file:
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users_df = pandas.read_csv('users.dat', sep='::', names=u_cols,
 encoding='latin-1', engine = 'python')
'''

 #Reading items file:
i_cols = ['movie_id', 'movie_title','others']
movies_df = pandas.read_csv('movies.dat', sep='::', names=i_cols,
 encoding='latin-1', engine = 'python')

def most_popular_movies ():
    ratings_df_great_3 = ratings_df[ratings_df["rating"]>= 3]
    ratings_df_great_3_count = ratings_df_great_3["movie_id"].value_counts()
    result = pandas.DataFrame({'movie_id':ratings_df_great_3_count.index, 'count':ratings_df_great_3_count.values})
    result_10 = result.head(10)
    merged_pd =  pandas.merge(result_10, movies_df, on='movie_id')
    del merged_pd['others']
    print(merged_pd)
if(__name__ == "__main__"):
    most_popular_movies()
    print("Done ! ")
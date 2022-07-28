# recommends movie by calculating weighted ratings based on IMDb's rating system W = R.v + C.m / v + m
# where W is weighted rating, R is the mean rating for the movie, v is the number of votes for the movie, m is the
# minimum votes (1000) to be listed Top 50, C is the mean vote for all movies.
import collections

import pandas as pd

movies = pd.read_csv("/Users/sanjana/Downloads/tmdb_5000_movies.csv")
credits = pd.read_csv("/Users/sanjana/Downloads/tmdb_5000_credits.csv")

# minimum votes, m
m = movies['vote_count'].quantile(0.9)

# mean vote, C
C = movies['vote_average'].mean()

# filter all movies with minimum of 2500 votes
newMovies = movies[(movies['vote_count'] >= m)]


R = newMovies.columns.get_loc("vote_average")
title = newMovies.columns.get_loc("title")
v = newMovies.columns.get_loc("vote_count")

# Calculates weighted ratings for each of the newMovies

movieDict = {}

for i in range(len(newMovies)):

    weightedRating = ((newMovies.iloc[i, R] * newMovies.iloc[i, v]) + (C * m)) / (newMovies.iloc[i, v] + m)
    movieDict[newMovies.iloc[i, title]] = weightedRating

# Arranges movies in descending order to get top 50 movies

sorted_dict = {}
sorted_keys = reversed(sorted(movieDict, key=movieDict.get))

for w in sorted_keys:
    sorted_dict[w] = movieDict[w]

# Prints top 50 movies and their score

titleList = list(sorted_dict.keys())
score = list(sorted_dict.values())

for i in range(50):
    print(titleList[i], "||", score[i])







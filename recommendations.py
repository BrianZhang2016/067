import pandas as pd
import math
import requests
def recommendation():
    movies = pd.read_csv('movieData/movies.csv')
    movies.set_index("movieId",inplace=True, drop=True)
    dtype_dic= {'imdbId': str,
                'tmdbId' : str}

    links = pd.read_csv("movieData/links.csv", dtype = dtype_dic)
    links.set_index("movieId",inplace=True,drop=True)
    ratings = pd.read_csv("movieData/ratings.csv")
    ratings = ratings.groupby("movieId").mean()
    del ratings["userId"]
    del ratings["timestamp"]
    inputMovie = "toy story"
    movies['title'] = movies['title'].str.lower()
    inputMovies = movies.loc[movies['title'].str.contains(inputMovie,case=False)]
    genres = inputMovies.loc[1,"genres"].split("|")
    results = {}
    for x in range(2,len(movies)):
        try:
            rating = (ratings.loc[x,"rating"])
            x_genres = movies.loc[x,"genres"].split("|")
            common = len(set(x_genres).intersection(genres))
            if common>=3 and rating >=3:
                results[x] = math.dist([rating,common],[5,5])
        except:
            continue
    results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
    results = {k:results[k] for k in list(results.keys())[:10]}
    output = {}
    for x in list(results.keys())[:10]:
        tmdbId = links.loc[x,"tmdbId"]
        movie_data = requests.get("https://api.themoviedb.org/3/movie/{id}?api_key=da1fef95c8fac680ac2ada0bcce7339b".format(id=tmdbId)).json()
        output[tmdbId] = {
            "title":movie_data["title"],
            "poster":movie_data["poster_path"],
            "plot": movie_data["overview"]
        }
    return output
#fix line 12 issue of what movie to use as basis

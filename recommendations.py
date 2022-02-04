import pandas as pd
movies = pd.read_csv('movieData/movies.csv')
movies.set_index("movieId",inplace=True, drop=True)
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
        x_genres = movies.loc[x,"genres"].split("|")
        x_set = set(x_genres)
        common = x_set.intersection(genres)
        if len(common) >=3:
            results[x] = len(common)
    except:
        continue
results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1],reverse=True)}
print((results))
print(genres)
print(inputMovies)
#find all movies with at least 2 common genres
    #make df of that
#rank based on most common elements
#remove anything less than 3 stars
#present top 10


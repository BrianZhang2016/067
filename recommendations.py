import pandas as pd
import math
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
        if len(common) >=3 and ratings.loc[x,"rating"] >=3 :
            results[x] = [len(common),ratings.loc[x,"rating"]]
    except:
        continue
final_data = pd.DataFrame.from_dict(results,orient="index")
final_data.sort_values(by=[0,1],ascending=False,inplace=True)
results = {}
for index,row in final_data.iterrows():
    results[index] = math.dist([row[0],row[1]],[5,5])
results = {k: v for k, v in sorted(results.items(), key=lambda item: item[1])}
for x in list(results.keys())[:10]:
    print(movies.loc[x,"title"])
#find all movies with at least 2 common genres
    #make df of that
#rank based on most common elements
#remove anything less than 3 stars
#present top 10


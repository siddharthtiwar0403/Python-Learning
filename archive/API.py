import pandas as pd
import requests

reponse = requests.get('https://api.themoviedb.org/3/movie/top_rated?api_key=ae69e6b23b4fda50e3754465c0f0f83b')

df = pd.DataFrame(reponse.json()['results'])

df.head(4)[['adult', 'backdrop_path', 'id', 'title', 'overview', 'popularity', 'poster_path']]

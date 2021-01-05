from .models import OTT
import pandas as pd
import numpy as np
def init():
    ott_data = pd.read_csv("./data/MoviesOnStreamingPlatforms_updated.csv")
    cnt = 0
    for i in range(len(ott_data)):
        item = ott_data.iloc[i]
        id = int(item['ID'])
        title = checkNull('Title', item, 'str')
        year = checkNull('Year', item, 'int')
        if item.isnull()['Age']:
            age = None
        else:
            age = item['Age']
            if age == 'all':
                age = 0
            else:
                age = age[:-1]
            age = int(age)
        imdb = checkNull('IMDb', item, 'float')

        if item.isnull()['Rotten Tomatoes']:
            rottenTomatoes = None
        else:
            rottenTomatoes = item['Rotten Tomatoes']
            rottenTomatoes = rottenTomatoes[:-1]
            rottenTomatoes = float(rottenTomatoes) * 0.01
        netflix = checkNull('Netflix', item, 'bool')
        hulu = checkNull('Hulu', item, 'bool')
        primevideo = checkNull('Prime Video', item, 'bool')
        disneyplus = checkNull('Disney+', item, 'bool')
        directors = checkNull('Directors', item, 'str')
        genres = checkNull('Genres', item, 'str')
        country = checkNull('Country', item, 'str')
        language = checkNull('Language', item, 'str')
        runtime = checkNull('Runtime', item, 'int')
        data = OTT(id = id, title = title, year = year, age = age, imdb = imdb, rotten_tomatoes = rottenTomatoes, netflix = netflix, hulu = hulu, primevideo = primevideo, disneyplus = disneyplus, directors = directors, genres = genres, country = country, language = language, runtime = runtime)
        data.save()
        cnt += 1
    return cnt

def checkNull(name, item, dtype):
    if item.isnull()[name]:
        return None
    else:
        if dtype == 'str':
            return str(item[name])
        elif dtype == 'int':
            return int(item[name])
        elif dtype == 'float':
            return float(item[name])
        elif dtype == 'bool':
            return bool(item[name])

from ast import literal_eval
import random

import pandas
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_director(x):
    for i in x:
        if i["job"] == "Director":
            return i["name"]
    return numpy.nan


def get_list(x):
    if isinstance(x, list):
        names = [i["name"] for i in x]
        if len(names) > 3:
            names = names[:3]
        return names
    return []


def clean_data(row):
    if isinstance(row, list):
        return [str.lower(i.replace(" ", "")) for i in row]
    else:
        if isinstance(row, str):
            return str.lower(row.replace(" ", ""))
        else:
            return ""


def create_soup(features):
    return ' '.join(features['keywords']) + ' ' + ' '.join(features['cast']) + ' ' + features['director'] + ' ' + ' '.join(features['genres'])


def predict_movies(liked_movies, disliked_movies, favourites, mood=None):
    pandas.options.display.max_columns = None
    liked = str()
    disliked = str()
    for like in liked_movies:
        liked += like + '|'
    for dislike in disliked_movies:
        disliked += dislike + '|'
    if mood == 'Fear':
        disliked += 'Horror|Crime|'
    if mood == 'Sad':
        disliked += 'War|'
    credits_dataframe = pandas.read_csv('support/tmdb_5000_credits.csv')
    movies_dataframe = pandas.read_csv('support/tmdb_5000_movies.csv')
    movies_dataframe = movies_dataframe[movies_dataframe['vote_average'] > 6.5]
    movies_dataframe = movies_dataframe[movies_dataframe['popularity'] > 40]
    movies_dataframe = movies_dataframe[movies_dataframe['genres'].str.contains(liked[:-1])]
    movies_dataframe = movies_dataframe[~movies_dataframe['genres'].str.contains(disliked[:-1])]
    if 'Superhero' in disliked_movies:
        movies_dataframe = movies_dataframe[~movies_dataframe['keywords'].str.contains('superhero')]
    credits_dataframe.columns = ['id', 'title', 'cast', 'crew']
    movies_dataframe = movies_dataframe.merge(credits_dataframe, on="id")
    features = ["cast", "crew", "keywords", "genres"]
    for feature in features:
        movies_dataframe[feature] = movies_dataframe[feature].apply(literal_eval)
    movies_dataframe["director"] = movies_dataframe["crew"].apply(get_director)
    features = ["cast", "keywords", "genres"]
    for feature in features:
        movies_dataframe[feature] = movies_dataframe[feature].apply(get_list)
    features = ['cast', 'keywords', 'director', 'genres']
    for feature in features:
        movies_dataframe[feature] = movies_dataframe[feature].apply(clean_data)
    movies_dataframe["soup"] = movies_dataframe.apply(create_soup, axis=1)
    count_vectorizer = CountVectorizer(stop_words="english")
    count_matrix = count_vectorizer.fit_transform(movies_dataframe["soup"])
    cosine_sim2 = cosine_similarity(count_matrix, count_matrix)
    moviez = movies_dataframe.copy()
    movies_dataframe = movies_dataframe.reset_index()
    # print(movies_dataframe)
    movie_name = favourites[random.randint(0, len(favourites) - 1)]
    indices = pandas.Series(movies_dataframe.index, index=movies_dataframe.title_x).drop_duplicates()
    def get_recommendations(favourites, cosine_sim=cosine_sim2):
        movie_name = favourites[random.randint(0, len(favourites) - 1)]
        try:
            idx = indices[movie_name]
        except KeyError:
            idx = indices[random.randint(0, len(movies_dataframe) - 1)]
        similarity_scores = list(enumerate(cosine_sim[idx]))
        similarity_scores= sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        similarity_scores = similarity_scores[1:20]
        random.shuffle(similarity_scores)
        movies_indices = [ind[0] for ind in similarity_scores[1:3]]
        movies = list(movies_dataframe.title_x.iloc[movies_indices])
        overviews = list()
        for movie in movies:
            overview = movies_dataframe.loc[movies_dataframe['title_x'] == movie, 'overview'].iloc[0]
            overviews.append(overview)
        return {'films': movies, 'overviews': overviews}
    return get_recommendations(movie_name)

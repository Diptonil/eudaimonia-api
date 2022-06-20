import random
import re

from bs4 import BeautifulSoup as SOUP
import requests as HTTP

def predict_movies(liked, disliked, mood):
    emotion_anticipation = mood.get('anticipation')
    emotion_surprise = mood.get('surprise')
    if 'negative' in mood:
        emotion_sadness = mood.get('sadness')
        emotion_disgust = mood.get('disgust')
        emotion_anger = mood.get('anger')
        emotion_fear = mood.get('fear')
        emotion_list_raw = sorted([rate for rate in [emotion_sadness, emotion_anger, emotion_disgust, emotion_fear] if rate is not None], reverse=True)
        emotion_list_extra = sorted([rate for rate in [emotion_anticipation, emotion_surprise] if rate is not None], reverse=True)
        print(emotion_list_raw)
    elif 'positive' in mood:
        emotion_joy = mood['joy']
        emotion_trust = mood['trust']
        emotion_list_raw = sorted([rate for rate in [emotion_joy, emotion_trust] if rate is not None], reverse=True)
        emotion_list_extra = sorted([rate for rate in [emotion_anticipation, emotion_surprise] if rate is not None], reverse=True)
    genres = ['Western', 'Musical', 'Action', 'Thriller', 'Romance', 'Mystery', 'Horror', 'Fantasy', 'Drama', 'Comedy']
    final_genre = list()
    for genre in genres:
        if genre not in disliked:
            final_genre.append(genre)
    genre = final_genre
    for genre in genres:
        if genre in liked:
            final_genre.append(genre)
    if emotion_list_raw[0] == 'sadness':
        try:
            final_genre.remove('Drama')
            final_genre.remove('Horror')
        except ValueError:
            pass
    genre_chosen = random.choice(final_genre)
    url = 'http://www.imdb.com/search/title?genres=%s&title_type=feature&sort=moviemeter, asc' % (genre_chosen)

    response = HTTP.get(url)
    data = response.text
    soup = SOUP(data, "lxml")
    titles = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')}, limit=7)
    print(titles)
    return titles


def predict_music():
    pass


test = {'disgust': 0.2,  'negative': 0.2, 'fear': 0.2, 'anger': 0.2, 'response': 'Success'}
predict_movies(['Action', 'Thriller', 'Romance', 'Mystery', 'Fantasy'], ['Musical', 'Comedy', 'Horror'], test)
import requests

'''
# Emotion Analysis
headers = {'Authorization': 'Api-Key %s' % 'WNTDnKHs.bd9VaRno8zsc2S6r4l4owTFgLBnijakI'}
corpus = 'They fuck you up, your mum and dad.\
They may not mean to, but they do.\
They fill you with the faults they had\
And add some extra, just for you.'
request = requests.post('http://127.0.0.1:7000/api/v1/get_mood/', json={'CORPUS': corpus}, headers=headers)
print(request.json())
request = requests.post('http://127.0.0.1:7000/api/v1/get_emotion/', json={'CORPUS': corpus}, headers=headers)
print(request.json())

# Movie Recommendation
headers = {'Authorization': 'Api-Key %s' % 'WNTDnKHs.bd9VaRno8zsc2S6r4l4owTFgLBnijakI'}
corpus = 'This is a test corpus to test this weird model I pulled out of some remote ass.\
    The goal of it is to see if it can succeed in gauging the tone of my entry, which, unless otherwise mentioned, is of hope. Just that.\
    I really am waiting on a positive result. But this doesn\'t in any way mean that the intent behind this entry is of any positivity.\
    It is not. It is fuelled by distaste and tiredness. Still, I hope that the sum of the analysis doesn\'t get me a displeasing result.\
    So yes, the purpose of this entry is to just see if my intents are, confusing as they might be at some level (even for humans), understood.'
liked_movie_genre = ['Action', 'Thriller', 'Romance', 'Mystery', 'Fantasy']
disliked_movie_genre = ['Musical', 'Comedy', 'Horror', 'Superhero']
favourite_movies = ['No Country for Old Men', 'Avengers', 'Forrest Gump']
liked_music_genre = []
disliked_music_genre = []
json_data = {'LIKED_MOVIE_GENRES': liked_movie_genre, 'DISLIKED_MOVIE_GENRES': disliked_movie_genre, 'FAVOURITE_MOVIES': favourite_movies, 'CORPUS': corpus}
response = requests.post('http://127.0.0.1:7000/api/v1/get_movie/', json=json_data, headers=headers)
print(response.json())
'''
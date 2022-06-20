import json

from rest_framework.response import Response
from rest_framework.decorators import api_view

from support.nlp_model import predict_mood
from support.recommendation_model import predict_movies, predict_music
from api.serializers import EmotionDetectionSerializer, MovieRecommendationSerializer


@api_view(['POST'])
def get_mood_view(request):
    request_data = json.loads(request.body)
    response = predict_mood(request_data['CORPUS'])
    serializer = EmotionDetectionSerializer(response)
    return Response(serializer.data)


@api_view(['POST'])
def get_movie_view(request):
    request_data = json.loads(request.body)
    mood = predict_mood(request_data['CORPUS'])
    print(mood)
    response = predict_movies(request_data['LIKED_MOVIE_GENRES'], request_data['DISLIKED_MOVIE_GENRES'], mood)
    if len(request_data['LIKED_MOVIE_GENRES']) == 0:
        response['response'] = 'No values found in the LIKED_MOVIE_GENRES key of the JSON object passed. Please consult the documentation.'
    if len(request_data['DISLIKED_MOVIE_GENRES']) == 0:
        response['response'] = 'No values found in the DISLIKED_MOVIE_GENRES key of the JSON object passed. Please consult the documentation.'
    serializer = MovieRecommendationSerializer(response)
    return Response(serializer.data)

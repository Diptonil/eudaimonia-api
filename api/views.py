import json

from rest_framework.response import Response
from rest_framework.decorators import api_view
from transformers import BertTokenizer, BertForSequenceClassification
import numpy as np

from support.nlp_model import predict_mood, predict_emotion
from support.recommendation_model import predict_movies
from api.serializers import EmotionDetectionSerializer, MovieRecommendationSerializer


@api_view(['POST'])
def get_mood_view(request):
    request_data = json.loads(request.body)
    response = predict_mood(request_data['CORPUS'])
    serializer = EmotionDetectionSerializer(response)
    return Response(serializer.data)


@api_view(['POST'])
def get_emotion_view(request):
    request_data = json.loads(request.body)
    response = predict_emotion(request_data['CORPUS'])
    serializer = EmotionDetectionSerializer(response)
    return Response(serializer.data)


@api_view(['POST'])
def view(request, diary_entry):
    model_name = 'bert-base-uncased'
    diary_entry = ""
    tokenizer = BertTokenizer.from_pretrained(model_name)
    model = BertForSequenceClassification.from_pretrained('fine_tuned_bert_model') 
    inputs = tokenizer(diary_entry, return_tensors='pt', truncation=True, padding=True)
    emotions = ['happiness', 'sadness', 'surprise', 'fear', 'anger']
    with tokenizer.as_target_tokenizer():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = np.exp(logits.numpy()) / np.exp(logits.numpy()).sum(axis=1, keepdims=True)
    emotion_percentages = {emotion: probability for emotion, probability in zip(emotions, probabilities[0])}
    return emotion_percentages


@api_view(['POST'])
def get_movie_view(request):
    request_data = json.loads(request.body)
    mood = predict_emotion(request_data['CORPUS'])['emotion']
    print(mood)
    response = predict_movies(request_data['LIKED_MOVIE_GENRES'], request_data['DISLIKED_MOVIE_GENRES'], request_data['FAVOURITE_MOVIES'], mood)
    if len(request_data['LIKED_MOVIE_GENRES']) < 2:
        response['response'] = 'Incorrect number of values found in the LIKED_MOVIE_GENRES key of the JSON object passed. Please consult the documentation.'
    elif len(request_data['DISLIKED_MOVIE_GENRES']) < 2:
        response['response'] = 'Incorrect number of values found in the DISLIKED_MOVIE_GENRES key of the JSON object passed. Please consult the documentation.'
    else:
        response['response'] = ''
    serializer = MovieRecommendationSerializer(response)
    return Response(serializer.data)

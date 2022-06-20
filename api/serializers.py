from rest_framework import serializers

class EmotionDetectionSerializer(serializers.Serializer):

    def to_representation(self, instance):
        instance['response'] = 'Success'
        return instance


class MovieRecommendationSerializer(serializers.Serializer):

    def to_representation(self, instance):
        if (instance['response'] is None) or (instance['response'] == ''):
            instance['response'] = 'Success'
        return instance
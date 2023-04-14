from rest_framework import serializers


class UserInputSerializer(serializers.Serializer):
    budget = serializers.IntegerField()
    available_from = serializers.CharField()
    available_to = serializers.CharField()
    lat = serializers.FloatField()
    long = serializers.FloatField()

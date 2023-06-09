from rest_framework import serializers


class LocInputSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    long = serializers.FloatField()


class LocRadiusSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    long = serializers.FloatField()
    radius = serializers.IntegerField()


class BudgetInputSerializer(serializers.Serializer):
    budget = serializers.IntegerField()
    lat = serializers.FloatField()
    long = serializers.FloatField()


class TypeInputSerializer(serializers.Serializer):
    keyword = serializers.CharField()
    lat = serializers.FloatField()
    long = serializers.FloatField()


class TypeRadiusInputSerializer(serializers.Serializer):
    keyword = serializers.CharField()
    radius = serializers.IntegerField()
    lat = serializers.FloatField()
    long = serializers.FloatField()


class TouristSearchSerializer(serializers.Serializer):
    keyword = serializers.CharField()
    location = serializers.CharField()
    budget = serializers.IntegerField()

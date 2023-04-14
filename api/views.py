import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import LocInputSerializer, BudgetInputSerializer, TypeInputSerializer, TypeRadiusInputSerializer
from .recommender import budget_loc_recommendation, tourism_recommendation, tourist_type_recommendation


class LocInputView(APIView):
    serializer_class = LocInputSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        lat = serializer.validated_data['lat']
        long = serializer.validated_data['long']

        try:
            result = tourism_recommendation(
                lat=lat, long=long)
            context = {
                'data': result
            }
            return Response(context)
        except Exception:
            return Response({'error': "Couldn't find tourist attraction around you"}, status=400)


class BudgetInputView(APIView):
    serializer_class = BudgetInputSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        lat = serializer.validated_data['lat']
        long = serializer.validated_data['long']
        budget = serializer.validated_data['budget']

        try:
            result = budget_loc_recommendation(
                lat=lat, long=long, budget=budget)
            context = {
                'data': result
            }
            return Response(context)
        except Exception:
            return Response({'error': "Couldn't find tourist attraction around you"}, status=400)


class TypeInputView(APIView):
    serializer_class = TypeInputSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        lat = serializer.validated_data['lat']
        long = serializer.validated_data['long']
        preferred_type = serializer.validated_data['preferred_type']

        try:
            result = tourist_type_recommendation(
                lat=lat, long=long, keyword=preferred_type)
            context = {
                'data': result
            }
            return Response(context)
        except Exception:
            return Response({'error': "Couldn't find tourist attraction around you"}, status=400)


class TypeRadiusInputView(APIView):
    serializer_class = TypeRadiusInputSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        lat = serializer.validated_data['lat']
        long = serializer.validated_data['long']
        preferred_type = serializer.validated_data['preferred_type']
        radius = serializer.validated_data['radius']

        try:
            result = tourist_type_recommendation(
                lat=lat, long=long, keyword=preferred_type, max_distance=radius)
            context = {
                'data': result
            }
            return Response(context)
        except Exception:
            return Response({'error': "Couldn't find tourist attraction around you"}, status=400)

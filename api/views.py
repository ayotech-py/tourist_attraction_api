import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .recommender import *

url = 'https://touristattractionapi-production.up.railway.app/places/'
#url = 'http://127.0.0.1:8000/places/'


class UrlViews(APIView):
    def get(self, request):
        return Response({
            'Location View': url+'tourist_attraction/',
            'Location Radius View': url+'tourist_radius/',
            'Budget View': url+'tourist_budget/',
            'Tourist Type View': url+'tourist_type/',
            'Tourist Type-Radius View': url+'tourist_type_radius/',
            'Tourist Search View': url+'tourist_search/'
        })


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


class LocRadiusInputView(APIView):
    serializer_class = LocRadiusSerializer

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        lat = serializer.validated_data['lat']
        long = serializer.validated_data['long']
        radius = serializer.validated_data['radius']

        try:
            result = tourism_recommendation(
                lat=lat, long=long, max_distance=radius)
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
        preferred_type = serializer.validated_data['keyword']

        filtered_history = filter_csv_string(input_list)

        try:
            result = tourist_type_recommendation(
                lat=lat, long=long, keyword=preferred_type)
            context = {
                'data': result,
                'browser_history': filtered_history,
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
        preferred_type = serializer.validated_data['keyword']
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


class SearchView(APIView):
    serializer_class = TouristSearchSerializer

    def post(self, request):
        data = request.data
        #serializer = self.serializer_class(data=data)
        # serializer.is_valid(raise_exception=True)
        keyword = data['keyword']
        country = data['location']
        budget = data['budget']

        try:
            result = tourist_search(
                keyword=keyword, country=country, budget=int(budget))
            context = {
                'data': result
            }
            print(context)
            return Response(context)
        except Exception:
            return Response({'error': "Couldn't find tourist attraction around you"}, status=400)

import json
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserInputSerializer
from .recommender import budget_loc_recommendation


class UserInputView(APIView):
    serializer_class = UserInputSerializer

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

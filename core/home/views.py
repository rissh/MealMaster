from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReceipeSerializer
from .models import Receipe, Ingredients

# Create your views here.
class ReceipeAPI(APIView):

    def get(self, request):
        queryset = Receipe.objects.all()
        serializer = ReceipeSerializer(queryset, many = True)
        return Response({
            "status": True,
            "message" : "data fetched",
            "data": serializer.data,
        })
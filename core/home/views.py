from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReceipeSerializer
from .models import Receipe

class ReceipeAPI(APIView):

    def get(self, request):
        queryset = Receipe.objects.all()
        serializer = ReceipeSerializer(queryset, many=True)
        return Response({
            "status": True,
            "message": "data fetched",
            "data": serializer.data,
        })

    def post(self, request):
        serializer = ReceipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "data is created",
                "data": serializer.data,
            }, status=201)
        return Response({
            "status": False,
            "message": "data not created",
            "data": serializer.errors,
        }, status=400)

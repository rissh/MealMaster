from rest_framework import serializers
from .models import Receipe


class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe  # Your model here
        fields = '__all__'  # or specify the fields you want, e.g., ['id', 'name', 'description']

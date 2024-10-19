from rest_framework import serializers
from .models import Receipe, Ingredients


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients  # Replace with your Ingredient model
        fields = '__all__'  # You can specify the fields or use '__all__'

class ReceipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipe  # Your model here
        fields = '__all__'  # or specify the fields you want, e.g., ['id', 'name', 'description']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['ingredients'] = IngredientSerializer(
            instance.ingredients.all(), many=True
        ).data

        return data
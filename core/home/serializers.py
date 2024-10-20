from rest_framework import serializers
from .models import Receipe, Ingredients

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'

class ReceipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True, required=False)

    class Meta:
        model = Receipe
        fields = '__all__'

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        receipe = Receipe.objects.create(**validated_data)
        for ingredient_data in ingredients_data:
            Ingredients.objects.create(receipe=receipe, **ingredient_data)
        return receipe

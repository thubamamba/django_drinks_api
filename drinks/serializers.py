# Describes the process of going from python Object to JSON
from rest_framework import serializers
from .models import Drink


class DrinkSerializer(serializers.ModelSerializer):
    # Metadata describing the Model
    class Meta:
        model = Drink
        fields = ['id', 'name', 'description']

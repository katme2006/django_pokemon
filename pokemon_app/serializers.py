from rest_framework import serializers # import serializers from DRF
from .models import Pokemon # import Pokemon model from models.py


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon # specify what model this serializer is for
        fields = ['id', 'name', 'level'] # specify the fields you would like this serializer to return. Alternatively if you would like to cover all fields at once you could use "__all__" within the fields list.

class PokemonAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'
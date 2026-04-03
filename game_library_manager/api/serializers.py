from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from core.models import Game, Genre, BacklogEntry


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["id", "name", "image_background", "description"]


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["rawg_id", "title", "cover_url", "genres"]

    genres = GenreSerializer(many=True, read_only=True)

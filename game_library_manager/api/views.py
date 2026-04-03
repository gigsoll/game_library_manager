from django.shortcuts import render
from rest_framework import viewsets
from core.models import Game, Genre, BacklogEntry
from .serializers import GenreSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GameViwSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

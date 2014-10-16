from django.shortcuts import render
from .models import Album

from rest_framework import viewsets

class AlbumViewSet(viewsets.ModelViewSet):
	model = Album
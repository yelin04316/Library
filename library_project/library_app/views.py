from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from library_app.models import LibraryMap
from library_app.serializers import LibraryMapSerializer

class LibraryMapViewSet(viewsets.ModelViewSet):
    queryset = LibraryMap.objects.all()
    serializer_class = LibraryMapSerializer
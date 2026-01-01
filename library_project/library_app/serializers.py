from rest_framework import serializers
from library_app.models import LibraryMap

class LibraryMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryMap
        fields = ('map',)
# API 앤드포인트
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from library_app.models import LibraryMap
from library_app.distance import haversine

class LibraryMapViewSet(viewsets.ViewSet):

    def list(self, request):
        lat = request.query_params.get("lat")
        lng = request.query_params.get("lng")

        if lat is None or lng is None:
            return Response({"error": "lat and lng parameters are required"}, status=400)

        lat = float(lat)
        lng = float(lng)

        result = []
        for lib in LibraryMap.objects.all():
            distance = haversine(lat, lng, lib.latitude, lib.longitude)
            result.append({
                "id": lib.id,
                "name": lib.name,
                "latitude": lib.latitude,
                "longitude": lib.longitude,
                "distance": round(distance, 2),
            })

        result.sort(key=lambda x: x["distance"])
        return Response(result[:5])

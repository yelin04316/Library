"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include #, re_path 혹시 몰라서 남겨둔 코드
from rest_framework.routers import DefaultRouter
from library_app.views import LibraryMapViewSet

router = DefaultRouter()
router.register(r'libraies', LibraryMapViewSet, basename='library')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # re_path('admin/', admin.site.urls), 혹시 몰라 남겨둔 코드
]


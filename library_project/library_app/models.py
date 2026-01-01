# DB 구조
from django.db import models

# Create your models here.

# 도서정보나루에서 받은 정보 저장
# 위도, 경도: FloatField
class LibraryMap(models.Model):
    lib_code = models.CharField(max_length=20, unique=True, default='unknown')
    name = models.CharField(max_length=100, default='unknown library')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    def __str__(self):
        return self.name
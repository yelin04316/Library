from django.db import models

# Create your models here.

class LibraryMap(models.Model):
    map = models.CharField(max_length=10)

    def __str__(self):
        return self.map

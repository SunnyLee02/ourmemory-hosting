from django.db import models

# Memory Model을 만드는 클래스.
# (created), title, description, linenos, language
class Memory(models.Model):
    id = models.AutoField(primary_key=True)
    placeName = models.TextField(default='')
    placeRoad = models.TextField(default='', blank=True)
    placeAddress = models.TextField(default='', blank=True)
    placeX = models.TextField(default='')
    placeY = models.TextField(default='')
    placeUrl = models.TextField(default='', blank=True)
    feedDate = models.TextField(default='')
    description = models.TextField(default= '', blank=True)
    image = models.ImageField(default='media/default_image.jpeg', blank=True)

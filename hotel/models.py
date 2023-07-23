from django.db import models


# Create your models here.
class Rooms(models.Model):
    name = models.CharField(max_length=100)
    room = models.IntegerField(default=0)
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField(default=0)
    wifi = models.BooleanField(default=False)

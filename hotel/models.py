from django.db import models


# Create your models here.
class Rooms:
    id: int
    name: str
    room: int
    img: str
    price: int
    wifi: bool

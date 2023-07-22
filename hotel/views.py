from django.shortcuts import render
from .models import Rooms


# Create your views here.
def index(request):
    room1 = Rooms()
    room1.id = 1
    room1.room = 2
    room1.img = 'room-1.jpg'
    room1.name = 'Dubi'
    room1.price = 103
    room1.wifi = False

    room2 = Rooms()
    room2.id = 1
    room2.room = 22
    room2.img = 'room-2.jpg'
    room2.name = 'Bushehr'
    room2.price = 250
    room2.wifi = True

    room3 = Rooms()
    room3.id = 1
    room3.room = 33
    room3.img = 'room-3.jpg'
    room3.name = 'Talhe'
    room3.price = 123
    room3.wifi = False

    rooms = [room1, room2, room3]

    return render(request, 'index.html', {'rooms': rooms})

from django.shortcuts import render
from .models import Rooms


# Create your views here.
def index(request):
    rooms = Rooms.objects.all()

    return render(request, 'index.html', {'rooms': rooms})

from django.shortcuts import render
from .models import LearningJourney

def index(request):
    journeys = LearningJourney.objects.all().order_by('-date')
    return render(request, 'index.html', {'journey': journeys})

def about(request):
    return render(request, 'aboutMe.html')

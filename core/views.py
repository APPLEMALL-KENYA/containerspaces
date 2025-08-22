from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Slider

def home(request):
    sliders = Slider.objects.filter(is_active=True)
    return render(request, 'home.html', {'sliders': sliders})

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  # Make sure this template exists

# Base/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'Home.html')  # This matches your HTML file

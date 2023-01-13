from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'poultry/home.html')

def journal(request):
    return render(request, 'poultry/journal.html')

def analytics(request):
    return render(request, 'poultry/analytics.html')

def about(request):
    return render(request, 'poultry/about.html')

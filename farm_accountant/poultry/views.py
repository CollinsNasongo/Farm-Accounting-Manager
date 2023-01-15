from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'poultry/home.html', {'title': 'Home'})

def journal(request):
    return render(request, 'poultry/journal.html', {'title': 'Journal'})

def analytics(request):
    return render(request, 'poultry/analytics.html', {'title': 'Analytics'})

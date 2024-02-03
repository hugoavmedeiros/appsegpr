from django.shortcuts import render

from django.views.generic import ListView
from django.http import HttpResponse

def index(request):
    return render(request, 'apoio/index.html')
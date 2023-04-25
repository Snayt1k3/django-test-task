from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


def base(request, name):
    return render(request, 'home.html', {'name': name})

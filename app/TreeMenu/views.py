from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.


class BaseView(TemplateView):
    template_name = 'home.html'

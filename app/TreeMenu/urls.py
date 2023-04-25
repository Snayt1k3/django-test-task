from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.base, {'name': 'Home'}, name='home'),
    path('test/', views.base, {'name': 'Стрелялки'}, name='test'),

]

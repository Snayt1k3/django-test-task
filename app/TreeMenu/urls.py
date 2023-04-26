from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.base, {'name': 'Home'}, name='home'),
    path('horror/', views.base, {'name': 'Хоррор'}, name='horror'),
    path('triller/', views.base, {'name': 'Триллер'}, name='triller'),
    path('c-horror/', views.base, {'name': 'Детский Хоррор'}, name='c-horror'),
    path('triller/c-triller/', views.base, {'name': 'Детский Триллер'}, name='c-triller'),


]

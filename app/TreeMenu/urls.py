from django.urls import path

from . import views

urlpatterns = [
    path('', views.BaseView.as_view(), name='home'),
    path('horror/', views.BaseView.as_view(), name='horror'),
    path('triller/', views.BaseView.as_view(), name='triller'),
    path('c-horror/', views.BaseView.as_view(), name='c-horror'),
    path('triller/c-triller/', views.BaseView.as_view(), name='c-triller'),


]

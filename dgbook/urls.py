from django.urls import path

from . import views

app_name = 'dgbook'
urlpatterns = [

    path('', views.index, name='index'),

    ]
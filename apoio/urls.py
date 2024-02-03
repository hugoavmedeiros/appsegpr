from django.urls import path
from . import views

app_name = 'apoio'

urlpatterns = [
    path('', views.index, name='index'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('juegos/', views.juegos, name='juegos'),
    path('historia/', views.historia, name='historia'),
    path('personajes/', views.personajes, name='personajes'),
    path('wiki/', views.wiki, name='wiki'),
    path('top/', views.top, name='top'),
]
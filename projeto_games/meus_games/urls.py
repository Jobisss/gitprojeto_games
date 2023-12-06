from django.urls import path
from meus_games.views import inicio
from meus_games.views import animal1
from meus_games.views import animal2
from meus_games.views import animal3

urlpatterns = [
    path('', inicio),
    path('cacau/', animal1),
    path('duke/', animal2),
    path('luiza/', animal3),
]

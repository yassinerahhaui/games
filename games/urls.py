from django.urls import path
from . import views



urlpatterns = [
    path('',views.all_game,name='all_games'),
    path('<int:id>',views.game,name='games'),
]
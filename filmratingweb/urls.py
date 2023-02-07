from django.urls import path
from filmratingweb.views import all_movies, new_movie, update_movie, delete_movie

urlpatterns = [
    path('all/', all_movies, name="all_movies"),
    path('new/', new_movie, name="new_movie"),
    path('update/<int:id>', update_movie, name="update_movie"),
    path('delete/<int:id>', delete_movie, name="delete_movie"),
]

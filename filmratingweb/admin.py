from django.contrib import admin
from .models import Movie, Additional_inf, Rate, Actor

#admin.site.register(Movie)

@admin.register(Movie)
class FilmAdmin(admin.ModelAdmin):
    list_display = ["title", "imdb_rating", "year"]
    list_filter = ("year", "imdb_rating")
    search_fields = ("title",)

admin.site.register(Additional_inf)
admin.site.register(Rate)
admin.site.register(Actor)

from django.forms import ModelForm
from .models import Movie, Rate, Additional_inf

class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'year', 'premiere', 'imdb_rating', 'poster']


class AdditionalInfForm(ModelForm):
    class Meta:
        model = Additional_inf
        fields = ['duration', 'species']

class RateForm(ModelForm):
    class Meta:
        model = Rate
        fields = ['stars', 'review']

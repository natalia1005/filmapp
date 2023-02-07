from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Additional_inf, Rate
from .forms import MovieForm, AdditionalInfForm, RateForm
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializes import UserSerializer, MovieSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

def all_movies(request):
    all = Movie.objects.all()
    return render(request, 'film.html', {'movies': all})

@login_required()
def new_movie(request):
    form_movie = MovieForm(request.POST or None, request.FILES or None)
    form_additional = AdditionalInfForm(request.POST or None)

    if all((form_movie.is_valid(), form_additional.is_valid())):
        movie = form_movie.save(commit=False)
        additional = form_additional.save()
        movie.additional = additional
        movie.save()
        return redirect(all_movies)

    return render(request, 'form_movie.html', {'form': form_movie, 'form_additional': form_additional})

@login_required()
def update_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)
    rate = Rate.objects.filter(movie=movie)

    try:
        additional = Additional_inf.objects.get(movie=movie.id)
    except Additional_inf.DoesNotExist:
        additional = None

    form_movie = MovieForm(request.POST or None, request.FILES or None, instance=movie)
    form_additional = AdditionalInfForm(request.POST or None, instance=additional)
    form_rate = RateForm(request.POST or None)

    if request.method == 'POST':
        if 'stars' in request.POST:
            rate = form_rate.save(commit=False)
            rate.movie = movie
            rate.save()

    if all((form_movie.is_valid(), form_additional.is_valid())):
        movie = form_movie.save(commit=False)
        additional = form_additional.save()
        movie.additional = additional
        movie.save()
        return redirect(all_movies)

    return render(request, 'form_movie.html', {'form': form_movie, 'form_additional': form_additional,
                                               'rate': rate, 'form_rate': form_rate, 'new': False})

@login_required()
def delete_movie(request, id):
    movie = get_object_or_404(Movie, pk=id)

    if request.method == "POST":
        movie.delete()
        return redirect(all_movies)

    return render(request, 'confirm.html', {'movie': movie})

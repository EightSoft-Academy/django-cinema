from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import *


# class MovieView(View):
#     """List of all films."""
#
#     def get(self, request):
#         movies = Movie.objects.all()
#         return render(request, "movies/movies_list.html", {"movies_list": movies})

class MovieView(ListView):
    """List of all films."""

    model = Movie  # django automatically will put movie_list by taking the lower(model)
    # context_object_name = 'movies_list'
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_list.html"

# class MoviesDetailView(View):
#     """The description of film."""
#
#     def get(self, request, slug):
#         movies = Movie.objects.get(url=slug)
#         return render(request, "movies/movie_detail.html", {"movies": movies})


class MoviesDetailView(DetailView):
    """The description of film."""

    model = Movie
    slug_field = "url"
    queryset = Movie.objects.filter(draft=False)
    template_name = "movies/movie_detail.html"

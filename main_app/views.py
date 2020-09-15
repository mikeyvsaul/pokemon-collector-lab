from django.shortcuts import render
from .models import Pokemon

from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def pokemons_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })
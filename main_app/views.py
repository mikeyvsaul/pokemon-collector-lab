from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Pokemon
from .forms import FeedingForm

from django.http import HttpResponse


def home(request):
  return HttpResponse('<h1>Hello</h1>')

def about(request):
  return render(request, 'about.html')

def pokemons_index(request):
  pokemons = Pokemon.objects.all()
  return render(request, 'pokemons/index.html', { 'pokemons': pokemons })

def pokemon_detail(request, pokemon_id):
  pokemon = Pokemon.objects.get(id=pokemon_id)
  feeding_form = FeedingForm()
  return render(request, 'pokemons/detail.html', { 'pokemon': pokemon, 'feeding_form': feeding_form })

class PokemonCreate(CreateView):
  model = Pokemon
  fields = '__all__'
  success_url = '/pokemons/'

class PokemonUpdate(UpdateView):
  model = Pokemon
  fields = ['element', 'description', 'age']

class PokemonDelete(DeleteView):
  model = Pokemon
  success_url = '/pokemons/'
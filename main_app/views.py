from django.shortcuts import render
from django.http import HttpResponse
from .models import Pokemon
from django.views.generic.edit import CreateView, UpdateView, DeleteView


def home(request):
    return render(request, 'home.html')


def about(request):
    # return HttpResponse('<h1>About the CatCollector</h1>')
    return render(request, 'about.html')


def pokemons_index(request):
    # view all pokemons
    pokemons = Pokemon.objects.all()
    return render(request, 'pokemons/index.html', {'pokemons': pokemons})


def pokemon_detail(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    return render(request, 'pokemons/detail.html', {'pokemon': pokemon})


class PokemonCreate(CreateView):
    model = Pokemon
    fields = '__all__'
    template_name = 'pokemons/pokemon_form.html'


class PokemonUpdate(UpdateView):
    model = Pokemon
    fields = ('img',)
    template_name = 'pokemons/pokemon_form.html'


class PokemonDelete(DeleteView):
    model = Pokemon
    success_url = "/pokemons/"
    template_name = 'pokemons/pokemon_confirm_delete.html'

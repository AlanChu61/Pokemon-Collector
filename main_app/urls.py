from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('pokemons/', views.pokemons_index, name="pokemons_index"),
    path('pokemons/<int:pokemon_id>', views.pokemon_detail, name="pokemon_detail"),
    path('porkemons/create', views.PokemonCreate.as_view(), name='pokemon_create'),
    path('porkemons/<int:pk>/update',
         views.PokemonUpdate.as_view(), name="pokemon_update"),
    path('porkemons/<int:pk>/delete',
         views.PokemonDelete.as_view(), name="pokemon_delete"),

]

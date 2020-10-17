import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import PokemonEntity, Pokemon, PokemonElementType


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL, description=""):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
        popup=description
    ).add_to(folium_map)


def show_all_pokemons(request):
    entities = PokemonEntity.objects.all()
    pokemons = Pokemon.objects.all()
    pokemons_on_page = []

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in entities:
        add_pokemon(
            folium_map,
            entity.lat,
            entity.lon,
            entity.pokemon.title_ru,
            entity.pokemon.image.path,
            entity.pokemon.description,
        )
        pokemons_on_page.append(entity.pokemon)

    return render(
        request,
        "mainpage.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemons": pokemons_on_page,
        },
    )


def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)
    entities = pokemon.entities.all()
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon.title_ru,
            request.build_absolute_uri(pokemon.image.url),
            pokemon.description,
        )    
    return render(
        request,
        "pokemon.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemon": pokemon,
        },
    )

import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from .models import PokemonEntity, Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
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
        )
        pokemons_on_page.append(get_dict_from_pokemon(entity.pokemon, request))

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
    # return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    entities = PokemonEntity.objects.filter(pokemon__id=pokemon_id)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in entities:
        add_pokemon(
            folium_map,
            pokemon_entity.lat,
            pokemon_entity.lon,
            pokemon_entity.pokemon.title_ru,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url),
        )
    pokemon_dict = get_dict_from_pokemon(pokemon, request)
    if pokemon.previous_evolution:
        pokemon_dict["previous_evolution"] = get_dict_from_pokemon(pokemon.previous_evolution, request)    
    if pokemon.next_evolutions.all():
        next = get_dict_from_pokemon(pokemon.next_evolutions.all()[0], request)
        pokemon_dict["next_evolution"] = next
    return render(
        request,
        "pokemon.html",
        context={
            "map": folium_map._repr_html_(),
            "pokemon": pokemon_dict,
        },
    )


def get_dict_from_pokemon(pokemon, request):        
    return {
        "pokemon_id": pokemon.id,
        "img_url": request.build_absolute_uri(pokemon.image.url),
        "title_ru": pokemon.title_ru,
        "title_en": pokemon.title_en,
        "title_jp": pokemon.title_jp,
        "description": pokemon.description,        
    }

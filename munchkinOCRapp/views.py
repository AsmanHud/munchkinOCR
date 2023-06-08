from django.shortcuts import render
from .forms import DoorCardSearchForm, TreasureCardSearchForm
from .models import Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc, TreasureCard

# Create your views here.


def search(request):
    if request.method == 'POST':
        door_form = DoorCardSearchForm(request.POST, prefix='door')
        treasure_form = TreasureCardSearchForm(request.POST, prefix='treasure')

        if door_form.is_valid():
            card = search_card(door_form, [Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc])
            if card:
                return render(request, 'search.html',
                              {'card': card, 'door_form': door_form, 'treasure_form': treasure_form})
            else:
                error_message = 'Sorry, no such card available! Try again.'

        elif treasure_form.is_valid():
            card = search_card(treasure_form, [TreasureCard])
            if card:
                return render(request, 'search.html',
                              {'card': card, 'door_form': door_form, 'treasure_form': treasure_form})
            else:
                error_message = 'Sorry, no such card available! Try again.'

        return render(request, 'search.html',
                      {'door_form': door_form, 'treasure_form': treasure_form, 'error_message': error_message})
    else:
        door_form = DoorCardSearchForm(prefix='door')
        treasure_form = TreasureCardSearchForm(prefix='treasure')

    return render(request, 'search.html', {'door_form': door_form, 'treasure_form': treasure_form})


def search_card(form, models):
    name = form.cleaned_data['name']
    for Model in models:
        try:
            card = Model.objects.get(name_pl__iexact=name)
            if card.card_type == "Раса" or card.card_type == "Класс":
                card.description_ru = card.description_ru.replace('\n', '<br><br>')
            return card
        except Model.DoesNotExist:
            pass
    return None

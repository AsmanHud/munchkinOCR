from django.shortcuts import render
from .forms import CardSearchForm
from .models import Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc

# Create your views here.


def search(request):
    if request.method == 'POST':
        form = CardSearchForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']

            for Model in [Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc]:
                try:
                    card = Model.objects.get(name_pl__iexact=name)
                    if card.card_type == "Раса" or card.card_type == "Класс":
                        card.description_ru = card.description_ru.replace('\n', '<br><br>')
                    return render(request, 'search.html', {'card': card, 'form': form})
                except Model.DoesNotExist:
                    pass

            return render(request, 'search.html', {'form': form,
                                                   'error_message': 'Sorry, no such card available! Try again.'})

    else:
        form = CardSearchForm()

    return render(request, 'search.html', {'form': form})

from django import forms
from .models import *

CHOICES = []
for model in [Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc]:
    for obj in model.objects.all():
        CHOICES.append((obj.name_pl, obj.name_pl))
CHOICES.sort()

class CardSearchForm(forms.Form):
    name = forms.ChoiceField(choices=CHOICES)

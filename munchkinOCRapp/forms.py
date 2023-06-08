from django import forms
from .models import *


class DoorCardSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(DoorCardSearchForm, self).__init__(*args, **kwargs)

        CHOICES = []
        for model in [Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc]:
            for obj in model.objects.all():
                CHOICES.append((obj.name_pl, obj.name_pl))
        CHOICES.sort()

        self.fields['name'] = forms.ChoiceField(choices=CHOICES)


class TreasureCardSearchForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TreasureCardSearchForm, self).__init__(*args, **kwargs)

        CHOICES = []
        for obj in TreasureCard.objects.all():
            CHOICES.append((obj.name_pl, obj.name_pl))
        CHOICES.sort()

        self.fields['name'] = forms.ChoiceField(choices=CHOICES)

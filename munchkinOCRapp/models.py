from django.db import models


class Card(models.Model):
    name_pl = models.CharField(max_length=200, unique=True)
    name_ru = models.CharField(max_length=200)
    description_ru = models.TextField(blank=True)
    card_type = ""

    def __str__(self):
        return f"{self.card_type + ' ' if self.card_type else ''}{self.name_ru}"

    class Meta:
        abstract = True


class Hireling(Card):
    card_type = "Наёмничек"
    bonus = models.IntegerField()


class Steed(Card):
    card_type = "Скакун"
    bonus = models.IntegerField()
    is_big = models.BooleanField(default=True)
    price = models.IntegerField()


class Monster(Card):
    card_type = "Монстр"
    undead = models.BooleanField(default=False)
    level = models.IntegerField()
    bad_stuff = models.TextField()
    get_two_levels = models.BooleanField(default=False)
    treasures = models.IntegerField()


class MonsterModifier(Card):
    card_type = "Модификатор"
    modifier = models.IntegerField()

    def save(self, *args, **kwargs):
        # Calculate description_ru based on modifier
        self.description_ru = f"Применить в бою. Если монстр побеждён, возьми на " \
                              f"{1 if abs(self.modifier) == 5 else 2} " \
                              f"Сокровище {'больше' if self.modifier > 0 else 'меньше'} (минимум 1)."
        super().save(*args, **kwargs)


class Race(Card):
    card_type = "Раса"


class Class(Card):
    card_type = "Класс"


class Curse(Card):
    card_type = "Проклятие"


class Misc(Card):
    card_type = ""


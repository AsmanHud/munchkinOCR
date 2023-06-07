from django.contrib import admin
from .models import Hireling, Steed, Monster, MonsterModifier, Race, Class, Curse, Misc
# Register your models here.

admin.site.register(Hireling)
admin.site.register(Steed)
admin.site.register(Monster)
admin.site.register(MonsterModifier)
admin.site.register(Race)
admin.site.register(Class)
admin.site.register(Curse)
admin.site.register(Misc)
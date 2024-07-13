from django.contrib import admin

from equal.models import Player, Problem, Rank
from django.contrib.auth.models import User

admin.site.register(Player)
admin.site.register(Problem)
admin.site.register(Rank)
# admin.site.register(User)
# Register your models here.

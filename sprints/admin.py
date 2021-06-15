from django.contrib import admin
from .models import SprintGoal, SprintHabit, DailyToDo, Sprint, Mood, Energy


admin.site.register(Sprint)
admin.site.register(SprintGoal)
admin.site.register(SprintHabit)
admin.site.register(Mood)
admin.site.register(DailyToDo)
admin.site.register(Energy)

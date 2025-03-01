from django.contrib import admin

# Register your models here.
from .models import Trip, Expense, Settlement

admin.site.register(Trip)
admin.site.register(Expense)
admin.site.register(Settlement)
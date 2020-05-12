from django.contrib import admin

# Register your models here.

from .models import Country, City, Vanue, Person




admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
admin.site.register(Vanue)
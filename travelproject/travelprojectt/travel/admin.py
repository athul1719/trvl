from django.contrib import admin

from travel.models import place
from travel.models import names
# Register your models here.
admin.site.register(place)
admin.site.register(names)
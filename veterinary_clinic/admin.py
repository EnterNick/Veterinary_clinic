from django.contrib import admin

from .models import Person, Request, Settings, Services

admin.site.register(Request)
admin.site.register(Services)
admin.site.register(Person)
admin.site.register(Settings)

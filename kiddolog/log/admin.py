from django.contrib import admin

from .models import Kid, Caretaker, Log

admin.site.register(Kid)
admin.site.register(Caretaker)
admin.site.register(Log)

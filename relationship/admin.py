from django.contrib import admin
from .models import Creator, Developers, Frameworks, Language

# Register your models here.

admin.site.register(Creator)
admin.site.register(Language)
admin.site.register(Frameworks)
admin.site.register(Developers)

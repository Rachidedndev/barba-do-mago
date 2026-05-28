from django.contrib import admin
from .models import Lugar, NPC

# Registrando os modelos para aparecerem na interface web
admin.site.register(Lugar)
admin.site.register(NPC)
from django.contrib import admin
from .models import *
# Register your models here.

class registro(admin.ModelAdmin):
    list_display=('nombre', 'correo', 'area')

admin.site.register(registroSafely, registro)
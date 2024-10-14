from django.contrib import admin
from django.contrib.admin import site, ModelAdmin

from .models import clinica, solicitar, recuperacao


# Register your models here.
class clinicaadmin(ModelAdmin):
    list_display = ('id','nome')

class solicitaadmin(ModelAdmin):
    list_display = ('protocolo','data', 'ip')

class recuperaadmin(ModelAdmin):
    list_display = ('nome','email', 'clinica')

site.register(clinica, clinicaadmin)
site.register(solicitar, solicitaadmin)
site.register(recuperacao,recuperaadmin)
from django.contrib import admin
from .models import Equipo, Arriendo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):  
    list_display = ('nombre', 'descripcion', 'precio_arriendo', 'disponible')
    list_filter = ('disponible',)
    search_fields = ('nombre', 'descripcion')

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('equipo', 'fecha_inicio', 'fecha_fin', 'cliente', 'precio_arriendo')
    list_filter = ('fecha_inicio', 'fecha_fin')
    search_fields = ('cliente', 'equipo__nombre')
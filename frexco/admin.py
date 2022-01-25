from django.contrib import admin


from .models import Region, Fruit


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'criacao', 'atualizacao', 'ativo')


@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'criacao', 'atualizacao', 'ativo')

# Register your models here.

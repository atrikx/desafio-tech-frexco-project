from django.db import models


class Base(models.Model):

    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Region(Base):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'
    
    def __str__(self):
        return self.name

class Fruit(Base):
    name = models.CharField(max_length=20)
    region = models.ForeignKey(Region, related_name='fruits_related', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Fruit'
        verbose_name_plural = 'Fruts'

# Create your models here.

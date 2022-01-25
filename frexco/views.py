

##API V2
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



##API V1

from rest_framework import generics

from .models import Region, Fruit

from .serializers import RegionSerializer, FruitSerializer


## Inicio da V1 API - Inativo ##
class RegionsAPIView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class FruitsAPIView(generics.ListCreateAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer

class RegionAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class FruitAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer


## V2 da atual API ##

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @action(detail=True, methods=['get'])
    def fruits_related(self, request, pk=None):
        region = self.get_object()
        serializer = FruitSerializer(region.fruits_related.all(), many=True)
        return Response(serializer.data)

class FruitViewSet(viewsets.ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer


## V2 da atual API ##

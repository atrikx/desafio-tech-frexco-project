from rest_framework import serializers

from .models import Region, Fruit


class FruitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fruit
        fields = (
            'id',
            'name',
            'region',
        )


class RegionSerializer(serializers.ModelSerializer):

    fruits_related = FruitSerializer(many=True, read_only=True)

    class Meta:
        model = Region
        fields = (
            'id',
            'name',
            'fruits_related',
        )


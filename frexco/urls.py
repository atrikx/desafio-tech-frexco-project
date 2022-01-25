from django.urls import path

from rest_framework.routers import SimpleRouter

from frexco.views import RegionAPIView, FruitAPIView, RegionsAPIView, FruitsAPIView, RegionViewSet, FruitViewSet

router = SimpleRouter()
router.register('regions', RegionViewSet)
router.register('fruits', FruitViewSet)

urlpatterns = [
    #    path('regions/', RegionsAPIView.as_view(), name='regions'),
    #   path('fruits/', FruitsAPIView.as_view(), name='fruits'),
    #  path('regions/<int:pk>/', RegionAPIView.as_view(), name='region'),
    # path('fruits/<int:pk>/', FruitAPIView.as_view(), name='fruit'),
]

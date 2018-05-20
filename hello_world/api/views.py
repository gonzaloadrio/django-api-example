from rest_framework import viewsets, permissions

from api import serializers
from core.models import Building, Floor


# Create your views here.
class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = serializers.BuildingSerializer
    permission_classes = (permissions.IsAuthenticated,)


class FloorViewSet(viewsets.ModelViewSet):
    queryset = Floor.objects.all()
    serializer_class = serializers.FloorSerializer
    permission_classes = (permissions.IsAuthenticated,)

from core.models import Building, Floor
from rest_framework import serializers


class FloorSerializer(serializers.ModelSerializer):
    # building = serializers.SerializerMethodField('get_building_display')
    #
    # def get_building_display(self, obj):
    #     return obj.get_building_display()

    class Meta:
        model = Floor
        fields = ('id', 's_id', 'name', 'description', 'building')


class BuildingSerializer(serializers.ModelSerializer):
    floors = FloorSerializer(many=True, read_only=True)

    class Meta:
        model = Building
        fields = ('id', 's_id', 'name', 'description', 'location', 'position', 'floors',)

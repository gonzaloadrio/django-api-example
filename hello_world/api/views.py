from rest_framework import viewsets, permissions, views, response
import math
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


class CustomDataView(views.APIView):

    def get(self, request):
        points = [(10, 5), (20, 5), (20, 10), (15, 7), (10, 10)]
        point = (15, 6)
        serializer = serializers.CustomDataSerializer(
            many=True,
            data=[
                {
                    'nombre': 'Gonzalo',
                    'cantidad': 28,
                    'varios': points,
                    'point': point,
                    'is_in_polygon': inside_polygon(point[0], point[1], points),
                    'is_in_circle': inside_circle(point[0], point[1], points[0][0], points[0][1], 100),
                },
            ]
        )
        serializer.is_valid(raise_exception=True)
        return response.Response(serializer.data, 200)


def inside_polygon(x, y, points):
    """
    Return True if a coordinate (x, y) is inside a polygon defined by
    a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].

    Reference: http://www.ariel.com.au/a/python-point-int-poly.html
    """
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(1, n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def inside_circle(x, y, center_x, center_y, radius):
    dist = math.hypot(center_x - x, center_y - y)
    return radius > dist

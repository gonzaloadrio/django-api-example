import json
import random

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
        points = [(4, 4)]
        for i in range(0, 1000):
            x = random.randint(0, 800)
            y = random.randint(0, 600)
            points.append((x, y))

        point = (15, 6)

        num_points = len(points)

        polygons = grid(points)

        for i in range(0, len(polygons)):
            for j in range(0, len(polygons[i])):
                if polygons[i][j]['points_inside'] > 0:
                    print(polygons[i][j])

        # for i in range(0, len(polygons)):
        #     for j in range(0, len(polygons[i])):
        #         polygon = polygons[i][j]
        #         for point in points:
        #             if inside_polygon(point[0], point[1], polygon['points']):
        #                 polygons[i][j]['points_inside'] += 1
        #         if polygons[i][j]['points_inside'] is not 0:
        #             polygons[i][j]['weight'] = polygons[i][j]['points_inside'] / num_points

        with open('data/data.json', 'w') as outfile:
            json.dump(polygons, outfile, indent=4)

        # print(str(polygons))

        serializer = serializers.CustomDataSerializer(
            many=True,
            data=
            [
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


def grid(points):
    step_count = 50
    width = 800
    height = 600

    x_start = 0
    y_start = 0

    polygons = []

    for i, x in enumerate(range(x_start, width, step_count)):
        polygons.append([])
        for j, y in enumerate(range(y_start, height, step_count)):
            polygons[i].append(
                {
                    'points':
                        [
                            [x, y],
                            [x + step_count, y],
                            [x + step_count, y + step_count],
                            [x, y + step_count]
                        ],
                    'points_inside': 0,
                    'weight': 0
                }
            )
            for point in points:
                if inside_polygon(point[0], point[1], polygons[i][j]['points']):
                    polygons[i][j]['points_inside'] += 1
            if polygons[i][j]['points_inside'] is not 0:
                polygons[i][j]['weight'] = polygons[i][j]['points_inside'] / len(points)

    return polygons

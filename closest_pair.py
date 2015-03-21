__author__ = 'gregory'

import sys
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "(%d, %d)" % (self.x, self.y)

class LineSegment:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def length(self):
        return math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2)

points = []
shortest_distance = None

with open(sys.argv[1], 'r') as file:
    number_of_points = int(file.readline().strip())

    for i in range(number_of_points):
        current_point = Point(*[int(n) for n in file.readline().strip().split()])
        points += [current_point]

        for point in [point for point in points if point != current_point]:
            distance = LineSegment(point, current_point).length()

            if shortest_distance is None:
                shortest_distance = distance
            elif distance < shortest_distance:
                shortest_distance = distance

if shortest_distance is None:
    print("INFINITY")
elif shortest_distance >= 10000:
    print("INFINITY")
else:
    print("%.4f" % shortest_distance)

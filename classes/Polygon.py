from classes.Point import Point
from classes.Line import Line
from classes.helpers import left_turn, right_turn
import matplotlib.pyplot as plt


class Polygon:
    points = []

    def __init__(self, points):
        self.points = self.sort(points)

    def sort(self, to_sort_points):
        points = to_sort_points
        midpoint_x = sum(point.x for point in to_sort_points) / len(to_sort_points)
        midpoint_y = sum(point.y for point in to_sort_points) / len(to_sort_points)
        midpoint = Point(midpoint_x, midpoint_y)

        def sort_by_angle(point):
            return midpoint.angle(point)

        to_sort_points.sort(key=sort_by_angle)
        return to_sort_points + [points[0]]

    def is_convex(self):
        is_convex = True
        for i in range(len(self.points) - 2):
            line = Line(self.points[i], self.points[i+1])
            print(line.point_a,line.point_b,self.points[i+2], line.left_turn(self.points[i+2]))
            if not line.left_turn(self.points[i+2]):
                is_convex = False
                break
        return is_convex

    def print(self):
        for point in self.points:
            print(point)

    def check_point_inclusion(self, query_point: Point):
        all_Left = True
        all_Right = True
        for i in range(len(self.points) - 1):
            left = left_turn(self.points[i], self.points[i + 1], query_point)
            right = right_turn(self.points[i], self.points[i + 1], query_point)
            if right:
                all_Left = False
            if left:
                all_Right = False
        return all_Left or all_Right

    def draw(self):
        x_values = [point.x for point in self.points]
        y_values = [point.y for point in self.points]
        plt.plot(x_values, y_values)

# %%

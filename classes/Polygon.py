from classes.Point import Point
from classes.Line import Line
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
            turn = line.check_turn_test(self.points[i+2])
            if turn != "leftturn":
                is_convex = False
                break
        return is_convex

    def print(self):
        for point in self.points:
            print(point)

    def draw(self):
        x_values = [point.x for point in self.points]
        y_values = [point.y for point in self.points]
        plt.plot(x_values, y_values)



#%%

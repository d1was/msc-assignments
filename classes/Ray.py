from classes.Point import Point
from classes.Line import Line

class Ray(Line):
    def __init__(self, point_a: Point, point_b: Point):
        super().__init__(point_a, point_b)
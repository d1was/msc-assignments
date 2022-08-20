import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def angle(self, point: "Point"):
        return math.atan2(point.y - self.y, point.x - self.x) * 100 / math.pi

    def __str__(self):
        return str(self.x) + "," + str(self.y)
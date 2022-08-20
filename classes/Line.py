from classes.Point import Point
from classes.Intersection import Intersection

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def check_betweenness(self, point_c: Point):
        points = [self.point_a, self.point_b]
        def sort_by_x(point):
            return point.x
        points.sort(key=sort_by_x)

        if point_c.x >= points[0].x and point_c.x <= points[1].x and point_c.y >= points[0].y and point_c.y <= points[1].y :
                return True

    def check_turn_test(self, point_c: Point):
        # cross product of three vector p0,p1,p2 = (x1-x0)(y2-y0) - (x2-x0)(y1-y0)
        area = (self.point_b.x - self.point_a.x) * (point_c.y - self.point_a.y) - (point_c.x - self.point_a.x) * (self.point_b.y - self.point_a.y)
        area = int(area)
        if area == 0:
            return "colinear"
        elif area > 0:
            return "leftturn"
        else:
            return "rightturn"

    def check_intersection(self, second_line: "Line"):
        abc_turntest = self.check_turn_test(second_line.point_a)
        abd_turntest = self.check_turn_test(second_line.point_b)

        if abc_turntest == abd_turntest:
            print("These two lines doesn't intersect")
            return Intersection.NO_INTERSECTION
        elif abc_turntest != "colinear" and abd_turntest != "colinear":
            print("These two lines intersect and is a proper intersection")
            return Intersection.PROPER_INTERSECTION
        else:
            point_to_check_betweenness = second_line.point_a if abc_turntest == "colinear" else second_line.point_b
            is_between = self.check_betweenness(point_to_check_betweenness)
            if is_between:
                print("Improper Intersection")
                return Intersection.IMPROPER_INTERSECTION
            else:
                print("No Intersection, just collinear")
                return Intersection.NO_INTERSECTION

    def is_horizontal(self):
        if self.point_a.x == self.point_b.x:
            return True
        else:
            return False
#%%

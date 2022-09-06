from classes.Point import Point
from classes.Intersection import Intersection

class Line:
    def __init__(self, point_a: Point, point_b: Point):
        self.point_a = point_a
        self.point_b = point_b

    def check_betweenness(self, point_c: Point):
        if not self.collinear(point_c):
            return False

        if self.point_a.x != self.point_b.x:
            return ( (self.point_a.x <= point_c.x) and (point_c.x <= self.point_b.x) ) or ( (self.point_a.x >= point_c.x) and (point_c.x >= self.point_b.x) )
        else:
            return ( (self.point_a.y <= point_c.y) and (point_c.y <= self.point_b.y) ) or ( (self.point_a.y >= point_c.y) and (point_c.y >= self.point_b.y) )


    def area(self, point_c: Point):
        # cross product of three vector p0,p1,p2 = (x1-x0)(y2-y0) - (x2-x0)(y1-y0)
        area = (self.point_b.x - self.point_a.x) * (point_c.y - self.point_a.y) - (point_c.x - self.point_a.x) * (self.point_b.y - self.point_a.y)
        area = int(area)
        return area

    def left_turn(self, point_c: Point):
        return self.area(point_c) > 0

    def right_turn(self, point_c: Point):
        return self.area(point_c) < 0

    def collinear(self, point_c: Point):
        return self.area(point_c) == 0

    def intersection_proper(self, second_line: "Line"):
        a = self.point_a
        b = self.point_b
        c = second_line.point_a
        d = second_line.point_b

        if(
            self.collinear(a,b,c) or
            self. collinear(a,b,d) or
            self.collinear(c,d,a) or
            self.collinear(c,d,b)
        ):
            return False

        return self.xor( self.left_turn(a,b,c), self.left_turn(a,b,d)) and self.xor( self.left_turn(a,b,c), self.left_turn(c,d,b))

    def xor(self, x: bool, y: bool):
        return x ^ y

    def intersection(self, second_line: "Line"):
        a = self.point_a
        b = self.point_b
        c = second_line.point_a
        d = second_line.point_b
        if self.intersection_proper(second_line):
            return True
        elif(self.check_betweenness(second_line) or self.check_betweenness(a,b,d) or
            self.check_betweenness(c,d,a) or self.check_betweenness(c,d,b)):
            return True
        else:
            return False

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

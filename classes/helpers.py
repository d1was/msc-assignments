from classes.Point import Point


def area(a: Point, b: Point, c: Point):
    # cross product of three vector p0,p1,p2 = (x1-x0)(y2-y0) - (x2-x0)(y1-y0)
    area = (b.x - a.x) * (c.y - a.y) - (c.x - a.x) * (b.y - a.y)
    area = int(area)
    return area


def left_turn(a: Point, b: Point, c: Point):
    return area(a, b, c) > 0


def right_turn(a: Point, b: Point, c: Point):
    return area(a, b, c) < 0


def collinear(a: Point, b: Point, c: Point):
    return area(a, b, c) == 0


def check_betweenness(a: Point, b: Point, c: Point):
    if not collinear(a, b, c):
        return False

    if a.x != b.x:
        return ((a.x <= c.x) and (c.x <= b.x)) or ((a.x >= c.x) and (c.x >= b.x))
    else:
        return ((a.y <= c.y) and (c.y <= b.y)) or ((a.y >= c.y) and (c.y >= b.y))


def xor(x: bool, y: bool):
    return x ^ y


# %%

def intersection_proper(a: Point, b: Point, c: Point, d: Point):
    if (
            collinear(a, b, c) or
            collinear(a, b, d) or
            collinear(c, d, a) or
            collinear(c, d, b)
    ):
        return False
    return xor(left_turn(a, b, c), left_turn(a, b, d)) and xor(left_turn(c, d, a), left_turn(c, d, b))


def intersection(a: Point, b: Point, c: Point, d: Point):
    if intersection_proper(a, b, c, d):
        return True
    elif (check_betweenness(a, b, c) or check_betweenness(a, b, d) or
          check_betweenness(c, d, a) or check_betweenness(c, d, b)):
        return True
    else:
        return False


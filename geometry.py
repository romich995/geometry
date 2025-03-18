

class Geometry:
    pass


class Point(Geometry):
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point(x={self.x}, y={self.y})"

    def serialize(self):
        return vars(self)

    @classmethod
    def deserialize(cls, dct: dict):
        return cls(dct["x"], dct["y"])


class Segment(Geometry):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Segment(a={self.a}, b={self.b})"

    def serialize(self):
        return {"a": self.a.serialize(),
                "b": self.b.serialize()}

    @classmethod
    def deserialize(cls, dct: dict):
        return cls(Point.deserialize(dct["a"]),
                   Point.deserialize(dct["b"]))


class Circle(Geometry):
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def __str__(self):
        return f"Circle(center={self.center}, radius={self.radius})"

    def serialize(self):
        return {"center": self.center.serialize(),
                "radius": self.radius}


    @classmethod
    def deserialize(cls, dct: dict):
        return cls(Point.deserialize(dct["center"]),
                   dct["radius"])



class Square(Geometry):
    def __init__(self, left_top: Point, side_length: float, angle: float):
        assert 0 <= angle < 360
        self.left_top = left_top
        self.side_length = side_length
        self.angle = angle

    def __str__(self):
        return f"Square(left_top={self.left_top}, side_length={self.side_length}, angle={self.angle})"

    def serialize(self):
        return {"left_top": self.left_top.serialize(),
                "side_length": self.side_length,
                "angle": self.angle}

    @classmethod
    def deserialize(cls, dct: dict):
        return cls(Point.deserialize(dct["left_top"]),
                   dct["side_length"], dct["angle"])

class Rectangle(Geometry):
    def __init__(self, left_top: Point, right_length: float, bottom_length: float, angle: float):
        assert 0 <= angle < 360
        self.left_top = left_top
        self.right_length = right_length
        self.bottom_length = bottom_length
        self.angle = angle


    def __str__(self):
        return f"Rectangle(left_top={self.left_top}, right_length={self.right_length}, bottom_length={self.bottom_length}, angle={self.angle})"

    def serialize(self):
        return {"left_top": self.left_top.serialize(),
                "right_length": self.right_length,
                "bottom_length": self.bottom_length,
                "angle": self.angle}

    @classmethod
    def deserialize(cls, dct: dict):
        return cls(Point.deserialize(dct["left_top"]),
                   dct["right_length"], dct["bottom_length"], dct["angle"])

class Ellipse(Geometry):
    def __init__(self, focus_1: Point, focus_2: Point, distance: float):
        self.focus_1 = focus_1
        self.focus_2 = focus_2
        self.distance = distance

    def __str__(self):
        return f"Ellipse(focus_1={self.focus_1}, focus_2={self.focus_2}, distance={self.distance})"

    def serialize(self):
        return {"focus_1": self.focus_1.serialize(),
                "focus_2": self.focus_2.serialize(),
                "distance": self.distance}

    @classmethod
    def deserialize(cls, dct: dict):
        return cls(Point.deserialize(dct["focus_1"]), Point.deserialize(dct["focus_2"]),
                   dct["distance"])



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
    def __init__(self, left_top: Point, side_length: float):
        self.left_top = left_top
        self.side_length = side_length

    def __str__(self):
        return f"Square(left_top={self.left_top}, side_length={self.side_length})"

    def serialize(self):
        return {"left_top": self.left_top.serialize(),
                "side_length": self.side_length}

    @classmethod
    def deserialize(cls, dct: dict):
        return cls(Point.deserialize(dct["left_top"]),
                   dct["side_length"])


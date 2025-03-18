import argparse

import tinydb
from tinydb import Query

from geometry import Point, Segment, Circle, Square, Rectangle
from resolvers import AddResolver, DeleteResolver, ShowResolver


def add_point_arguments(parser):
    parser.add_argument("x", type=float, help="x coordinate")
    parser.add_argument("y", type=float, help="y coordinate")


def add_square_arguments(parser):
    parser.add_argument("left_top_x", type=float, help="x coordinate of left top point")
    parser.add_argument("left_top_y", type=float, help="y coordinate of left top point")
    parser.add_argument("side_length", type=float,  help="side length")
    parser.add_argument("angle", type=float, help="angle")


def add_segment_arguments(parser):
    parser.add_argument("a_x", type=float, help="x coordinate of first Point")
    parser.add_argument("a_y", type=float, help="y coordinate of first Point")
    parser.add_argument("b_x", type=float, help="x coordinate of second Point")
    parser.add_argument("b_y", type=float, help="y coordinate of second Point")


def add_circle_arguments(parser):
    parser.add_argument("center_x", type=float, help="x coordinate of center")
    parser.add_argument("center_y", type=float, help="y coordinate of center")
    parser.add_argument("radius", type=float,  help="y coordinate of center")

def add_ellips_arguments(parser):
    parser.add_argument("focus_1_x", type=float, help="x coordinate of first focus")
    parser.add_argument("focus_1_y", type=float, help="y coordinate of first focus")
    parser.add_argument("focus_2_x", type=float,  help="x coordinate of second focus")
    parser.add_argument("focus_2_y", type=float,  help="y coordinate of second focus")
    parser.add_argument("distance", type=float,  help="sum distance from two focus")


def add_rectangle_arguments(parser):
    parser.add_argument("left_top_x", type=float, help="x coordinate of left top point")
    parser.add_argument("left_top_y", type=float, help="y coordinate of left top point")
    parser.add_argument("right_side_length", type=float,  help="right side length")
    parser.add_argument("bottom_side_length", type=float,  help="bottom side length")
    parser.add_argument("angle", type=float, help="angle")


db = tinydb.TinyDB('./tiny.db')

parser = argparse.ArgumentParser()

subparser = parser.add_subparsers(title="Commands", dest="cmd")

add = subparser.add_parser("add", help="add new figure")
add_figure = add.add_subparsers(title="Figures", dest="figure")

add_point = add_figure.add_parser("point", help="add new point")
add_point_arguments(add_point)

add_segment = add_figure.add_parser("segment", help="add new segment")
add_segment_arguments(add_segment)

add_circle = add_figure.add_parser("circle", help="add new circle")
add_circle_arguments(add_circle)

add_square = add_figure.add_parser("square", help="add new square")
add_square_arguments(add_square)

add_ellipse = add_figure.add_parser("ellipse", help="add new ellipse")
add_ellips_arguments(add_ellipse)

add_rectangle = add_figure.add_parser("rectangle", help="add new rectangle")
add_rectangle_arguments(add_rectangle)


show = subparser.add_parser("show", help="show figures")

delete = subparser.add_parser("delete", help="delete figure")

delete_figure = delete.add_subparsers(title="Figures", dest="figure")

delete_point = delete_figure.add_parser("point", help="delete point")
add_point_arguments(delete_point)

delete_segment = delete_figure.add_parser("segment", help="delete segment")
add_segment_arguments(delete_segment)

delete_circle = delete_figure.add_parser("circle", help="delete circle")
add_circle_arguments(delete_circle)

delete_square = delete_figure.add_parser("square", help="delete square")
add_square_arguments(delete_square)

delete_ellipse = delete_figure.add_parser("ellipse", help="delete ellipse")
add_ellips_arguments(delete_ellipse)

delete_rectangle = delete_figure.add_parser("rectangle", help="delete rectangle")
add_rectangle_arguments(delete_rectangle)

parse_args = parser.parse_args()


class FigureService:
    figure: str
    def __init__(self, parser):
        self.parser = parser
        self.storage = db.table(self.figure)


class PointService(FigureService):
    figure = 'point'

    def add(self):
        self.storage.insert(
            Point(
                self.parser.x,
                self.parser.y
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["x"] == self.parser.x) &
            (Query()["y"] == self.parser.y)
        )


    def show(self):
        print("Points:",)
        print('\n'.join(str(Point.deserialize(point)) for point in self.storage.all()))


class SegmentService(FigureService):
    figure = 'segment'

    def add(self):
        self.storage.insert(
            Segment(
                Point(self.parser.a_x, self.parser.a_y),
                Point(self.parser.b_x, self.parser.b_y)
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["a"]["x"] == self.parser.a_x) &
            (Query()["a"]["y"] == self.parser.a_y) &
            (Query()["b"]["x"] == self.parser.b_x) &
            (Query()["b"]["y"] == self.parser.b_y)
        )

    def show(self):
        print("Segments:", )
        print('\n'.join(str(Segment.deserialize(segment)) for segment in self.storage.all()))


class CircleService(FigureService):
    figure = 'circle'

    def add(self):
        self.storage.insert(
            Circle(
                Point(self.parser.center_x, self.parser.center_y),
                self.parser.radius
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["center"]["x"] ==  self.parser.center_x) &
            (Query()["center"]["y"] ==  self.parser.center_y) &
            (Query()["radius"] ==  self.parser.radius)
        )

    def show(self):
        print("Circles:", )
        print('\n'.join(str(Circle.deserialize(circle)) for circle in self.storage.all()))



class SquareService(FigureService):
    figure = 'square'

    def add(self):
        self.storage.insert(
            Square(
                Point( self.parser.left_top_x,  self.parser.left_top_y),
                self.parser.side_length,
                self.parser.angle
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["left_top"]["x"] ==  self.parser.left_top_x) &
            (Query()["left_top"]["y"] ==  self.parser.left_top_y) &
            (Query()["side_length"] ==  self.parser.side_length) &
            (Query()["angle"] ==  self.parser.angle)
        )

    def show(self):
        print("Squares:", )
        print('\n'.join(str(Square.deserialize(square)) for square in self.storage.all()))


class RectangleService(FigureService):
    figure = 'rectangle'

    def add(self):
        self.storage.insert(
            Rectangle(
                Point(self.parser.left_top_x,  self.parser.left_top_y),
                self.parser.right_side_length,
                self.parser.bottom_side_length,
                self.parser.angle
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["left_top"]["x"] ==  self.parser.left_top_x) &
            (Query()["left_top"]["y"] ==  self.parser.left_top_y) &
            (Query()["right_length"] ==  self.parser.right_side_length) &
            (Query()["bottom_length"] ==  self.parser.bottom_side_length) &
            (Query()["angle"] ==  self.parser.angle)
        )

    def show(self):
        print("Rectangles:", )
        print('\n'.join(str(Rectangle.deserialize(rectangle)) for rectangle in self.storage.all()))




class CommandExecutor:
    def __init__(self, parser, services_cls, resolvers_cls):
        self.parser = parser
        self.services_cls = services_cls
        self.resolver_cls = resolvers_cls


    def run(self):
        for resolver in self.resolver_cls:
            if self.parser.cmd == resolver.cmd:
                resolver(self.parser, self.services_cls).run()


CommandExecutor(parse_args,
                [PointService, SegmentService, CircleService, SquareService, RectangleService],
                [AddResolver, DeleteResolver, ShowResolver]).run()
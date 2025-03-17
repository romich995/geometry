import argparse

import tinydb
from tinydb import Query

from geometry import Point, Segment, Circle, Square
from resolvers import AddResolver, DeleteResolver, ShowResolver


def add_point_arguments(parser):
    parser.add_argument("x", type=float, help="x coordinate")
    parser.add_argument("y", type=float, help="y coordinate")


def add_square_arguments(parser):
    parser.add_argument("left_top_x", type=float, help="x coordinate of left top point")
    parser.add_argument("left_top_y", type=float, help="y coordinate of left top point")
    parser.add_argument("side_length", type=float,  help="side length")


def add_segment_arguments(parser):
    parser.add_argument("a_x", type=float, help="x coordinate of first Point")
    parser.add_argument("a_y", type=float, help="y coordinate of first Point")
    parser.add_argument("b_x", type=float, help="x coordinate of second Point")
    parser.add_argument("b_y", type=float, help="y coordinate of second Point")


def add_circle_arguments(parser):
    parser.add_argument("center_x", type=float, help="x coordinate of center")
    parser.add_argument("center_y", type=float, help="y coordinate of center")
    parser.add_argument("radius", type=float,  help="y coordinate of center")

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
                parse_args.x,
                parse_args.y
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["x"] == parse_args.x) &
            (Query()["y"] == parse_args.y)
        )

    def show(self):
        print("Points:",)
        print('\n'.join(str(Point.deserialize(point)) for point in self.storage.all()))


class SegmentService(FigureService):
    figure = 'segment'

    def add(self):
        self.storage.insert(
            Segment(
                Point(parse_args.a_x, parse_args.a_y),
                Point(parse_args.b_x, parse_args.b_y)
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["a"]["x"] == parse_args.a_x) &
            (Query()["a"]["y"] == parse_args.a_y) &
            (Query()["b"]["x"] == parse_args.b_x) &
            (Query()["b"]["y"] == parse_args.b_y)
        )

    def show(self):
        print("Segments:", )
        print('\n'.join(str(Segment.deserialize(segment)) for segment in self.storage.all()))


class CircleService(FigureService):
    figure = 'circle'

    def add(self):
        self.storage.insert(
            Circle(
                Point(parse_args.center_x, parse_args.center_y),
                parse_args.radius
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["center"]["x"] == parse_args.center_x) &
            (Query()["center"]["y"] == parse_args.center_y) &
            (Query()["radius"] == parse_args.radius)
        )

    def show(self):
        print("Circles:", )
        print('\n'.join(str(Circle.deserialize(circle)) for circle in self.storage.all()))



class SquareService(FigureService):
    figure = 'square'

    def add(self):
        self.storage.insert(
            Square(
                Point(parse_args.left_top_x, parse_args.left_top_y),
                parse_args.side_length
            ).serialize()
        )

    def delete(self):
        self.storage.remove(
            (Query()["left_top"]["x"] == parse_args.left_top_x) &
            (Query()["left_top"]["y"] == parse_args.left_top_y) &
            (Query()["side_length"] == parse_args.side_length)
        )

    def show(self):
        print("Squares:", )
        print('\n'.join(str(Square.deserialize(square)) for square in self.storage.all()))




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
                [PointService, SegmentService, CircleService, SquareService],
                [AddResolver, DeleteResolver, ShowResolver]).run()
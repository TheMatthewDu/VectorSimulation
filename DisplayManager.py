from __future__ import annotations
from typing import Tuple, List
from Vector import Vector
from DisplayVector import DisplayVector
from LinearTransformation import LinearTransformation


class DisplayManager:
    vectors: List[DisplayVector]

    def __init__(self, screen, colour: Tuple[float, float, float],
                 origin: Tuple[float, float],
                 spacing: float):
        self.screen = screen
        self.colour = colour
        self.origin_x = origin[0]
        self.origin_y = origin[1]
        self.spacing = spacing

        i_unit_vector = Vector((1, 0))
        j_unit_vector = Vector((0, 1))

        self.vectors = [
            DisplayVector(self.screen, self.cartesian_to_display_coordinates(1, 0), (self.origin_x, self.origin_y), (100,225,100), i_unit_vector),
            DisplayVector(self.screen, self.cartesian_to_display_coordinates(0, 1), (self.origin_x, self.origin_y), (100,225,100), j_unit_vector)
        ]

    def convert_to_display(self, vector: Vector):
        start = self.origin_x, self.origin_y
        end = self.cartesian_to_display_coordinates(vector.x, vector.y)
        return DisplayVector(self.screen, end, start, self.colour, vector)

    def cartesian_to_display_coordinates(self, x: float, y: float):
        return self.origin_x + x * self.spacing, \
               self.origin_y - y * self.spacing

    def display_all(self):
        for item in self.vectors:
            item.display()

    def move_to(self, transforamtion: LinearTransformation):
        for vector in self.vectors:
            new_vec = transforamtion.transform(vector.vector)
            first_x = new_vec.x
            first_y = new_vec.y
            new_x, new_y = self.cartesian_to_display_coordinates(first_x, first_y)
            speed = (vector.display_x - new_x) / 100, \
                    (vector.display_y - new_y) / 100
            vector.set_speed(speed)
            vector.move((new_x, new_y))

    def append(self, vector):
        self.vectors.append(self.convert_to_display(vector))


from __future__ import annotations
from typing import Tuple


class Vector:
    def __init__(self, position: Tuple[float, float]):
        self.x = position[0]
        self.y = position[1]

    def __mul__(self, other: int):
        first = self.x * other
        second = self.y * other
        return Vector((first, second))

    def __add__(self, other: Vector):
        return Vector((self.x + other.x, self.y + other.y))

    def __str__(self):
        return f'{self.x}, {self.y}'

    def get_position(self):
        return self.x, self.y


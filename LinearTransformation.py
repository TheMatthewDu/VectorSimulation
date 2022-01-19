from __future__ import annotations
from typing import List
from Vector import Vector

class Matrix:
    """
    |a|b|
    |c|d|
    """
    def __init__(self, elements: List[List[float]]):
        self.a = elements[0][0]
        self.b = elements[0][1]
        self.c = elements[1][0]
        self.d = elements[1][1]

    def __mul__(self, other: Vector):
        return Vector((self.a, self.c)) * other.x + Vector((self.b, self.d)) * other.y

    def __str__(self):
        return f"|{self.a}|{self.b}|\n|{self.c}|{self.d}|"


class LinearTransformation:
    def __init__(self, matrix: List[List[float]]):
        self.matrix = Matrix(matrix)

    def transform(self, vector: Vector):
        return self.matrix * vector

from __future__ import annotations
import pygame
from typing import Tuple
from Vector import Vector


class DisplayVector:
    def __init__(self, screen,
                 position: Tuple[float, float],
                 origin: Tuple[float, float],
                 colour: Tuple[float, float, float],
                 vector: Vector):
        self.screen = screen

        self.origin = origin
        self.display_x = position[0]
        self.display_y = position[1]

        self.x_speed = None
        self.y_speed = None

        self.colour = colour
        self.thickness = 10
        self.vector = vector

    def display(self):
        end = self.display_x, self.display_y
        pygame.draw.line(self.screen, self.colour, self.origin, end,
                         self.thickness)

    def set_speed(self, speed: Tuple[float, float]):
        self.x_speed = abs(speed[0])
        self.y_speed = abs(speed[1])

    def move(self, new: Tuple[float, float]) -> None:
        new_x, new_y = new[0], new[1]

        if new_x != self.display_x:
            if self.display_x > new_x:
                self.display_x -= self.x_speed
            else:
                self.display_x += self.x_speed

        if new_y != self.display_y:
            if self.display_y > new_y:
                self.display_y -= self.y_speed
            else:
                self.display_y += self.y_speed


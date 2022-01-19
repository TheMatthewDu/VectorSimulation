from __future__ import annotations
import pygame
import time
from DisplayManager import DisplayManager
from Vector import Vector
from LinearTransformation import LinearTransformation, Matrix
from math import sin, cos, radians


class Simulation:
    def __init__(self, space: int):
        # Setup the screen
        self.background_colour = (0, 0, 0)
        self.width = 1800
        self.height = 1000
        self.screen = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption('Vector_Math')
        self.screen.fill(self.background_colour)

        self.start_x = self.width // 2
        self.start_y = self.height // 2

        self.spacing = space
        self.y_axis = (self.width // 2, 0), \
                      (self.width // 2, self.height)
        self.x_axis = (0, self.height // 2), \
                      (self.width, self.height // 2)

        self.colour = (255, 255, 255)
        self.vector_colour = (100, 100, 255)

        self.display_manager = \
            DisplayManager(self.screen, self.vector_colour,
                           (self.start_x, self.start_y), self.spacing)

    def draw_axis(self):
        pygame.draw.line(self.screen, self.colour, self.y_axis[0], self.y_axis[1], 3)
        for i in range(- self.width // self.spacing, self.width // self.spacing, 2):
            next_start = ((self.width // 2) + self.spacing * i, 0)
            next_end = ((self.width // 2) + self.spacing * i, self.height)
            pygame.draw.line(self.screen, self.colour, next_start, next_end, 1)

        pygame.draw.line(self.screen, self.colour, self.x_axis[0], self.x_axis[1], 3)
        for i in range(- self.height // self.spacing, self.height // self.spacing, 2):
            next_start = (0, (self.height // 2) + self.spacing * i)
            next_end = (self.width, (self.height // 2) + self.spacing * i)
            pygame.draw.line(self.screen, self.colour, next_start, next_end, 1)

    def actions(self, transformation: LinearTransformation):
        self.display_manager.display_all()
        self.display_manager.move_to(transformation)

    def display(self, transformation: LinearTransformation):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.background_colour)

            self.draw_axis()
            self.actions(transformation)

            time.sleep(0.01)
            pygame.display.flip()

    def add_vector(self, vector: Vector):
        self.display_manager.append(vector)


# Main code
def main():
    simulation = Simulation(50)
    for i in range(-2, 3):
        for j in range(-2, 3):
            simulation.add_vector(Vector((i, j)))

    t = radians(30)
    matrix = [[cos(t), -5 * sin(t)],
              [5 * sin(t), cos(t)]]
    simulation.display(LinearTransformation(matrix))


if __name__ == '__main__':
    main()

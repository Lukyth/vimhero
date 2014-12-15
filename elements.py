import pygame
from pygame.locals import *
from random import randint

class Arrow(object):

    DIRECTION = ['up', 'down', 'left', 'right']

    def __init__(self, pos):
        (self.x, self.y) = pos
        self.change_direction()
        self.change_image()

    def render(self, surface):
        x = int(self.x) - (int(self.get_width()) / 2)
        y = int(self.y) - (int(self.get_height()) / 2)
        pos = (x, y)
        surface.blit(self.image, pos)

    def random_direction(self):
        return self.DIRECTION[randint(0, len(self.DIRECTION) - 1)]

    def get_image(self, direction):
        return pygame.image.load("img/" + direction + ".png")

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()

    def get_direction(self):
        return self.direction

    def change(self):
        self.change_direction()
        self.change_image()

    def change_direction(self):
        self.direction = self.random_direction()

    def change_image(self):
        self.image = self.get_image(self.direction)

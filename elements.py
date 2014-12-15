import pygame
from pygame.locals import *
from random import randint

class Arrow(object):

    DIRECTION = ['up', 'down', 'left', 'right']

    def __init__(self, pos):
        (self.x, self.y) = pos
        self.direction = self.random_direction()
        self.image = self.get_image(self.direction)

    def render(self, surface):
        pos = (int(self.x), int(self.y))
        surface.blit(self.image, pos)

    def random_direction(self):
        return self.DIRECTION[randint(0, len(self.DIRECTION) - 1)]

    def get_image(self, direction):
        return pygame.image.load("img/" + direction + ".png")

    def get_direction(self):
        return self.direction

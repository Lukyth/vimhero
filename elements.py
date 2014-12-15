import pygame
from pygame.locals import *

class Arrow(object):
    def __init__(self, pos):
        (self.x, self.y) = pos
        self.image = pygame.image.load("img/up.png")
        self.image.get_rect()
        

    def render(self, surface):
        pos = (int(self.x), int(self.y))
        surface.blit(self.image, pos)
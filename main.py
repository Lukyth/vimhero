import pygame
from pygame.locals import *

import gamelib
from elements import Arrow

class MainGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    
    def __init__(self):
        super(MainGame, self).__init__('VimHero', MainGame.BLACK)
        self.arrow = Arrow(pos = (self.window_size[0] / 2, self.window_size[1] / 2))
        self.score = 0

    def init(self):
        super(MainGame, self).init()
        self.render_score()

    def update(self):
        pass
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, MainGame.WHITE)

    def render(self, surface):
        self.arrow.render(surface)
        surface.blit(self.score_image, (10,10))

def main():
    game = MainGame()
    game.run()

if __name__ == '__main__':
    main()

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
        self.is_game_over = False

    def init(self):
        super(MainGame, self).init()
        self.render_score()

    def update(self):
        for event in pygame.event.get(KEYUP):
            if event.key == pygame.K_ESCAPE:
                self.terminate()
        if not self.is_game_over:
            for event in pygame.event.get(KEYUP):
                if event.key == pygame.K_h:
                    if self.arrow.get_direction() is 'left':
                        self.correct_key()
                    else:
                        self.game_over()
                elif event.key == pygame.K_j:
                    if self.arrow.get_direction() is 'up':
                        self.correct_key()
                    else:
                        self.game_over()
                elif event.key == pygame.K_k:
                    if self.arrow.get_direction() is 'down':
                        self.correct_key()
                    else:
                        self.game_over()
                elif event.key == pygame.K_l:
                    if self.arrow.get_direction() is 'right':
                        self.correct_key()
                    else:
                        self.game_over()
        else:
            for event in pygame.event.get(KEYUP):
                if event.key == pygame.K_SPACE:
                    self.score = -1
                    self.correct_key()
                    self.is_game_over = False


    def correct_key(self):
        self.arrow.change()
        self.score += 1
        self.render_score()

    def game_over(self):
        self.is_game_over = True
        
    def reset_game(self):
        self.score = 0
        self.is_game_over = False

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

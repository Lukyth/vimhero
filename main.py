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
        self.init_game()

    def init(self):
        super(MainGame, self).init()

    def init_game(self):
        self.score = 0
        self.arrow.change()
        self.is_game_over = False

    def update(self):
        self.check_key()

    def check_key(self):
        for event in pygame.event.get(KEYUP):
            self.check_key_exit(event)
            if not self.is_game_over:
                self.check_key_direction(event)
            else:
                self.check_key_reset(event)

    def check_key_exit(self, event):
        if event.key == pygame.K_ESCAPE:
            self.terminate()

    def check_key_direction(self, event):
        if event.key == pygame.K_h:
            self.check_direction('left')
        elif event.key == pygame.K_j:
            self.check_direction('up')
        elif event.key == pygame.K_k:
            self.check_direction('down')
        elif event.key == pygame.K_l:
            self.check_direction('right')

    def check_direction(self, direction):
        if self.arrow.get_direction() is direction:
                self.correct_key()
        else:
            self.game_over()

    def check_key_reset(self, event):
        if event.key == pygame.K_SPACE:
            self.reset_game()

    def correct_key(self):
        self.arrow.change()
        self.score += 1

    def game_over(self):
        self.is_game_over = True
        
    def reset_game(self):
        self.init_game()

    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, MainGame.WHITE)

    def render(self, surface):
        self.arrow.render(surface)
        self.render_score()
        surface.blit(self.score_image, (10,10))

def main():
    game = MainGame()
    game.run()

if __name__ == '__main__':
    main()

import pygame
from pygame.locals import *

import gamelib
from elements import Arrow

class MainGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    SECOND = 1000
    
    def __init__(self):
        super(MainGame, self).__init__('VimHero', MainGame.BLACK)
        self.arrow = Arrow(pos = (self.window_size[0] / 2, self.window_size[1] / 2))
        self.init_game()

    def init(self):
        super(MainGame, self).init()

    def init_game(self):
        self.score = 0
        self.arrow.change()
        self.time_limit = 2 * MainGame.SECOND
        self.time_decrease = 50
        self.is_started = False
        self.is_game_over = False

    def update(self):
        if self.is_started and not self.is_game_over:
            if self.is_over_time():
                self.game_over()
        self.check_key()

    def is_over_time(self):
        if self.get_time() - self.time > self.time_limit:
            return True
        return False

    def get_time(self):
        return pygame.time.get_ticks()

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
        if not self.is_started:
            self.is_started = True
        if self.arrow.get_direction() is direction:
                self.correct_key()
        else:
            self.game_over()

    def check_key_reset(self, event):
        if event.key == pygame.K_SPACE:
            self.reset_game()

    def correct_key(self):
        self.time_limit -= self.time_decrease
        self.set_time()
        self.arrow.change()
        self.score += 1

    def set_time(self):
        self.time = pygame.time.get_ticks()

    def game_over(self):
        self.is_game_over = True
        
    def reset_game(self):
        self.is_started = False
        self.init_game()

    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, MainGame.WHITE)
        self.set_score_position()

    def set_score_position(self):
        self.score_pos_x = (self.window_size[0] / 2) - (self.score_image.get_width() / 2)
        if not self.is_game_over:
            self.score_pos_y = (self.window_size[1] / 10) - (self.score_image.get_height() / 2)
        else:
            self.score_pos_y = (self.window_size[1] / 2) - (self.score_image.get_height() / 2)

    def render(self, surface):
        self.render_score()
        surface.blit(self.score_image, (self.score_pos_x, self.score_pos_y))
        if not self.is_game_over:
            self.arrow.render(surface)

def main():
    game = MainGame()
    game.run()

if __name__ == '__main__':
    main()

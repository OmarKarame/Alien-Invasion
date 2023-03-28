import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        # Bullet settings
        self.bulllet_speed = 3.0
        self.bullet_height = 12
        self.bullet_width = 3
        self.bullet_color = (250, 10, 10)

        self.rect = pygame.Rect(0, 0, self.bullet_width, self.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        self.y = float(self.rect.y)


    def update(self):
        self.y -= self.bulllet_speed
        self.rect.y = self.y
        

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)

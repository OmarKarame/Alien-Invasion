import pygame
import os


class Ship:
    IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship.png'))
    RESIZED_IMAGE = pygame.transform.scale(IMAGE, (40, 80))

    SPEED = 8

    moving_right = False
    moving_left = False

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.game_width = ai_game.WIDTH

        self.image = self.RESIZED_IMAGE
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.x + self.RESIZED_IMAGE.get_width() < self.game_width:
            self.rect.x += self.SPEED
        elif self.moving_left and self.rect.x > self.screen_rect.x:
            self.rect.x -= self.SPEED

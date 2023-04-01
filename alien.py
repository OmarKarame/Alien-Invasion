import pygame
import os

from pygame.sprite import Sprite


class Alien(Sprite):
    # Add new alien spaceship image to the assets folder 
    # The alien spaceship is not being loaded in the alien invasion file
    IMAGE = pygame.image.load(os.path.join('Assets', 'UFO.png'))
    RESIZED_IMAGE = pygame.transform.scale(IMAGE, (44, 30))

    SPEED = 1
    DROP_SPEED = 10

    fleet_direction = 1
    
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = self.RESIZED_IMAGE
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def update(self): 
        self.x += (self.SPEED * self.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right and self.fleet_direction > 0 or self.rect.left <= 0 and self.fleet_direction < 0:
            return True
        return False

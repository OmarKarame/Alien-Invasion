import sys
import pygame
import os
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:

    HEIGHT, WIDTH = 800, 500
    SPACE_BG = pygame.image.load(os.path.join('Assets', 'space_bg.jpg'))
    RESIZED_BG = pygame.transform.scale(SPACE_BG, (WIDTH, HEIGHT))
    TITLE = "Alien Invasion"

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.bg_color = (255, 255, 255)
        self.FPS = 60

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.create_fleet()


    def draw_window(self): 
        self.screen.fill(self.bg_color)
        self.blitme()
        self.ship.blitme()
        self.ship.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom > 0:
                bullet.draw_bullet()
                bullet.update()
            else:
                self.bullets.remove(bullet)

        self.aliens.draw(self.screen)
        pygame.display.update()




    # can move if else statements to separate class and using the strategy design pattern we can dynamically switch
    # between each movement
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                elif event.key == pygame.K_UP:
                    self._fire_bullet()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False


    def _fire_bullet(self):
        if len(self.bullets) < self.ship.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def create_fleet(self):
        alien = Alien(self)
        alien_width = alien.rect.width
        available_space_x = self.WIDTH - (2 * alien_width - 30)
        number_aliens_x = available_space_x // (2 * alien_width)

        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)



    def _create_alien(self, alien_number):
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def run_game(self):
        is_running = True
        clock = pygame.time.Clock()

        while is_running:
            clock.tick(self.FPS)
            self.check_events()
            self.draw_window()
            pygame.display.flip()

        pygame.quit()

    def blitme(self):
        self.screen.blit(self.RESIZED_BG, self.RESIZED_BG.get_rect())

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


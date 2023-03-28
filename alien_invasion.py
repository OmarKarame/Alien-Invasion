import sys
import pygame
from ship import Ship
from bullet import Bullet


class AlienInvasion:

    HEIGHT, WIDTH = 800, 600
    TITLE = "Alien Invasion"

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption(self.TITLE)
        self.bg_color = (255, 255, 255)
        self.FPS = 60

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()


    def draw_window(self):
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        self.ship.update()
        for bullet in self.bullets.sprites():
            if bullet.rect.bottom > 0:
                bullet.draw_bullet()
                bullet.update()
            else:
                self.bullets.remove(bullet)
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


    def run_game(self):
        is_running = True
        clock = pygame.time.Clock()

        while is_running:
            clock.tick(self.FPS)
            self.check_events()
            self.draw_window()
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


class GameStats:

    def __init__(self, ai_game):
        self.ship = ai_game.ship
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.ship.ship_limit
import pygame 
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship"""
    def __init__(self, ai_game):
        """Create a ship object from ship's current location"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.bullet_color

class Settings:
    """A class to store all settings of Alien Invasion."""

    def __init__(self):
        """Initilize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 500
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1

        # Bullet settins 
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
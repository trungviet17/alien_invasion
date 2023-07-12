import pygame 
from pygame.sprite import Sprite 

class Bullet(Sprite) : 
    """A class to manage bullets fired from the ship """

    def __init__(self, ai_game) : 
        """create a bullet object at the ship's current position """
        super().__init__()
        self.screen = ai_game.screen 
        self.setting = ai_game.setting
        self.color = self.setting.bullet_color

        self.rect = pygame.Rect(0, 0, self.setting.bullet_width, self.setting.bullet_height)

        # make the bullet emerge from the top of the ship 
        self.rect.midtop = ai_game.ship.rect.midtop 

        self.y = float(self.rect.y)

    def update(self) :
        """Move the bullet up the screen"""
        self.y -= self.setting.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self) : 
        """Draw the bullet to the sreen """
        pygame.draw.rect(self.screen, self.color, self.rect)
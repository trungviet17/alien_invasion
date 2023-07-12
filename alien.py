import pygame
from pygame.sprite import Sprite 

class Alien(Sprite) : 
    def __init__(self, ai_game) :
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        #load image 
        self.image = pygame.image.load('Alien_game\\alien.bmp')  
        self.rect = self.image.get_rect()

        # start each new alien near the top of scene 
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the alien's exact horizontal position 
        self.x = float(self.rect.x)
        self.setting = ai_game.setting
    
    def update(self) : 
        self.x += (self.setting.alien_speed * self.setting.alien_direction) 
        self.rect.x = self.x 
        

    def check_edges(self) : 
        if (self.rect.right >= self.screen_rect.right or self.rect.left <= 0) : 
            return True 
        return False
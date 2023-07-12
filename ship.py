import pygame 

class Ship: 
    """A class to manage the ship"""

    def __init__(self, ai_game) : 
        """Init the ship and set its starting position"""
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        #load the ship image and get its rect
        self.image = pygame.image.load('Alien_game\ship.bmp')

        # acces the ship's surface rect attribute
        self.rect = self.image.get_rect()

        # set rect  
        self.rect.midbottom = self.screen_rect.midbottom

        # movement flag 
        self.moving_right = False
        self.moving_left = False 

        #setting 
        self.setting = ai_game.setting
        self.x = float(self.rect.x)
    
    def update(self) : 
        """Update ship's position """
        if self.moving_right and self.rect.right < self.screen_rect.right : 
            self.x += self.setting.ship_speed
        if self.moving_left and self.rect.left > 0 : 
            self.x -= self.setting.ship_speed
        
        self.rect.x = self.x

    def blitme(self) : 
        """Draw the ship at current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self) : 
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
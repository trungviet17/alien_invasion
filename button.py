import pygame.font 

class Button : 
    def __init__(self, ai_game, msg) : 
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect() 

        #Set the dimensions and properties of the button
        self.width, self.height = 200, 50 
        self.button_color = (0, 14, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        #build the button rect 
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self._prep_mgs(msg)

    def _prep_mgs(self, msg) : 
        # boolean in font.render is on or off 
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)
        # get text center 
        self.msg_img_rect = self.msg_img.get_rect()
        self.msg_img_rect.center = self.rect.center
    
    def draw_button(self) :
        # draw the button 
        self.screen.fill(self.button_color, self.rect)
        # draw text 
        self.screen.blit(self.msg_img, self.msg_img_rect) 
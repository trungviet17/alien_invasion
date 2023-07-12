import pygame.font 

class Aboard : 
    """A class to report score or lever or live"""

    def __init__(self, ai_game) : 
        self.screen = ai_game.screen 
        self.screen_rect = self.screen.get_rect()
        self.setting = ai_game.setting 
        self.start = ai_game.start

        # front game information 
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_level()
        self.prep_limit()
    
    def prep_score(self) : 
        """Turn score into a rendered image"""
        score_str = 'Score: ' +  str(self.start.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.setting.bg_color)

        #Display the score at the top right 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20 
    
    def prep_level(self) : 
        level_str = 'Level: ' + str(self.start.level)
        self.level_image = self.font.render(level_str, True, self.text_color, self.setting.bg_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.midtop = self.screen_rect.midtop 
        self.level_rect.top = 20

    def prep_limit(self) : 
        live_str = 'Live: ' + str(self.start.ships_left + 1)
        self.live_image = self.font.render(live_str, True, self.text_color, self.setting.bg_color)
        self.live_rect = self.live_image.get_rect()
        self.live_rect.left = self.screen_rect.left + 20 
        self.live_rect.top = 20

    def showing(self) : 
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.live_image, self.live_rect)

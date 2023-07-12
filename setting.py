class Setting : 
    """A class to store all settings for Alien Invasion"""

    def __init__(self) : 
        """ Init the game's setting"""
        #screen setting 
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        #ship setting 
        self.ship_speed = 1.0
        self.ship_limit = 2

        #bullet setting 
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_limit = 3

        # alien 
        self.origin_setting()

        

    def origin_setting(self): 
        self.alien_speed = 0.3
        self.alien_direction = 1
        self.alien_drop = 10
        self.alien_score = 50

    def level_up(self) : 
        self.alien_speed += 0.1
        self.alien_direction += 0.2
        self.alien_drop += 5
        self.alien_score += 10


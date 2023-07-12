class Gamestart: 
    def __init__(self, ai_game) : 

        self.setting = ai_game.setting
        self.reset_state()
        self.game_state = False
        
    
    def reset_state(self) : 
        self.ships_left = self.setting.ship_limit
        self.score = 0 
        self.level = 1
    
        

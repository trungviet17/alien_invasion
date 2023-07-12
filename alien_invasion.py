# TODO : create pygame window and responding to user input

import sys, pygame
from setting import Setting
from ship import Ship
from bullet import Bullet
from alien import Alien
from  time import sleep 
from game_start import Gamestart
from button import Button
from aboard import Aboard 

class AlienInvasion : 
    """ Overall class to manage game assets and behaviour"""

    def __init__(self) : 
        pygame.init() #init the game 

        self.setting = Setting()
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height)) # set size window game 
        pygame.display.set_caption("Alien Invasion")
        # init ship 
        self.ship = Ship(self)

        # group bullets 
        self.bullets = pygame.sprite.Group()

        #group ailen and create aliens
        self.aliens = pygame.sprite.Group()
        self.creat_feelt()

        #create game start 
        self.start = Gamestart(self)

        self.button = Button(self, 'play')  

        #Create level 
        
        
        self.aboard = Aboard(self)

        
    
    def run_game(self) : 
        """Game loop """
        while True : 
            # watch for keyboard and mouse events 
            self._check_events()
            if (self.start.game_state) :
                self.ship.update()
                self.bullets.update()

                self._update_bullet()
                self.update_ailen()

            self._update_screen()

    # TODO : help method's run_game
    def _check_events(self) : 
        """Respond to keypress and mouse events"""
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT : sys.exit()
            elif event.type == pygame.KEYDOWN : 
                self._check_key_down(event)

            elif event.type == pygame.KEYUP : 
                self._check_key_up(event)
            elif event.type == pygame.MOUSEBUTTONDOWN : 
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)

    # Checking 
    def _check_key_down(self, event) : 
        if event.key == pygame.K_RIGHT: 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT: 
            self.ship.moving_left = True
        elif event.key == pygame.K_q : 
            sys.exit()
        elif event.key == pygame.K_SPACE :
            self.bullet_fire()
    
    def _check_key_up(self, event) :
        if event.key == pygame.K_RIGHT : 
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT :
            self.ship.moving_left = False
        elif event.key == pygame.K_q : 
            sys.exit()

    def bullet_fire(self) : 
        if (len(self.bullets) < self.setting.bullet_limit) : 
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    # creat alien
    def creat_feelt(self) : 
        _alien = Alien(self)
        alien_w = _alien.rect.width
        alien_h = _alien.rect.height
        # calulate nums x 
        avai_space_x = self.setting.screen_width - (2 * alien_w) 
        numx = avai_space_x // (2 * alien_w)

        # caculate nums y 
        avai_space_y = self.setting.screen_height - (3 * alien_h) - self.ship.rect.height
        numy = avai_space_y // (2 * alien_h)
        
        for num in range(numx) :
            for num2 in range(numy) : 
                self.creat_alien(num, num2)

    def creat_alien(self, alien_num, row) : 
        alien = Alien(self)
        alien_w , alien_h = alien.rect.size
        alien.x = alien_w + 2 * alien_w * alien_num
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row
        alien.rect.x = alien.x
        self.aliens.add(alien)

    def update_ailen(self) :
        self.check_fleet_edges() 
        self.aliens.update()
        # look for any member of group that has collided 
        if pygame.sprite.spritecollideany(self.ship, self.aliens) : 
            self.ship_hit()
        self.check_alien_bottom()

    def _update_screen(self) : 
        """Update images on the screen and flip to new screen"""

        #redraw the screen during each pass through the loop 
        self.screen.fill(self.setting.bg_color)

        #draw ship 
        self.ship.blitme()

        # create bullet 
        for bullet in self.bullets.sprites() : 
            bullet.draw_bullet()
        
        self.aliens.draw(self.screen)

        self.aboard.showing()

        if not self.start.game_state : 
            self.button.draw_button()

        # draw the most recently screen 
        pygame.display.flip()

    def _update_bullet(self) : 
        for bullet in self.bullets.copy() : 
            if (bullet.rect.y <= 0) : 
                self.bullets.remove(bullet)
        #check the bullets that have hit aliens 
        self.check_bullet_collisions()

    def check_bullet_collisions(self) : 
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, False, True)
        if collisions : 
            self.start.score += self.setting.alien_score
            self.aboard.prep_score()
            self.aboard.prep_level()
            
        if not self.aliens : 
            self.start.level += 1
            self.aboard.prep_level()
            self.setting.level_up()
            self.bullets.empty()
            self.creat_feelt()
            
           
    def check_fleet_edges(self) : 
        for alien in self.aliens.sprites() :
            if (alien.check_edges()) :
                self.change_direction() 
                break

    def change_direction(self) : 
        for alien in self.aliens.sprites() : 
            alien.rect.y += self.setting.alien_drop
        self.setting.alien_direction *= -1
                
    # Create new game 
    def ship_hit(self) : 
        if self.start.ships_left > 0 : 
            self.start.ships_left -= 1
            self.aboard.prep_limit()
            self.aliens.empty()
            self.bullets.empty()

            self.creat_feelt()
        else : 
            self.start.game_state = False
            self.setting.origin_setting()
            pygame.mouse.set_visible(True)

    def check_play_button(self, mouse_pos) :

        if self.button.rect.collidepoint(mouse_pos) and not self.start.game_state : 
            # reset game
            self.start.game_state = True
            self.start.reset_state()
            pygame.mouse.set_visible(False)

            # delete all element 
            self.aliens.empty()
            self.bullets.empty()

            # create new 
            self.creat_feelt()
            self.ship.center_ship()
            self.aboard.prep_score()
            self.aboard.prep_level()
    
    
    def check_alien_bottom (self) : 
        sceen_rect = self.screen.get_rect()
        for a in self.aliens.sprites() : 
            if (a.rect.bottom >= sceen_rect.bottom) : 
                self.ship_hit()
                break


# When run this condition is true - check if module as main 
if __name__ == '__main__' : 
    # Make a game instance and run game 
    ai = AlienInvasion()
    ai.run_game()
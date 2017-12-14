
import pygame

from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from bullet import Bullet
from pygame.sprite import Group

def run_game():
    #Intialize pygame,settings, and  screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make an Alien
    alien = Alien(ai_settings, screen)
    
    # Make a ship
    ship = Ship( ai_settings, screen)
    # Make a group to store bullets in
    bullets = Group()

    # Set the background color.
    bg_color = (230, 230, 230)

    # Start the main loop for the game.
    while True:
            gf.check_events(ai_settings, screen, ship, bullets)
            ship.update()
            gf.update_bullets(bullets)
            gf.update_aliens(aliens)
            gf.update_screen(ai_settings,screen, ship, alien, bullets)
            

            
            
            

            # Make the most recently drawn screen visible.
            pygame.display.flip()

            
            

            # Make the most recently drawn screen visible.
            pygame.display.flip()


run_game()


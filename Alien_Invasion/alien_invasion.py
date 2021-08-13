import sys
from settings import Settings
from ufo import Ufo
from alien import Alien
from pygame.sprite import Group
import pygame
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("星际大战")
    ufo: Ufo = Ufo(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, aliens)
    aliens = Alien(ai_settings, screen)
    while True:
        gf.check_events(ai_settings, screen, ufo, bullets)
        ufo.update()
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings, screen, ufo, bullets, aliens)
        ufo.blitme()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run_game()

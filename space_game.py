import pygame, control
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption("Galaxy Wars")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    ufo = Group()
    control.create_army(screen, ufo)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        control.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            control.update(bg_color, screen, stats, sc, gun, ufo, bullets)
            control.update_bullets(screen,stats, sc, ufo, bullets)
            control.update_ufos(stats, screen, sc, gun, ufo, bullets)


run()
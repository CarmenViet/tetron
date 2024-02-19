import pygame
from modules.intro import *
from modules.game import *

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

show_intro_screen(screen, clock)
show_game(screen, clock)
pygame.quit()

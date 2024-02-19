import pygame
import os
intro_image = pygame.image.load(os.path.join('Assets', 'tetron_intro.png'))
bunny = pygame.image.load(os.path.join('Assets', 'bunny.png'))
bunny = pygame.transform.scale(bunny, (170, 170))
play = pygame.image.load(os.path.join('Assets', 'play.png'))

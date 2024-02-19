import pygame
from modules.images import *

def show_intro_screen(screen, clock):
    screen.blit(intro_image,(0,0))
    pygame.display.update()
    user_has_clicked = False

    while user_has_clicked == False:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                #print(pos)
                if 1168 > pos[0] and pos[0] > 434 and 670 > pos[1] and pos[1] > 385:
                    user_has_clicked = True
            if event.type == pygame.QUIT:
                pygame.quit()

        clock.tick(60)
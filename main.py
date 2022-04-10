import pygame
import champion
from sys import exit

# General setup
pygame.init()
clock = pygame.time.Clock()
game_active = True

# Game Screen
screen_width = 800
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
background_surface = pygame.image.load('assets/images/background.png').convert()
ground_surface = pygame.image.load('assets/images/ground.png').convert()

# Fonts
text_font = pygame.font.Font("assets/fonts/megaman.ttf", 10)

strawberry = champion.Champion("Strawberry", 10, 3, 100, 300)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if game_active:
        screen.blit(background_surface, (0,0))
        screen.blit(ground_surface,(0,500))

        
        strawberry.update()
    else:
        screen.fill('Olive')
        score_message = text_font.render(f'Game end', False, "White")

    pygame.display.update() 
    clock.tick(60)

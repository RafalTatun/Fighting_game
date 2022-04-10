import pygame
import champion
from strawberry import Strawberry
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


# Champions

strawberry = pygame.sprite.GroupSingle()
strawberry.add(Strawberry('Strawberry', 5, 3, 200, 200))
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if game_active:
        screen.blit(background_surface, (0,0))
        screen.blit(ground_surface,(0,500))

        strawberry.draw(screen)
        strawberry.update()
    else:
        screen.fill('Olive')
        score_message = text_font.render(f'Game end', False, "White")

    pygame.display.update() 
    clock.tick(60)

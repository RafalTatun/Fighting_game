from champion import Champion
import pygame

class Strawberry(Champion):
    def __init__(self):
        self.player_walk = pygame.image.load('assets/images/sprite.png').convert_alpha()
        self.image = self.player_walk
        self.rect = self.image.get_rect(midbottom =(x_pos, y_pos))
    # Update champion
    def update(self):
        keys = pygame.key.get_pressed()
        self.moves(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d], None)
        #self.apply_gravity()
from champion import Champion
import pygame

class Strawberry(Champion):
    def __init__(self, name, attack, speed, x_pos, y_pos):
        super(Champion, self).__init__()
        pass
    # Update champion
    def update(self):
        keys = pygame.key.get_pressed()
        self.moves(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d], None)
        #self.apply_gravity()
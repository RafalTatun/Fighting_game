import pygame


class Champion(pygame.sprite.Sprite):
    def __init__(self, name, attack, speed, x_pos, y_pos):
        self.name = name
        self.health = 100
        self.attack = attack
        self.speed = speed
        self.gravity = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.player_walk = pygame.image.load(f'assets/images/{self.name}/sprite.png').convert_alpha()
        self.image = self.player_walk
        self.rect = self.image.get_rect(midbottom =(x_pos, y_pos))

    def moves(self, up, left, right, abilities):
        # Jump key
        if up and self.rect.bottom >= 500:
            self.gravity = -5

        # Move left key
        if left:
            self.rect.x -= self.speed
        
        # Move right key
        elif right:
            self.rect.x += self.speed

        # Superpower key
        if abilities:
            self.abilities()
    
    # Gravity
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 500:
            self.rect.bottom = 500

    # Superpower
    def abilities():
        pass
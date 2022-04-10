import pygame


class Champion(pygame.sprite.Sprite):
    def __init__(self, name, attack, speed, x_pos, y_pos):
        super().__init__()
        self.name = name
        self.health = 100
        self.attack = attack
        self.speed = speed
        self.gravity = 0
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.player_walk = pygame.image.load('assets/images/sprite.png').convert_alpha()
        self.image = self.player_walk
        self.rect = self.image.get_rect(midbottom =(x_pos, y_pos))


    def moves(self, up, left, right, abilities):
        keys = pygame.key.get_pressed()

        # Jump key
        if keys[pygame.up] and self.rect.bottom >= 500:
            self.gravity = -5

        # Move left key
        if keys[pygame.left]:
            self.rect.x += self.speed
        
        # Move right key
        elif keys[pygame.right]:
            self.rect.x -= self.speed

        # Superpower key
        if keys[pygame.abilities]:
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

    # Update champion
    def update(self):
        self.moves()
        self.apply_gravity()
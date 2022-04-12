import pygame
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

# Class Champions
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
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)

    def draw(self):
        screen.blit(self.image, self.rect)

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


# Strawberry character
class Strawberry(Champion):
    def __init__(self, name, attack, speed, x_pos, y_pos):
        pass
    # Update champion
    def update(self):
        keys = pygame.key.get_pressed()
        self.moves(keys[pygame.K_w], keys[pygame.K_a], keys[pygame.K_d], None)
        #self.apply_gravity()

# Champions creator
strawberry = Champion('Strawberry', 5, 3, 200, 200)
    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    if game_active:
        screen.blit(background_surface, (0,0))
        screen.blit(ground_surface,(0,500))

        strawberry.draw()
        strawberry.update()
    else:
        screen.fill('Olive')
        score_message = text_font.render(f'Game end', False, "White")

    pygame.display.update() 
    clock.tick(60)

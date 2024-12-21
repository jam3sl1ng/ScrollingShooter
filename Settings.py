import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60
GRAVITY = 0.75
# Colours
BG = (144, 201, 120)
RED = (255, 0,0)

# Groups
bullet_group = pygame.sprite.Group()
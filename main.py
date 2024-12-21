import pygame
import os
from Soldier import Soldier

pygame.init()

# Global consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60
GRAVITY = 0.75
# Colours
BG = (144, 201, 120)
RED = (255, 0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scrolling Shooter')

clock = pygame.time.Clock() # Allow FPS to be set manually

# Player action variables
moving_left = False
moving_right = False

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 200, 3, 5)

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.update_animation()
    player.draw(screen)

    if player.alive:
        if player.in_air:
            player.update_action(2) # Jump
        elif moving_left or moving_right:
            player.update_action(1) # Run
        else:
            player.update_action(0) # Idle
    
        player.move(moving_left, moving_right, GRAVITY)

    enemy.draw(screen)    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit game
            run = False

        if event.type == pygame.KEYDOWN: # Key presses
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False
        
        if event.type == pygame.KEYUP: # Key release
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    
    pygame.display.update()

pygame.quit()

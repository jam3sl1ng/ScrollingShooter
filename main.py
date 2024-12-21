import pygame
import os

from Soldier import Soldier
from Bullet import Bullet
from Settings import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scrolling Shooter')

clock = pygame.time.Clock() # Allow FPS to be set manually

# Player action variables
moving_left = False
moving_right = False
shoot = False

# Images
bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()

def draw_bg():
    screen.fill(BG)
    pygame.draw.line(screen, RED, (0, 300), (SCREEN_WIDTH, 300))

player = Soldier('player', 200, 200, 3, 5, 5)
enemy = Soldier('enemy', 400, 200, 3, 5, 5)

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.update()
    player.draw(screen)
    enemy.draw(screen)

    # Update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)

    if player.alive:
        if shoot:
            player.shoot(bullet_img)
        elif player.in_air:
            player.update_action(2) # Jump
        elif moving_left or moving_right:
            player.update_action(1) # Run
        else:
            player.update_action(0) # Idle
    
        player.move(moving_left, moving_right, GRAVITY)    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit game
            run = False

        if event.type == pygame.KEYDOWN: # Key presses
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_w:
                shoot = True
            if event.key == pygame.K_SPACE and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                run = False
        
        if event.type == pygame.KEYUP: # Key release
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_w:
                shoot = False
    
    pygame.display.update()

pygame.quit()

import pygame
import os

from Settings import *
from Bullet import Bullet

pygame.init()

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)

        self.alive = True
        self.health = 100
        self.max_health = self.health

        # Jumping + Moving + Shooting
        self.speed = speed
        self.jump = False
        self.vel_y = 0
        self.in_air = False
        self.update_time = pygame.time.get_ticks()
        self.shoot_cooldown = 0
        self.ammo = ammo
        self.start_ammo = ammo

        # Change direction if moving left or right
        self.direction = 1
        self.flip = False

        ################################
        ########## ANIMATIONS ##########
        ################################

        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        
        self.char_type = char_type

        animation_types = ['Idle', 'Run', 'Jump', 'Death'] # Load all images for the player

        for animation in animation_types:
            temp_list = [] # Reset temp list
            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}')) # Count number of files in the animation folder

            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
                temp_list.append(img)

            self.animation_list.append(temp_list)

        ################################
        ################################
        ################################

        self.image = self.animation_list[self.action][self.frame_index]

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        self.update_animation()
        self.check_alive()

        # Update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
    
    def move(self, moving_left, moving_right, gravity):
        # Reset moving variables
        dx = 0
        dy = 0

        # Assign moving variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        
        # Jump
        if self.jump and not self.in_air:
            self.vel_y = -11
            self.jump = False
            self.in_air = True

        # Gravity
        self.vel_y += gravity
        if self.vel_y > 10:
            self.vel_y
        dy += self.vel_y

        # Check collision with floor
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.in_air = False

        # Update rect position
        self.rect.x += dx
        self.rect.y += dy
    
    def shoot(self, bullet_img):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction, bullet_img)
            bullet_group.add(bullet)

            self.ammo -= 1 # Reduce ammo

    def update_animation(self):
        # Update animation
        ANIMATION_COOLDOWN = 100

        self.image = self.animation_list[self.action][self.frame_index] # Update image depending on current frame

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN: # Check if enough time has passed since last update
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        
        if self.frame_index >= len(self.animation_list[self.action]): # If the animation has finished reset it back to the start
            if self.action == 3:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action: # Check if new action is different to the previous one
            self.action = new_action
            # Update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()
    
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3) # Death

    def draw(self, screen):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)
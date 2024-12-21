import pygame
from Settings import *

pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction, bullet_img):
        pygame.sprite.Sprite.__init__(self)
        
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
    
    def update(self):
        # Move bullet
        self.rect.x += (self.direction * self.speed)
        
        # Check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
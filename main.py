import pygame

pygame.init()

# Global consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scrolling Shooter')

# Player action variables
moving_left = False
moving_right = False

class Soldier(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed

        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def draw(self, moving_left, moving_right):
        # Reset moving variables
        dx = 0
        dy = 0

        # Assign moving variables if moving left or right
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed

    def draw(self):
        screen.blit(self.image, self.rect)

player = Soldier(200, 200, 3, 5)

run = True
while run:

    player.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit game
            run = False

        if event.type == pygame.KEYDOWN: # Key presses
            if event.key == pygame.K_LEFT or pygame.K_a:
                moving_left = True
            if event.key == pygame.K_RIGHT or pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False
        
        if event.type == pygame.KEYUP: # Key release
            if event.key == pygame.K_LEFT or pygame.K_a:
                moving_left = False
            if event.key == pygame.K_RIGHT or pygame.K_d:
                moving_right = False
    
    pygame.display.update()

pygame.quit()

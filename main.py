import pygame

pygame.init()

# Global consts
SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)
FPS = 60
BG = (144, 201, 120)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Scrolling Shooter')

clock = pygame.time.Clock() # Allow FPS to be set manually

# Player action variables
moving_left = False
moving_right = False

def draw_bg():
    screen.fill(BG)

class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed

        # Change direction if moving left or right
        self.direction = 1
        self.flip = False

        img = pygame.image.load(f'img/{char_type}/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def move(self, moving_left, moving_right):
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

        # Update rect position
        self.rect.x += dx
        self.rect.y += dy

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 300, 3, 5)

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.draw()
    player.move(moving_left, moving_right)

    enemy.draw()    

    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Quit game
            run = False

        if event.type == pygame.KEYDOWN: # Key presses
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False
        
        if event.type == pygame.KEYUP: # Key release
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    
    pygame.display.update()

pygame.quit()

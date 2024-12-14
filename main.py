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
        self.update_time = pygame.time.get_ticks()

        # Change direction if moving left or right
        self.direction = 1
        self.flip = False

        # Soldier animations
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        
        ########## ACTION 0 ##########

        temp_list = []

        for i in range(5):
            img = pygame.image.load(f'img/{char_type}/Idle/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        ########## ACTION 1 ##########

        temp_list = []

        for i in range(6):
            img = pygame.image.load(f'img/{char_type}/Run/{i}.png')
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
            temp_list.append(img)

        self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]

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

    def update_animation(self):
        # Update animation
        ANIMATION_COOLDOWN = 100

        self.image = self.animation_list[self.action][self.frame_index] # Update image depending on current frame

        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN: # Check if enough time has passed since last update
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        
        if self.frame_index >= len(self.animation_list[self.action]): # If the animation has finished reset it back to the start
            self.frame_index = 0

    def update_action(self, new_action):
        if new_action != self.action: # Check if new action is different to the previous one
            self.action = new_action
            # Update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

player = Soldier('player', 200, 200, 3, 5)
enemy = Soldier('enemy', 400, 300, 3, 5)

run = True
while run:

    clock.tick(FPS)

    draw_bg()

    player.update_animation()
    player.draw()

    if moving_left or moving_right:
        player.update_action(1) # Run
    else:
        player.update_action(0) # Idle
    
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

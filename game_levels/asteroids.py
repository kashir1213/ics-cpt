import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (800, 600)
screen = pygame.display.set_mode(size)

# asteroidImage  = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/asteroid.png')

class makeAsteroid():
    def __init__(self):
        self.image = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/asteroid.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.width = random.randint(100, 500)
        self.height = random.randint(100, 500)

        self.posX = 700
        self.posY = 20

        self.moveX = random.randint(0,600) 
        self.moveY = random.randint(500,700)       

    def move(self):

        if self.posX > self.moveX:
            self.posX -= (self.moveX)/70
        if self.posY < self.moveY:
            self.posY += (self.moveY)/70
        
    def draw(self):
        asteroidImage = pygame.transform.scale(self.image, (self.width,self.height))
        screen.blit(asteroidImage, (self.posX,self.posY))


# pygame.init()
 
# # Set the width and height of the screen [width, height]

# x = makeAsteroid()
 
# pygame.display.set_caption("My Game")
 
# # Loop until the user clicks the close button.
# done = False
 
# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# while not done:
#     # --- Main event loop
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
 
#     # --- Game logic should go here
 
#     # --- Screen-clearing code goes here
    
    
#     # Here, we clear the screen to white. Don't put other drawing commands
#     # above this, or they will be erased with this command.
 
#     # If you want a background image, replace this clear with blit'ing the
#     # background image.
#     screen.fill(BLACK)
#     x.draw()
#     x.move()
 
#     # --- Drawing code should go here
 
#     # --- Go ahead and update the screen with what we've drawn.
#     pygame.display.flip()
 
#     # --- Limit to 60 frames per second
#     clock.tick(60)
 
# # Close the window and quit.
# pygame.quit()

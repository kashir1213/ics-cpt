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
        self.image = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/asteroid.png').convert_alpha()
        self.image = pygame.transform.flip(self.image, True, False)
        self.width = random.randint(100, 200)
        self.height = self.width

        self.posX = -100
        self.posY = -100

        self.rotation = 0

        self.imageRect = 0

        self.imageShow = True

        self.mask = None

    def move(self, toMove):
        moveX = toMove[0]
        moveY = toMove[1]
        
        if self.posX < moveX:
            self.posX -= (self.posX - moveX)/100
        if self.posY < moveY:
            self.posY += abs((self.posY - moveY)/100)
        
    def draw(self):
        if self.imageShow == True:
            asteroidImage = pygame.transform.scale(self.image, (self.width,self.height))
            asteroidImage = pygame.transform.rotate(asteroidImage, self.rotation)
            self.rotation += 20
            screen.blit(asteroidImage, (self.posX,self.posY))
            self.mask = pygame.mask.from_surface(asteroidImage)

    def delete(self):
        self.imageShow = False
    
        
        


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

## Kashir 
## Kevin

import pygame
import random

# Initialize Pygame
pygame.init()
size = (800, 600)
screen = pygame.display.set_mode(size)
class bottle():
    def __init__(self, posX, posYRange):
        self.image = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/waterBottle.png')
        self.width = 50
        self.heigth = 50
        self.showImage = True
        self.posX = posX
        self.posY = random.randint(posYRange[0], posYRange[1])

        self.mask = None
    
    def move(self):
        if self.posX > -100:
            self.posX -= 5 
    
    def delete (self):
        self.showImage = False


    def draw(self):
        if self.showImage == True:
            image = pygame.transform.scale(self.image, (self.width, self.heigth))
            screen.blit(image, (self.posX, self.posY))
            self.mask = pygame.mask.from_surface(image)


# a = waterBottle(700, (100, 200))

# # Set up the drawing window


# pygame.display.set_caption("My Animation")
#  # RGBA color

# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()

# # Colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# BROWN = (153, 76, 0)
# GREY = (96, 96, 96)
# YELLOW = (255, 255, 0)
# DARKGREEN = (0, 51, 0)
# ORANGE = (255,128,0)


# # Main Program Loop
# while not done:
#     # Event handling
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     # Fill the screen with black
#     screen.fill((0, 0, 0))

#     # Blit the semi-transparent overlay
#     a.move()
#     a.draw()

 
#     # Draw a black rectangle (ground)
#     pygame.draw.rect(screen, BROWN, [0, 400, 800, 200])

#     # Update the display
#     pygame.display.flip()

#     # Limit frames per second
#     clock.tick(60)

# # Quit Pygame
# pygame.quit()



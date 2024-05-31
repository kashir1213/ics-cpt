# Drawings
# Kevin Tuiza

import pygame
import random

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

# Items to keep player alive
class boxes:
    def __init__(self):
        self.x = random.randint(0,100)

        self.y = random.randint(0,100)
    
    def drawBox(self):
        pygame.draw.rect(screen,BROWN,[self.x,self.y,50,50])
        pygame.draw.ellipse(screen,BLUE,[15+self.x,12+self.y,20,20])


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Update Screen
pygame.display.flip()
clock.tick(60)



# Colours
BROWN = (110,60,11)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (153,76,0)
GREY = (96,96,96)
YELLOW = (255,255,0)
DARKGREEN = (0,51,0)



    

## Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)
    summon = random.randint(0,10)
    #need to change
    theboxes = boxes()
    if summon == 5:
        theboxes.drawBox()
        
    # Update Screen
    pygame.display.flip()
    clock.tick(60)
# Close the window and quit
pygame.quit()
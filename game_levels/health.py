# Drawings
# Kevin Tuiza

import pygame
import random

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")

# Items to keep player alive
class healthbar:
    def __init__(self, health):
        self.x = 0
        self.y = 0

        self.length = health
        self.width = 30
    
    def drawHealth(self):
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(self.x, self.y, self.length, self.width), 15,5)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x, self.y, 202, self.width +2), 2, 5)

class dehydration:
    def __init__(self, hydration):
        self.x = 0
        self.y = 50

        self.length = hydration
        self.width = 30

    def drawHydration(self):
        pygame.draw.rect(screen, (52, 168, 235), pygame.Rect(self.x, self.y, self.length, self.width), 15,5)
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x, self.y, 202, self.width +2), 2, 5)

        


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
start_ticks = pygame.time.get_ticks()
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


#summon boxes at random locations
    
x = healthbar(200)
z = dehydration(200)
# Main Program Loop
while not done:
    ## CONTROL
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)
    
    
    y = random.randint(1, 10)
    if y == 5:
        x.length -= 1
    x.drawHealth()
    

    seconds = (pygame.time.get_ticks()-start_ticks)/1000
    print(seconds)

    if seconds%1 == 0:
        z.length -= 1
    z.drawHydration()
    # Update Screen
    pygame.display.flip()
    clock.tick(60)
    
# Close the window and quit
pygame.quit()

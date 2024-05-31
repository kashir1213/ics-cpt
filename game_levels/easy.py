import pygame

# Initialize Pygame
pygame.init()

# Set up the drawing window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Animation")

# Create a surface with 
overlay = pygame.Surface((800, 600), pygame.SRCALPHA)
overlay.fill((153, 76, 0, 50))  # RGBA color

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# x = makeAsteroid()
# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (153, 76, 0)
GREY = (96, 96, 96)
YELLOW = (255, 255, 0)
DARKGREEN = (0, 51, 0)


backgroundImage = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/background.png')
transformedBack = pygame.transform.scale(backgroundImage, (800,600))

width = 600
i = 0
# Main Program Loop
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # # Fill the screen with black
    # screen.fill((0xff, 0xff, 0xff))


    #moving background
    screen.fill((0,0,0))
    screen.blit(transformedBack, (i,0))
    screen.blit(transformedBack,(width+i,0))

    if i == -width:
        screen.blit(transformedBack,(width+i,0))
        i = 0
    i -= 1

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()




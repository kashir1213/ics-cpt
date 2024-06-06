## Sounds
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

# Test sounds in characters death
death_sound = pygame.mixer.Sound("Wake_tf_up.mp3")


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
    
    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(200)

# Quit Pygame
pygame.quit()
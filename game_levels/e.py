import people
import waterbottle
import pygame




# Initialize Pygame
pygame.init()

# Set up the drawing window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Animation")
x = waterbottle.bottle()
y = people.mainCharacter()


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
ORANGE = (255,128,0)


# Main Program Loop
while not done:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Blit the semi-transparent overlay
    x.draw()
    y.draw()
 
    # Draw a black rectangle (ground)
    pygame.draw.rect(screen, BROWN, [0, 400, 800, 200])

    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Quit Pygame
pygame.quit()



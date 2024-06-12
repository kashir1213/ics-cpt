import pygame
from game_levels import easy

# Initialize Pygame
pygame.init()

# Set up the drawing window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Animation")

done = False
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
BROWN = (153, 76, 0)

# Main Program Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(BLACK)

    easy.game1(screen)

    pygame.draw.rect(screen, BROWN, [0, 400, 800, 200])

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

## Easy mode

import pygame
import asteroids
import people 


# Initialize Pygame
pygame.init()

# Set up the drawing window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Animation")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



backgroundImage = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/background.png').convert()
transformedBack = pygame.transform.scale(backgroundImage, (800,600))
tiles = (size[1]/600) + 2
scroll = 0
asteroids_list = []
asteroid_cooldown = 0
asteroidPresent = False
i = 1
mc = people.mainCharacter(100, 450, (-20, 350, 700, 530))

# Main Program Loop


while not done:
    asteroid_summoned = False
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    #moving background
    for j in range(0, int(tiles)):
        screen.blit(transformedBack, (j * 600 + scroll,0))
    
    scroll -= 5

    if abs(scroll) > 600:
        scroll = 0


    mc.draw()
    mc.anim()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        mc.move('L') 
    if keys[pygame.K_d]:
        mc.move('R')
    if keys[pygame.K_w]:
        mc.move('U')
    if keys[pygame.K_s]:
        mc.move('D')

    
    
    if asteroid_cooldown <= 0 and (i % 2 == 0) and len(asteroids_list) < 1:
        new_asteroid = asteroids.makeAsteroid()
        asteroids_list.append(new_asteroid)
        asteroid_cooldown = 100  # Reset cooldown timer (adjust as needed)

    # Decrease cooldown timer
    asteroid_cooldown -= 1

    for asteroid in asteroids_list:
        if (asteroid.posX == mc.x or asteroid.posX == 0) and (asteroid.posY == mc.y or asteroid.posY == 0):
            asteroid.move((mc.x, mc.y))
        
        if asteroid.posX == mc.x and asteroid.posY == mc.y:
            asteroids_list = []
            
        asteroid.draw()
    i += 1
    # Update the display
    pygame.display.flip()

    # Limit frames per second
    clock.tick(120)

# Quit Pygame
pygame.quit()




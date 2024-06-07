## Easy mode

import pygame
import asteroids
import people 
import random
import health
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

asteroidPresent = False
mc = people.mainCharacter(100, 450, (-20, 350, 700, 530))

# Main Program Loop
newAsteroid = asteroids.makeAsteroid()
mcHealth = health.healthbar(200)

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

    
    if newAsteroid.posY < 650 and newAsteroid.posY > -200:
        asteroidPresent = True
    else: 
        asteroidPresent = False
    
    if asteroidPresent == False:
        num = random.randint(0, 100)
        if num%10 == 0:
            newAsteroid = asteroids.makeAsteroid() 
            newAsteroid.draw()
            newAsteroid.move((mc.x + newAsteroid.height, 700))
    else:
        pos = mc.x+ newAsteroid.height
        if mc.x < 0:
            pos = mc.x
        newAsteroid.draw()
        newAsteroid.move((pos, 700))

    
    mcRect = mc.returnRect()
    asteroidRect = newAsteroid.returnRect()
    collide = collide = mcRect.colliderect(asteroidRect)

    if collide:
        print('yes')
    # Update the display
    pygame.display.flip()

    # Limit fr  ames per second
    clock.tick(120)

# Quit Pygame
pygame.quit()




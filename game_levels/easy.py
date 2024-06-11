## Easy mode

import pygame
import asteroids
import people 
import random
import health
import waterbottle

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
start_ticks = pygame.time.get_ticks()
asteroidPresent = False
mc = people.mainCharacter(100, 450, (-20, 350, 700, 530))

# Main Program Loop
newAsteroid = asteroids.makeAsteroid()
healthNum = 200
hydrate = 200
wata = waterbottle.bottle(700,(350, 530))
waterPresent = False
waterCollected = False

collision = None
toMove =()
movementPos = []

touched = False
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
    if (newAsteroid.posY < (mc.y-100) and newAsteroid.posY > -100) or asteroidPresent == True:
        asteroidPresent = True
    else: 
        asteroidPresent = False
    
    
    if asteroidPresent == False:
        num = random.randint(0, 500)
        if num%2 == 0:
            movementPos.clear()
            newAsteroid = asteroids.makeAsteroid() 
            newAsteroid.draw()
            toMove = (mc.x + newAsteroid.height,mc.y)
            movementPos.append((toMove[0], toMove[1]))
            newAsteroid.move((toMove[0], toMove[1]))
            collision = newAsteroid.mask.overlap(mc.mask,((newAsteroid.posX + newAsteroid.height) - (mc.x+100), (newAsteroid.posY + newAsteroid.height)- (mc.y+100)))
            touched = False
            
    else:
        if len(movementPos) != 0:
            # print(True)
            if mc.x < 0:
                toMove = mc.x
            newAsteroid.draw()
            newAsteroid.move((movementPos[0][0], movementPos[0][1]))

            if newAsteroid.posX +20 >= movementPos[0][0]:
                newAsteroid.delete()
                asteroidPresent = False 
            
            collision = newAsteroid.mask.overlap(mc.mask,((newAsteroid.posX + newAsteroid.height) - (mc.x+100), (newAsteroid.posY + newAsteroid.height)- (mc.y+100)))
    
            
        seconds = round((pygame.time.get_ticks()-start_ticks)/1000,2)
        if round(seconds%1, 1) == 0:
            hydrate -= 1
        mcHydration = health.dehydration(hydrate)
        mcHydration.drawHydration()


    if waterPresent == False:
        wata = waterbottle.bottle(700,(350, 530))
        wata.move()
        wata.draw()
        waterPresent = True
        waterCollected = False
    else:
        wata.move()
        wata.draw()
        waterCollected = False
    
    if waterPresent == True and wata.posX <= -10:
        waterPresent = False

   

    collisonX = (abs((wata.heigth + wata.posX) - (mc.x + 100))) <= 40
    collisonY = (abs((wata.width + wata.posY) - (mc.y + 100))) <= 40

   
    if collisonX and collisonY:
        

        while waterCollected == False:
            wata.delete()
            if hydrate < 200:
                print(hydrate)
                hydrate += 0.5
                if hydrate > 200:
                    hydrate = 200
                print('\n')
            waterCollected = True

    if hydrate <=0:
        hydrate = 0
        healthNum -= 0.01
           

    #(wata.heigth + wata.posX) - mc.x + 100 <= 20 and 
    if collision:
        if touched == False:
            healthNum -=10
            touched = True
            newAsteroid.delete()
    mcHealth = health.healthbar(healthNum)
    mcHealth.drawHealth()
    
    
    # Update the display
    pygame.display.flip()

    # Limit fr  ames per second
    clock.tick(120)

# Quit Pygame
pygame.quit()




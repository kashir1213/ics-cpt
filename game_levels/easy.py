## Easy mode

import pygame
from . import asteroids
from . import people 
import random
from . import health
from . import waterbottle

# Initialize Pygame
pygame.init()

# Set up the drawing window
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Animation")


def game1():
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    #background
    backgroundImage = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/background.png').convert()
    transformedBack = pygame.transform.scale(backgroundImage, (800,600))

    #moving background
    tiles = (size[1]/600) + 2
    scroll = 0

    #main character
    mainCharacter = people.mainCharacter(100, 450, (-20, 350, 700, 530))
    start = pygame.time.get_ticks()
    
    #asteroid config
    asteroid = asteroids.makeAsteroid()
    asteroidPresent = False
    movementPos = []
    
    #health bar and hydration     
    healthNum = 200
    hydrate = 200
    water = waterbottle.bottle(700,(350, 530))
    waterPresent = False
    waterCollected = False

    collision = None
    toMove =()
    

    touched = False

    
    while not done:
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

        #draw main character
        mainCharacter.draw()
        mainCharacter.anim()

        #movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            mainCharacter.move('L') 
        if keys[pygame.K_d]:
            mainCharacter.move('R')
        if keys[pygame.K_w]:
            mainCharacter.move('U')
        if keys[pygame.K_s]:
            mainCharacter.move('D')
        
        #asteroid moving 
        
        if (asteroid.posY < (mainCharacter.y-100) and asteroid.posY > -100) or asteroidPresent == True:
            asteroidPresent = True
        else: 
            asteroidPresent = False
        
        
        if asteroidPresent == False:
            num = random.randint(0, 500)
            if num%2 == 0:
                movementPos.clear()
                asteroid = asteroids.makeAsteroid() 
                asteroid.draw()
                toMove = (mainCharacter.x + asteroid.height,mainCharacter.y)
                movementPos.append((toMove[0], toMove[1]))
                asteroid.move((toMove[0], toMove[1]))
                offset = ((asteroid.posX + asteroid.height) - (mainCharacter.x+100), (asteroid.posY + asteroid.height)- (mainCharacter.y+100))
                collision = asteroid.mask.overlap(mainCharacter.mask, offset)
                touched = False      
        else:
            if len(movementPos) != 0:
                if mainCharacter.x < 0:
                    toMove = mainCharacter.x
                asteroid.draw()
                asteroid.move((movementPos[0][0], movementPos[0][1]))

                if asteroid.posX +20 >= movementPos[0][0]:
                    asteroid.delete()
                    asteroidPresent = False 
                
                collision = asteroid.mask.overlap(mainCharacter.mask,((asteroid.posX + asteroid.height) - (mainCharacter.x+100), (asteroid.posY + asteroid.height)- (mainCharacter.y+100)))
        
                
            seconds = round((pygame.time.get_ticks()-start)/1000,2)
            if round(seconds%1, 1) == 0:
                hydrate -= 1
            mainCharacterHydration = health.dehydration(hydrate)
            mainCharacterHydration.drawHydration()


        if waterPresent == False:
            water = waterbottle.bottle(700,(350, 530))
            water.move()
            water.draw()
            waterPresent = True
            waterCollected = False
        else:
            water.move()
            water.draw()
            waterCollected = False
        
        if waterPresent == True and water.posX <= -10:
            waterPresent = False

    

        collisonX = (abs((water.heigth + water.posX) - (mainCharacter.x + 100))) <= 40
        collisonY = (abs((water.width + water.posY) - (mainCharacter.y + 100))) <= 40

    
        if collisonX and collisonY:
            

            while waterCollected == False:
                water.delete()
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
            

        #(water.heigth + water.posX) - mainCharacter.x + 100 <= 20 and 
        if collision:
            if touched == False:
                healthNum -=10
                touched = True
                asteroid.delete()
        mainCharacterHealth = health.healthbar(healthNum)
        mainCharacterHealth.drawHealth()
        
        
        # Update the display
        pygame.display.flip()

        # Limit fr  ames per second
        clock.tick(120)

    # Quit Pygame
    pygame.quit()




import pygame
from . import asteroids
from . import people
import random
from . import health
from . import waterbottle

def game1(screen):
    clock = pygame.time.Clock()

    backgroundImage = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/background.png').convert()
    transformedBack = pygame.transform.scale(backgroundImage, (800, 600))

    tiles = (800 // 600) + 2
    scroll = 0

    mainCharacter = people.mainCharacter(100, 450, (-20, 350, 700, 530))
    start = pygame.time.get_ticks()

    asteroid = asteroids.makeAsteroid()
    asteroidPresent = False
    movementPos = []

    healthNum = 200
    hydrate = 200
    water = waterbottle.bottle(700, (350, 530))
    waterPresent = False
    waterCollected = False

    collision = None
    toMove = ()

    touched = False

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return  # Return control to the main loop to handle quitting

        if healthNum <= 0:
            screen.fill((0, 0, 0))
            gameOver = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/gameOver.png').convert()
            screen.blit(gameOver, (0, 0))
            pygame.display.flip()
            pygame.time.wait(3000)
            return  # Return to the main loop after displaying the game over screen

        for j in range(0, int(tiles)):
            screen.blit(transformedBack, (j * 600 + scroll, 0))

        scroll -= 5
        if abs(scroll) > 600:
            scroll = 0

        mainCharacter.draw()
        mainCharacter.anim()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            mainCharacter.move('L')
        if keys[pygame.K_d]:
            mainCharacter.move('R')
        if keys[pygame.K_w]:
            mainCharacter.move('U')
        if keys[pygame.K_s]:
            mainCharacter.move('D')

        if (asteroid.posY < (mainCharacter.y - 100) and asteroid.posY > -100) or asteroidPresent:
            asteroidPresent = True
        else:
            asteroidPresent = False

        if not asteroidPresent:
            num = random.randint(0, 500)
            if num % 100 == 0:
                movementPos.clear()
                asteroid = asteroids.makeAsteroid()
                asteroid.draw()
                toMove = (mainCharacter.x, mainCharacter.y)
                movementPos.append((toMove[0], toMove[1]))
                asteroid.move((toMove[0], toMove[1]))

                offset = ((asteroid.posX + asteroid.height) - (mainCharacter.x + 100), (asteroid.posY + asteroid.height) - (mainCharacter.y + 100))
                collision = asteroid.mask.overlap(mainCharacter.mask, offset)
                touched = False
        else:
            if movementPos:
                if mainCharacter.x < 0:
                    toMove = mainCharacter.x
                asteroid.draw()
                asteroid.move((movementPos[0][0], movementPos[0][1]))

                if asteroid.posX + 20 >= movementPos[0][0]:
                    asteroid.delete()
                    asteroidPresent = False

                offset = ((asteroid.posX + asteroid.height) - (mainCharacter.x + 100), (asteroid.posY + asteroid.height) - (mainCharacter.y + 100))
                collision = asteroid.mask.overlap(mainCharacter.mask, offset)

        if collision:
            if not touched:
                healthNum -= 10
                touched = True
                asteroid.delete()

        mainCharacterHealth = health.healthbar(healthNum)
        mainCharacterHealth.drawHealth()

        if not waterPresent:
            water = waterbottle.bottle(700, (350, 530))
            water.move()
            water.draw()
            waterPresent = True
            waterCollected = False
        else:
            water.move()
            water.draw()
            waterCollected = False

        if waterPresent and water.posX <= -10:
            waterPresent = False

        collisionX = (abs((water.heigth + water.posX) - (mainCharacter.x + 100))) <= 40
        collisionY = (abs((water.width + water.posY) - (mainCharacter.y + 100))) <= 40

        if collisionX and collisionY:
            while not waterCollected:
                water.delete()
                if hydrate < 200:
                    hydrate += 0.5
                    if hydrate > 200:
                        hydrate = 200
                waterCollected = True

        if hydrate <= 0:
            hydrate = 0
            healthNum -= 0.01

        seconds = round((pygame.time.get_ticks() - start) / 1000, 2)
        if round(seconds % 1, 1) == 0:
            hydrate -= 1

        mainCharacterHydration = health.dehydration(hydrate)
        mainCharacterHydration.drawHydration()

        pygame.display.flip()
        clock.tick(120)

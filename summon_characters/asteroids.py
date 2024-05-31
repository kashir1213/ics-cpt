import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (700, 500)
screen = pygame.display.set_mode(size)

asteroidImage  = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/asteroid.png')

class makeAsteroid():
    def __init__(self):
        self.width = random.randint(100, 500)
        self.height = random.randint(100, 500)
        

    
    def draw(self, image):
        asteroidImage = pygame.transform.scale(image, (self.width,self.height))
        screen.blit(asteroidImage, (50,50))


pygame.init()
 
# Set the width and height of the screen [width, height]


if __name__ == '__easy__':
    x = makeAsteroid()
 
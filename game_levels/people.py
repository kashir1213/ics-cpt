import pygame
# Player created just to test(imported from my lab file)

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
class mainCharacter():
    def __init__(self):
        self.image = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/default.png')
        self.x = 370
        self.y = 100

        self.movement1 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement1.png')
        self.movement2 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement2.png')
        self.movement3 = pygame.image.load()

        self.movements = [self.movement1, self.movement2]

    def draw(self):
        # Head
        image = pygame.transform.scale(self.image,(100,100))
        screen.blit(image, (self.x, self.y))
        
        
player = mainCharacter()




# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# Update Screen
pygame.display.flip()
clock.tick(60)

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BROWN = (153,76,0)
GREY = (96,96,96)
YELLOW = (255,255,0)
DARKGREEN = (0,51,0)
ORANGE = (255,128,0)
        

# ## Main Program Loop
while not done:
#     ## CONTROL
#     # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(BLACK)

    player.draw()
# #         # Controls for player
#          elif(event.type == pygame.KEYDOWN):      
#              if event.key == pygame.K_a:
#                  player.x -= player.speed
#              elif event.key == pygame.K_d:
#                  player.x += player.speed
#              elif event.key == pygame.K_e:
#                  boxes.remove()

    # Update Screen
    pygame.display.flip()
    clock.tick(60)

# Close the window and quit
pygame.quit()

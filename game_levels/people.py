import pygame
import boxes
# Player created just to test(imported from my lab file)
class character:

    def __init__(self):
        self.x = 370
        self.y = 470
        self.speed = 5
        self.width = 80
        self.height = 70

    def drawPlayer(self, screen):
        # Head
        pygame.draw.rect(screen, YELLOW, [1+self.x, self.y, 10, 10], 0)
        
player = character()
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)


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
#         # Controls for player
         elif(event.type == pygame.KEYDOWN):      
             if event.key == pygame.K_a:
                 player.x -= player.speed
             elif event.key == pygame.K_d:
                 player.x += player.speed
             elif event.key == pygame.K_e:
                 boxes.remove()


#     screen.fill(BLACK)

        
#     # Update Screen
#     pygame.display.flip()
#     clock.tick(60)
#     # Close the window and quit
# pygame.quit()

import pygame
# Player created just to test(imported from my lab file)

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)



class mainCharacter():
    def __init__(self):
        self.image = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/default.png')
        self.image = pygame.transform.flip(self.image, True, False)

        self.x = 370
        self.y = 100

        self.movement1 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement1.png')
        self.movement2 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement2.png')
        self.movement3 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement3.png')
        self.movement4 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement4.png')
        self.movement5 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement5.png')
        self.movement6 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement6.png')
        # self.movement7 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement7.png')


        self.movement1 = pygame.transform.flip(self.movement1, True, False)
        self.movement2 = pygame.transform.flip(self.movement2, True, False)
        self.movement3 = pygame.transform.flip(self.movement3, True, False)
        self.movement4 = pygame.transform.flip(self.movement4, True, False)
        self.movement5 = pygame.transform.flip(self.movement5, True, False)
        self.movement6 = pygame.transform.flip(self.movement6, True, False)

        self.movements = [self.movement1, self.movement2,self.movement3, self.movement4, self.movement5, self.movement6]
        self.current_image = 0

        self.animating = True

    def draw(self):
        
        image = pygame.transform.scale(self.image,(100,100))
        screen.blit(image, (self.x, self.y))
    def move(self, position):

        if (800 > self.x > 50) and (600 > self.y > 50):
            if position == 'L':
                self.x -= 8
            
            if position == 'R':
                self.x += 8
            
            if position == 'U':
                self.y -= 8

            if position == 'D':
                self.y += 8

    def anim(self):
        if self.animating:
            self.current_image += 1
            if self.current_image >= len(self.movements):
                self.current_image = 0
            self.image = self.movements[self.current_image]

        

# player = mainCharacter()




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


# n = 0
# # ## Main Program Loop
# while not done:
# #     ## CONTROL
# #     # Check for events
    
    
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
    
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_a]:
#         player.move('L')
#     if keys[pygame.K_d]:
#         player.move('R')
#     if keys[pygame.K_w]:
#         player.move('U')
#     if keys[pygame.K_s]:
#         player.move('D')
    
#     # print(pygame.key.get_pressed(pygame.K_a))
#     player.anim()

#     screen.fill(BLACK)

#     player.draw()
#     # Update Screen
#     pygame.display.flip()
#     clock.tick(10)

# # Close the window and quit
# pygame.quit()

import pygame

pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)



class mainCharacter():
    def __init__(self, xPos, yPos, stop):

        self.x = xPos
        self.y = yPos
        self.stop = list(stop)

        self.image = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/default.png')
        self.image = pygame.transform.flip(self.image, True, False)
        self.mask = None



        self.movement1 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement1.png').convert_alpha()
        self.movement2 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement2.png').convert_alpha()
        self.movement3 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement3.png').convert_alpha()
        self.movement4 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement4.png').convert_alpha()
        self.movement5 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement5.png').convert_alpha()
        self.movement6 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement6.png').convert_alpha()
        # self.movement7 = pygame.image.load('C:/Users/Kashir/OneDrive - Dufferin-Peel Catholic District School Board/ICS3UC/CPT/checkpoint1/movement7.png')


        self.movements = [self.movement1, self.movement2,self.movement3, self.movement4, self.movement5, self.movement6]
        self.current_image = 0

        self.animating = True

        self.imageRect = 0

    def draw(self):
        
        image = pygame.transform.scale(self.image,(100,100))
        self.mask = pygame.mask.from_surface(self.image)
        screen.blit(image, (self.x, self.y))
    def move(self,position):

        if(self.x > self.stop[0]):
            if position == 'L':
                self.x -= 8
        if(self.x < self.stop[2]):
            if position == 'R':
                self.x += 8
        if(self.y > self.stop[1]):
            if position == 'U':
                self.y -= 8
        if(self.y < self.stop[3]):
            if position == 'D':
                self.y += 8

    def anim(self):
        if self.animating:
            self.current_image += 1
            if self.current_image >= len(self.movements):
                self.current_image = 0
            self.image = self.movements[self.current_image]
            self.imageRect = self.image.get_rect()
    

        

        

# player = mainCharacter()




# # Loop until the user clicks the close button.
# done = False

# # Used to manage how fast the screen updates
# clock = pygame.time.Clock()
# # Update Screen
# pygame.display.flip()
# clock.tick(60)

# # Colours
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# BROWN = (153,76,0)
# GREY = (96,96,96)
# YELLOW = (255,255,0)
# DARKGREEN = (0,51,0)
# ORANGE = (255,128,0)

# playerX = 100
# playerY = 100

# player = mainCharacter(playerX, playerY,(50, 50, 700, 500))

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

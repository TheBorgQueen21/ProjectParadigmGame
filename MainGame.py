### Title: Main Part of the Game
### Date: July 6, 2020
### File Owner: Everyone

import pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))
#Colors
black = (0, 0, 0)

#font
over_font = pygame.font.Font('freesansbold.ttf', 20)

#Title and Icon
pygame.display.set_caption("Project Paradigm")
icon = pygame.image.load ('flower (1).png')
pygame.display.set_icon(icon)

# background
screen_one_background = pygame.image.load("Background_first_draft_finalsize.png").convert()
screen_two_background = pygame.image.load("cave_background.png").convert()
screen_three_background = pygame.image.load("Yellow_Background.png").convert()

#Player Code
playerImg = pygame.image.load('heart.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y)) #draws the player on the screen

#Trying out Classes for Different Rooms
"""class Room(object):
    Base class for all rooms.

    # Each room has a list of walls, and of enemy sprites.
    background_list = []
    sprite_list = None

    def __init__(self):
        Constructor, create our lists.
        self.background_list = pygame.sprite.Group()
        self.sprite_list = pygame.sprite.Group()

class Room1(Room):
    This creates all the walls in room 1
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)

        # This is a list of walls. Each is in the form [x, y, width, height]
        sprites = [[playerX == 143.5, playerY<=480, playerY >=402.5], #playerX == 143.5 and playerY<=480 and playerY >=402.5
                 [playerX==143.5, playerY<=334, playerY >=262.5], #playerX==143.5 and playerY<=334 and playerY >=262.5
                 [playerX>=143.5, playerX<=247, playerY == 64], #playerX>=143.5 and playerX<=247 and playerY == 64
                 [playerY==64, playerX>=494.5, playerX<=562.5], #playerY==64 and playerX>=494.5 and playerX<=562.5
                 [playerX==630.5, playerY>=225.5, playerY <=291], #playerX==630.5 and playerY>=225.5 and playerY <=291
                 [playerX== 630.5, playerY>=375.5, playerY<= 480], #playerX== 630.5 and playerY>=375.5 and playerY<= 480
                ]
        background.append(screen_one_background)

class Room2(Room):
    This creates all the walls in room 1
    def __init__(self):
        super().__init__()"""
        # Make the walls. (x_pos, y_pos, width, height)

scenerealnum = 0
#Press space
def spacepress (scripttext, secondtext):
    #global sone_item_count
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_SPACE:
            pygame.draw.rect(screen,black,(0, 350, 800, 600))
            first_text = over_font.render(scripttext, True, (255, 255, 255))
            second_text= over_font.render(secondtext, True, (255, 255, 255))
            screen.blit (first_text, (20, 400))
            screen.blit (second_text, (20, 450))
            #sone_item_count += 1

def screen_two ():
    playerX = 75
    playerY = 300
    screen.blit(screen_two_background, (0, 0)) #figrue out how to change the backgrounds


def screen_three ():
    playerX = 75
    playerY = 300
    screen.blit(screen_three_background, (0, 0)) #figrue out how to change the backgrounds

#Screen 1-at home
def screen_one (scenenum):
    screen.blit(screen_one_background, (0, 0))
    scenenum = 1
    if playerX == 143.5 and playerY<=480 and playerY >=402.5:
        print("plant")
        spacepress("plant_Trying out code", "")
    elif playerX==143.5 and playerY<=334 and playerY >=262.5:
        print("phone")
        spacepress("phone_Trying out code" , "")
    elif playerX>=143.5 and playerX<=247 and playerY == 64:
        print("painting")
        spacepress("This is a painting that came with this house.", "There is something behind it. Press E to Go through")
        #if event.type == pygame.KEYUP:
            #if event.key == pygame.K_e:

    elif playerY==64 and playerX>=494.5 and playerX<=562.5:
        print("piggybank")
        spacepress("piggybank_Trying out code", "")
    elif playerX==630.5 and playerY ==64:
        print("dumbells")
        spacepress("dumbbells_Trying out code", "")
    elif playerX==630.5 and playerY>=225.5 and playerY <=291:
        print("diary")
        spacepress("diary_Trying out code", "")
    elif playerX== 630.5 and playerY>=375.5 and playerY<= 480:
        print("bookshelf")
        spacepress("bookshelf_Trying out code", "")
    #elif playerX >= 307 and playerX<=440 and playerY <= 186:
        #print("bed")
    else:
        print("nothing")


#Game Loop
running = True
while running: #anything you want to appear continuously must go inside this while loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Assigns KeyBoard to Game
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.5
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.5
        if event.key == pygame.K_DOWN:
            playerY_change = 0.5
        if event.key == pygame.K_UP:
            playerY_change = -0.5
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or  event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            playerX_change = 0
            playerY_change = 0

    #Keeps Player in Bounds
    playerX += playerX_change
    playerY += playerY_change

    #print (playerX)
    #print (playerY)

    #if event.type == pygame.KEYUP:
        #if event.key == pygame.K_e:
    # playerX>=143.5 and playerX<=247 and playerY == 64


    #background mage
    screen.fill((0, 0, 0))
    screen_one(scenerealnum)
    player(playerX, playerY)

    if not scenerealnum == 1:
        if playerX <= 143.5:
            playerX = 143.5
        elif playerX >= 630.5:#736
            playerX = 630.5
        if playerY <= 64:
            playerY = 64
        elif playerY >= 480:
            playerY = 480
        print ("not scene 1")

    elif scenerealnum == 1:
        if playerX <= 247:
            playerX = 247
        elif playerX >= 630.5:
            playerX = 630.5
        if playerY <= 64:
            playerY = 64
        elif playerY >= 480:
            playerY = 480
        if playerX>=143.5 and playerX<=247 and playerY == 64:
            screen_two()
        print("scene 1")

    pygame.display.update()

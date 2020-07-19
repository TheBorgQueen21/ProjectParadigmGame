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

#Player Code
playerImg = pygame.image.load('heart.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y)) #draws the player on the screen

#Screen One Item Counter
x = 0

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


#Screen 1-at home
def screen_one (x):
    screen.blit(screen_one_background, (0, 0))
    screentwo = False
    if playerX == 143.5 and playerY<=480 and playerY >=402.5:
        print("plant")
        spacepress("plant_Trying out code", "")
    elif playerX==143.5 and playerY<=334 and playerY >=262.5:
        print("phone")
        spacepress("phone_Trying out code" , "")
    elif playerX>=143.5 and playerX<=247 and playerY == 64:
        print("painting")
        spacepress("This is a painting that came with this house.", "There is something behind it. (press e to take out painting)")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                x+=1
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
    if x >= 1:
        screen_two()

def screen_two ():
    playerX = 75
    playerY = 300
    screen.blit(screen_two_background, (0, 0)) #figrue out how to change the backgrounds


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
    if playerX <= 143.5:
        playerX = 143.5
    elif playerX >= 630.5:#736
        playerX = 630.5
    if playerY <= 64:
        playerY = 64
    elif playerY >= 480:
        playerY = 480
    #print (playerX)
    #print (playerY)

    #background mage
    screen.fill((0, 0, 0))
    screen_one(x)
    player(playerX, playerY)
    pygame.display.update()

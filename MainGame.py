### Title: Main Part of the Game
### Date: July 6, 2020
### File Owner: Everyone

import pygame
pygame.init()

#create the screen
screen = pygame.display.set_mode((800, 600))
#testing code here...

#Title and Icon
pygame.display.set_caption("Project Paradigm")
icon = pygame.image.load ('flower (1).png')
pygame.display.set_icon(icon)

# background
screen_one_background = pygame.image.load("Background_first_draft_finalsize.png").convert()

#Player Code
playerImg = pygame.image.load('heart.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0
def player(x, y):
    screen.blit(playerImg, (x, y)) #draws the player on the screen

#Screen One Item Counter
sone_item_count = 0

#Screen 1-at home
def screen_one ():
    screen.blit(screen_one_background, (0, 0))
    if playerX == 143.5 and playerY<=480 and playerY >=402.5:
        print("plant")
    elif playerX==143.5 and playerY<=334 and playerY >=262.5:
        print("phone")
    elif playerX>=143.5 and playerX<=247 and playerY == 64:
        print("painting")
    elif playerY==64 and playerX>=494.5 and playerX<=562.5:
        print("piggybank")
    elif playerX==630.5 and playerY ==64:
        print("dumbells")
    elif playerX==630.5 and playerY>=225.5 and playerY <=291:
        print("diary")
    elif playerX== 630.5 and playerY>=375.5 and playerY<= 480:
        print("bookshelf")
    elif playerX >= 307 and playerX<=440 and playerY <= 186:
        print("bed")
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
    screen_one()

    player(playerX, playerY)
    pygame.display.update()

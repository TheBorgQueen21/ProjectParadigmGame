### File Owner: Anika
### Date: July 7, 2020
### File: Second Mini Game (space invader)

#initialize the pygame
import pygame
import random
import math
pygame.init ()

#testing again different area


#create the screen
screen = pygame.display.set_mode((800, 600))

# background
#background = pygame.image.load('Yellow_Background.png')
background = pygame.image.load("Yellow_Background.png").convert()

#Title and Icon
pygame.display.set_caption("Project Paradigm")
icon = pygame.image.load('flower (1).png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('heart.png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
EnemyImg = []
EnemyX = []
EnemyY = []
EnemyX_change  = []
EnemyY_change = []
num_of_enemies = 6

for i in range (num_of_enemies):
    EnemyImg.append(pygame.image.load('broken-heart.png'))
    EnemyX.append(random.randint(50, 150))
    EnemyY.append(random.randint(50, 150))
    EnemyX_change.append(0.5)
    EnemyY_change.append(40)

#Bullet
bulletImg = pygame.image.load('up-arrow.png')
bulletX = 0
bulletY = 480 #change to random, between 50 and 150
bulletX_change  = 1###
bulletY_change = 1
bullet_state = "ready" #ready state means you can't see the bullet on the screen, fire means bullet is moving

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score (x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit (score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y)) #draws the player on the screen

def Enemy(x, y, i):
    screen.blit(EnemyImg [i], (x, y))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + int(16), y + int(10)))

def isCollision (EnemyX, EnemyY, bulletX, bulletY ):
    distance = math.sqrt ((math.pow(EnemyX - bulletX,2)) + (math.pow(EnemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False

#Game Over text
over_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over_text():
    over_text = over_font.render("Game Over", True, (255, 255, 255))
    screen.blit (over_text, (200, 250))

#Game Loop (allows user to exit)
running = True
while running: #anything you want to appear continuously must go inside this while loop
    screen.fill((150, 50, 250)) #rgb value
    #background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #if keystroke pressed, check if right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet (bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #checking player's sprite boundries
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #subtract the size of sprite from the side (800 pixels)
        playerX = 736

    #checking enemy movement
    for i in range (num_of_enemies):

        #Game over
        if EnemyY[i] > 440:
            for j in range(num_of_enemies):
                EnemyY[j] = 2000
            game_over_text()
            break

        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0:
            EnemyX_change[i] = 0.5
            EnemyY[i] += EnemyY_change[i]
        elif EnemyX[i] >= 736:
            EnemyX_change[i] = -0.5
            EnemyY[i] += EnemyY_change[i]

        #collision
        collision = isCollision (EnemyX[i], EnemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            EnemyX[i] = random.randint(0, 735)
            EnemyY[i] = 50 #change to random, between 50 and 150

        Enemy(EnemyX[i], EnemyY[i], i)


    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"


    if bullet_state is "fire":
        fire_bullet (bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY) #must be after fill method bc it wont be overwritten by the background
    show_score(textX, textY)

    pygame.display.update()

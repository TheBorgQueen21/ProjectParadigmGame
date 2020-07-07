### File Owner: Anika
### Date: July 3, 2020
### Title: Practice for Minigame

from pygame import *
SCREENWIDTH = 900
SCREENHEIGHT = 600
screen = display.set_mode((SCREENWIDTH, SCREENHEIGHT))

font.init()
calibriBold35 = font.SysFont ("Calibri Bold", 35) #35 is the size of the font

WHITE = (255, 255, 255)
BGCOLOR = (0, 220, 160)
BLUE = (50, 100, 230)
RED = (230, 50, 100)

p1Y = 250
p2Y = 250
paddlewidth = 30
paddleheight = 100
p1Points = 0
p2Points = 0


ballX = 450
ballY = 300
ballDx = 4 #ball speed (when positive, moves to right; when negative, moves to left)
ballDy = 4



running = True
myClock = time.Clock()
while running:
    for evt in event.get():
        if evt.type == QUIT:
            running = False
    #This defines the rectanges, but it doesn't actually draw them
    p1Paddle = Rect(50, p1Y, paddlewidth, paddleheight)
    p2Paddle = Rect(850, p2Y, paddlewidth, paddleheight)
    ball = Rect(ballX, ballY, 10, 10)


    keys = key.get_pressed()

    #for player 1 controls
    if (keys [K_w] and p1Y > 0):
        p1Y -= 5 #the speed of the paddles
    elif (keys[K_s] and p1Y + paddleheight < SCREENHEIGHT ):
        p1Y += 5

    #for player 2 controls
    if (keys [K_UP] and p2Y > 0):
        p2Y -= 5 #the speed of the paddles
    elif (keys[K_DOWN] and p2Y + paddleheight < SCREENHEIGHT ):
        p2Y += 5


    ballX += ballDx
    ballY += ballDy
    if (ball.colliderect(p1Paddle)):
        ballDx = abs(ballDx)
    if (ball.colliderect(p2Paddle)):
        ballDx = abs(ballDx) * -1
    elif (ballY <= 0):
        ballDy = abs(ballDy)
    elif (ballY >= SCREENHEIGHT):
        ballDy = abs(ballDy) * -1
    elif (ballX >= SCREENWIDTH or ballX <= 0):
        if ballX >= SCREENWIDTH:
            p1Points +=1
        elif ballX <= 0:
            p2Points += 1

        ballX = 450
        ballY = 300
        p1Y = 250
        p2Y = 250


    screen.fill(BGCOLOR)
    draw.rect(screen, BLUE, p1Paddle)
    draw.rect(screen, RED, p2Paddle)
    draw.rect(screen, WHITE, ball)
    p1PtsTxt = calibriBold35. render("P1 Points: " + str(p1Points), True, BLUE)
    p2PtsTxt = calibriBold35. render("P2 Points: " + str(p2Points), True, RED)
    screen.blit(p1PtsTxt, (130, 20))
    screen.blit(p2PtsTxt, (620, 20))

    display.flip()
    myClock.tick(60)


quit()

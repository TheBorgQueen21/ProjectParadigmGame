import pygame
import time
import random

pygame.init()

green = (0,255,0)
black = (0,0,0)
red = (255,0,0)
white = (255,255,255)

dis_width = 800 # screen width
dis_height = 600 # screen height

dis = pygame.display.set_mode((dis_width,dis_height)) # This is the screen size, it can be changed if needed
pygame.display.set_caption('Snake Game') # This doesn't display "Snake Game", idk why but its not needed anyways

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont(None, 30)


def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width/3, dis_height/3])

  
def gameLoop(): # Creates a function
  game_over = False
  game_close = False
  
  x1 = dis_width / 2
  y1 = dis_height / 2

  x1_change = 0
  y1_change = 0
  
  foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # Controls x value location of food I think
  foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # Controls y value location of food I think

  while not game_over:
    
    while game_close == True:
      dis.fill(black) # Changes the background color
      message("You Lost! Press Q to Quit or C to Play Again", red)
      pygame.display.update()
    
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q: # If the user presses Q
            game_over = True
            game_close = False
          if event.key == pygame.K_c: # If the user presses C
            gameLoop()
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_over = True
      if event.type == pygame.KEYDOWN: # When the user presses a direction key, the following code controls the snake's direction
        if event.key == pygame.K_LEFT:
          x1_change = -snake_block
          y1_change = 0
        elif event.key == pygame.K_RIGHT:
          x1_change = snake_block
          y1_change = 0
        elif event.key == pygame.K_UP:
          y1_change = -snake_block
          x1_change = 0
        elif event.key == pygame.K_DOWN:
          y1_change = snake_block
          x1_change = 0
  
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
      game_close = True
  
    x1 += x1_change
    y1 += y1_change
    dis.fill(black) # changes background color
    pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
    pygame.draw.rect(dis, white, [x1, y1, snake_block, snake_block])
    pygame.display.update()
    
    if x1 == foodx and y1 == foody:
      print("Yum!")
    clock.tick(snake_speed)

  pygame.quit
  quit()
  
gameLoop()

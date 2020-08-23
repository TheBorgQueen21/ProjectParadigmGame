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
snake_speed = 15

font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont("comicsansms", 35)

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width/20, dis_height/3]) # Controls where messages appear

  
def gameLoop(): # Creates a function
  game_over = False
  game_close = False
  
  x1 = dis_width / 2
  y1 = dis_height / 2

  x1_change = 0
  y1_change = 0

  snake_List = []
  Length_of_snake = 1
  
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
    pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_List.append(snake_head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]
        
    for x in snake_List[:-1]:
        if x == snake_head:
            game_close = True
            
    our_snake(snake_block, snake_List)

    pygame.display.update()
    
    if x1 == foodx and y1 == foody: # If the snake collides with the food
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1
    
    clock.tick(snake_speed)

  pygame.quit
  quit()
  
gameLoop()

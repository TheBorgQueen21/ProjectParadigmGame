import pygame
import time
pygame.init()

green = (0,255,0)
black = (0,0,0)
red = (255,0,0)

dis_width = 800 # screen width
dis_height = 600 # screen height
dis = pygame.display.set_mode((dis_width,dis_height)) # This is the screen size, it can be changed if needed
pygame.display.set_caption('Snake Game') # This doesn't display "Snake Game", idk why but its not needed anyways

game_over = False

x1 = dis_width/2
y1 = dis_height/2

x1_change = 0
y1_change = 0

snake_block = 10
snake_speed = 30

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

def message(msg,color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width/2, dis_height/2])

while not game_over:
  for event in pygame.event.get(): # Records where mouse is located I think
    if event.type == pygame.QUIT: # This line and the next might not be needed, they allow the user to close the screen when the mouse is over the quit button, but there's not quite button so im confused
      game_over == True
    if event.type == pygame.KEYDOWN: # When the user presses a key, the following code controls the snake's direction
      if event.key == pygame.K_LEFT:
        x1_change = -10
        y1_change = 0
      elif event.key == pygame.K_RIGHT:
        x1_change = 10
        y1_change = 0
      elif event.key == pygame.K_UP:
        y1_change = -10
        x1_change = 0
      elif event.key == pygame.K_DOWN:
        y1_change = 10
        x1_change = 0
  
  if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
    game_over = True
  
  x1 += x1_change
  y1 += y1_change
  dis.fill(black) # changes background color
  pygame.draw.rect(dis, green, [x1, y1, 10, 10])
  
  pygame.display.update()
  
  clock.tick(snake_speed)

message("Game Over",red)
pygame.display.update()
time.sleep(2) # Screen stays for 2 seconds I think

pygame.quit
quit()

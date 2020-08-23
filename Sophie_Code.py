import pygame

pygame.init()

green = (0,255,0)
black = (0,0,0)

dis = pygame.display.set_mode((800,600)) # This is the screen size, it can be changed if needed
pygame.display.set_caption('Snake Game') # This doesn't display "Snake Game", idk why but its not needed anyways

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

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
  
  x1 += x1_change
  y1 += y1_change
  dis.fill(black) # to change background color put dis.fill(color) make sure the color is defined earlier in code
  pygame.draw.rect(dis, green, [x1, y1, 10, 10])
  
  pygame.display.update()
  
  clock.tick(30)
  
pygame.quit
quit()

import pygame
pygame.init()
dis=pygame.display.set_mode((400,300)) # This is the screen size, it can be changed if needed
# I had pygame.display.update() here but idk if it's still needed

pygame.display.set_caption('Snake Game') # This doesn't display "Snake Game", idk why but its not needed anyways

green=(0,255,0)
blue=(0,0,225)

game_over=False
while not game_over:
  for event in pygame.event.get(): # Records where mouse is located
    if event.type==pygame.QUIT: # This line and the next might not be needed, they allow the user to close the screen when the mouse is over the quit button, but there's not quite button so im confused
      game_over==True
    
pygame.quit
quit()

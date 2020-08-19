import pygame
pygame.init()
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
PINK = (255, 51, 153)
YELLOW = (255, 255, 51)
NAVY = (0, 0, 204)
ORANGE = (255, 128, 0)
LIGHTPURPLE = (229, 204, 225)
LIGHTPINK = (255, 204, 255)
LIGHTBLUE = (204, 255, 255)
PEACH = (255,228,181)


game_font = pygame.font.Font('freesansbold.ttf', 15)
screen = pygame.display.set_mode([800, 600])


class Wall(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        
        
class Object(pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color, toptext, bottomtext):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        self.toptext = toptext
        self.bottomtext = bottomtext
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = (self.rect.x-20, self.rect.y-15, self.width+10, self.height+15) # NEW

    def draw_hitbox(self, x, y, width, height):
      self.hitbox = (self.rect.x-20, self.rect.y-15, self.width+10, self.height+15) # NEW
      pygame.draw.rect(screen, (255,0,0), self.hitbox,2) # To draw the hit box around the player
    
    def hit(self):
      pygame.draw.rect(screen, WHITE, (0, 350, 800, 600))
      first_text = game_font.render(self.toptext, True, BLUE)
      second_text= game_font.render(self.bottomtext, True, BLUE)
      screen.blit (first_text, (20, 400))
      screen.blit (second_text, (20, 450))
      
    def hit_hitbox (self, playerx, playery, player2, player3):
      if playery < self.hitbox[1] + self.hitbox[3] and playery + player3 > self.hitbox[1]:
        if playerx + player2 > self.hitbox[0] and playerx < self.hitbox[0] + self.hitbox[2]:
          self.hit()

class Sprite (pygame.sprite.Sprite):
    """This class represents the bar at the bottom that the player controls """
 
    def __init__(self, x, y, width, height, color, toptext, bottomtext):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Make a BLUE wall, of the size specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.width = width
        self.height = height
        self.toptext = toptext
        self.bottomtext = bottomtext
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = (self.rect.x-20, self.rect.y-15, self.width+10, self.height+15) # NEW

    def draw_hitbox(self, x, y, width, height):
      self.hitbox = (self.rect.x-20, self.rect.y-15, self.width+10, self.height+15) # NEW
      pygame.draw.rect(screen, (255,0,0), self.hitbox,2) # To draw the hit box around the player
    
    def hit(self):
      pygame.draw.rect(screen, WHITE, (0, 350, 800, 600))
      first_text = game_font.render(self.toptext, True, BLUE)
      second_text= game_font.render(self.bottomtext, True, BLUE)
      screen.blit (first_text, (20, 400))
      screen.blit (second_text, (20, 450))
      
    def hit_hitbox (self, playerx, playery, player2, player3):
      if playery < self.hitbox[1] + self.hitbox[3] and playery + player3 > self.hitbox[1]:
        if playerx + player2 > self.hitbox[0] and playerx < self.hitbox[0] + self.hitbox[2]:
          self.hit()
 
 
class Player(pygame.sprite.Sprite):
    """ This class represents the bar at the bottom that the
    player controls """
 
    # Set speed vector
    change_x = 0
    change_y = 0
    
 
    def __init__(self, x, y):
        """ Constructor function """
 
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])##pygame.image.load('heart.png') 
        self.image.fill(WHITE)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.hitbox = (self.rect.x-15, self.rect.y-15, 42, 42) # NEW

        
    def draw_hitbox(self, x, y):
      self.hitbox = (self.rect.x-15, self.rect.y-15, 42, 42) # NEW
      pygame.draw.rect(screen, (255,0,0), self.hitbox,2) # To draw the hit box around the player
      
      
    def changespeed(self, x, y):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
 
    def move(self, walls, objects, sprites): ###added objects here
        """ Find a new position for the player """
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
                
        #### --- OBJECT --- ####
        #Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, objects, False)

        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, objects, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
         
        ###---NPC Sprites ---###      
        #Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, sprites, False)

        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of
            # the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
 
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, sprites, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
        
 #####***JULY 24: I need to fix the walls and where they are placed. I already: Converted the code above, added all the rooms (the rooms don't have correct walls yet)***#####
 #####***JULY 27: I need to fix the walls' placement. I already: Fixed the order of the rooms ****######
 #####***JULY 28: I need to add the text for the objects and find a place to test the code. I already: Fixed all the walls in the rooms. *****#####
 #####***JULY 29: I need to fix the gameplay of the walls. I already: decoded everything.  ****######
 #####***JULY 30: I need to fix the lists for the objects in game. I already: prepped backgrounds ***####
 #####***JULY 31: I need to fix the spacepress function for object interaction. I already: created a way to make objects in game****#####
 #####***AUGUST 12: I need to find out how to access the arguments from a class outside the class (so that way I can compare the in game objects to the player's x and y)
 #####***AUGUST 13: I am in the middle of making hitboxes. I finished making hitboxes for the player, trying to figure out how to do it for the objects
 #####***AUGUST 14: I finished making the hitboxes for the player and objects!! Now I need add what happens when they collide
 #####***AUGUST 19: I finished adding the collisions for hitboxes and the text comes up when collided
 ################## I need to figure out how to make text appear and disappear when pressed.
 
 
player = Player(50, 50)
 
class Room(object):
    """ Base class for all rooms. """
 
    # Each room has a list of walls, and of enemy sprites.
    wall_list = None
    object_list = None
    chara_sprites = None
 
    def __init__(self):
        """ Constructor, create our lists. """
        self.wall_list = pygame.sprite.Group()
        self.object_list = pygame.sprite.Group()
        self.chara_sprites = pygame.sprite.Group()
 
 
class Room_Bedroom (Room): #finished walls
    """This creates all the walls in room 1"""
    def __init__(self):
        super().__init__()
        # Make the walls. (x_pos, y_pos, width, height)
 
        # This is a list of walls. Each is in the form [x, y, width, height]
        walls = [[0, 0, 20, 600, PINK], #left side closed
                 [780, 0, 20, 600, PINK], #right side closed
                 [20, 0, 350, 20, PINK], #top open left
                 [20, 0, 420, 20, PINK], #top open right
                 [20, 580, 760, 20, PINK], #bottom closed
                ]
 
 
        # Loop through the list. Create the wall, add it to the list
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
        
        
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "This is the bedroom", "This is the bed"], 
                    [500, 300, 100, 80, GREEN, "This is the bedroom", "This is the desk"] 
                  ]
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
        sprites = [[200, 300, 50, 50, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
 
class Room_Cave1(Room): #walls done
    """This creates all the walls in room 2"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, RED], #left open top
                 [0, 350, 20, 250, RED], #left open bottom
                 [780, 0, 20, 250, RED], #right open top
                 [780, 350, 20, 250, RED], #right open bottom
                 [20, 0, 350, 20, RED], #top open left
                 [20, 0, 420, 20, RED], #top open right
                 [20, 580, 350, 20, RED], #bottom open right
                 [20, 580, 420, 20, RED], #bottom open right
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
            
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 
            
        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
class Room_Cave2 (Room): #walls done
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, WHITE], #left open top
                 [0, 350, 20, 250, WHITE], #left open bottom
                 [780, 0, 20, 250, WHITE], #right open top
                 [780, 350, 20, 250, WHITE], #right open bottom
                 [20, 0, 350, 20, WHITE], #top open left
                 [20, 0, 420, 20, WHITE], #top open right
                 [20, 580, 350, 20, WHITE], #bottom open right
                 [20, 580, 420, 20, WHITE], #bottom open right
                ]
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                           
class Room_Cave3 (Room): #finsihed these walls
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()    
        walls = [[0, 0, 20, 250, BLUE],
                 [0, 350, 20, 250, BLUE],
                 [780, 0, 20, 250, BLUE],
                 [780, 350, 20, 250, BLUE],
                 [20, 0, 760, 20, BLUE],
                 [20, 580, 350, 20, BLUE], #bottom open right
                 [20, 580, 420, 20, BLUE], #bottom open right
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)

            
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                 
 
class Room_WorldOne (Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, PURPLE],
                 [0, 350, 20, 250, PURPLE],
                 [780, 0, 20, 600, PURPLE],
                 [20, 0, 760, 20, PURPLE],
                 [20, 580, 760, 20, PURPLE]
                ]
 
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                        
            
class Room_WorldTwo (Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 600, GREEN], #left closed
                 [780, 0, 20, 250, GREEN],
                 [780, 350, 20, 250, GREEN],
                 [20, 0, 760, 20, GREEN],
                 [20, 580, 760, 20, GREEN]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)            
 
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
                            
class Room_WorldThree (Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, LIGHTPURPLE],
                 [0, 350, 20, 250, LIGHTPURPLE],
                 [780, 0, 20, 600, LIGHTPURPLE],
                 [20, 0, 760, 20, LIGHTPURPLE],
                 [20, 580, 760, 20, LIGHTPURPLE]
                ]
 
  
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
            
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
                
class Room_WorldFour (Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 600, YELLOW], #left closed
                 [780, 0, 20, 250, YELLOW],
                 [780, 350, 20, 250, YELLOW],
                 [20, 0, 760, 20, YELLOW],
                 [20, 580, 760, 20, YELLOW]
                ]
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
            
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
                
                
class Room_WorldFive (Room):
    """This creates all the walls in room 3"""
    def __init__(self):
        super().__init__()
 
        walls = [[0, 0, 20, 250, NAVY],
                 [0, 350, 20, 250, NAVY],
                 [780, 0, 20, 600, NAVY],
                 [20, 0, 760, 20, NAVY],
                 [20, 580, 760, 20, NAVY]
                ]
 
 
        for item in walls:
            wall = Wall(item[0], item[1], item[2], item[3], item[4])
            self.wall_list.add(wall)
 
    def draw (self):
        objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
        for item in objects:
            game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.object_list.add(game_object) 
            game_object.draw_hitbox(item[0], item[1], item[2], item[3])
            game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

        sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
        for item in sprites:
            npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
            self.chara_sprites.add(npc_Sprite) 
            npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
            npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
                            
            
class Room_WorldSix (Room):
  """This creates all the walls in room 3"""
  def __init__(self):
    super().__init__()
 
    walls = [[0, 0, 20, 600, ORANGE], #left closed
            [780, 0, 20, 250, ORANGE],
            [780, 350, 20, 250, ORANGE],
            [20, 0, 760, 20, ORANGE],
            [20, 580, 760, 20, ORANGE]
            ]
 
    for item in walls:
      wall = Wall(item[0], item[1], item[2], item[3], item[4])
      self.wall_list.add(wall)
      
  def draw (self):
      objects = [[200, 200, 40, 60, BLUE, "text here", "wow, this works!!"]] 
      for item in objects:
          game_object = Object(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
          self.object_list.add(game_object) 
          game_object.draw_hitbox(item[0], item[1], item[2], item[3])
          game_object.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3]) 

      sprites = [[200, 300, 20, 20, PEACH, "This is a character", "Hello!!"]
                  ]
      for item in sprites:
          npc_Sprite = Sprite(item[0], item[1], item[2], item[3], item[4], item[5], item[6])
          self.chara_sprites.add(npc_Sprite) 
          npc_Sprite.draw_hitbox(item[0], item[1], item[2], item[3])
          npc_Sprite.hit_hitbox(player.hitbox[0], player.hitbox[1], player.hitbox[2], player.hitbox[3])    
                
                 
def main():
    """ Main Program """
 
    # Call this function so the Pygame library can initialize itself
    pygame.init()
 
    # Create an 800x600 sized screen
    screen = pygame.display.set_mode([800, 600])
 
    # Set the title of the window
    pygame.display.set_caption('Maze Runner')
 
    # Create the player paddle object
    ##player = Player(50, 50)
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    
    #Create Game Object Paddle Object
    
    rooms = []
 
    room = Room_Bedroom()
    rooms.append(room)
 
    room = Room_Cave1()
    rooms.append(room)
 
    room = Room_Cave2()
    rooms.append(room)
 
    room = Room_Cave3()
    rooms.append(room)
   
    room = Room_WorldOne()
    rooms.append(room)
    
    room = Room_WorldTwo()
    rooms.append(room)
    
    room = Room_WorldThree()
    rooms.append(room)
    
    room = Room_WorldFour()
    rooms.append(room)
    
    room = Room_WorldFive()
    rooms.append(room)
        
    room = Room_WorldSix()
    rooms.append(room)   

 
 
    current_room_no = 0
    current_room = rooms[current_room_no]
 
    clock = pygame.time.Clock()
 
    done = False
 
    while not done:
 
         # --- Event Processing ---
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5)
 
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0)
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0)
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5)
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5)
 
        # --- Game Logic ---
        player.move(current_room.wall_list, current_room.object_list, current_room.chara_sprites)
      
        if player.rect.x < -15:
            if current_room_no == 1:
                current_room_no = 5
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 2:
                current_room_no = 7
                current_room = rooms[current_room_no]
                player.rect.x = 790
            elif current_room_no == 3:
                current_room_no = 9
                current_room = rooms[current_room_no]
                player.rect.x = 790             
            elif current_room_no == 4:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 790              
            elif current_room_no == 6:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 790  
            elif current_room_no == 8:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 790                  
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 790
        if player.rect.x > 801:
            if current_room_no == 1:
              current_room_no = 4
              current_room = rooms[current_room_no]
              player.rect.x = 60
            elif current_room_no == 2:
                current_room_no = 6
                current_room = rooms[current_room_no]
                player.rect.x = 60
            elif current_room_no == 3:
                current_room_no = 8
                current_room = rooms[current_room_no]
                player.rect.x = 60             
            elif current_room_no == 9:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.x = 60              
            elif current_room_no == 7:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.x = 60 
            elif current_room_no == 5:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.x = 60                  
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.x = 60
        if player.rect.y < -15:
            if current_room_no == 0:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.y = 550
            elif current_room_no == 1: 
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.y = 550
            elif current_room_no == 2:
                current_room_no = 3
                current_room = rooms[current_room_no]
                player.rect.y = 550
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.y = 790
        if player.rect.y > 601:
            if current_room_no == 0:
                player.rect.y = 60
            elif current_room_no == 2:
                current_room_no = 1
                current_room = rooms[current_room_no]
                player.rect.y = 60
            elif current_room_no == 3:
                current_room_no = 2
                current_room = rooms[current_room_no]
                player.rect.y = 60
            else:
                current_room_no = 0
                current_room = rooms[current_room_no]
                player.rect.y = 60
 
        # --- Drawing ---
        #screen.fill(BLACK)
        ## Change this to different backgrounds eventually
        if current_room_no == 0: #bedroom
          screen.fill(BLACK)
        elif current_room_no == 1: #cave one
          screen.fill(BLACK)
        elif current_room_no == 2: #cave two
          screen.fill(BLACK)
        elif current_room_no == 3: #cave three
          screen.fill(BLACK)
        elif current_room_no == 4: #world one
          screen.fill(BLACK)
        elif current_room_no == 5: #world two
          screen.fill(BLACK)
        elif current_room_no == 6: #world three
          screen.fill(BLACK)
        elif current_room_no == 7: #world four
          screen.fill(BLACK)
        elif current_room_no == 8: #world five
          screen.fill(BLACK)
        elif current_room_no == 9: #world six
          screen.fill(BLACK)
        
        current_room.wall_list.draw(screen)
        current_room.object_list.draw(screen)
        movingsprites.draw(screen)
        player.draw_hitbox(player.rect.x, player.rect.y)
        current_room.draw()
        
        new_room = Room_Bedroom()

        pygame.display.flip()
 
        clock.tick(60)
 
    pygame.quit()
 
if __name__ == "__main__":
    main()

from enum import Enum
import pygame
from pygame.locals import DOUBLEBUF

pygame.init()

DISPLAYSURF = pygame.display.set_mode((640, 480), DOUBLEBUF)
pygame.display.set_caption('Ducky: the Quest of the Baguette')

FPSCLOCK = pygame.time.Clock()

### MAP ###
map_data = [[1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1]]
            
wall = pygame.image.load('wall.png').convert_alpha()
grass = pygame.image.load('grass.png').convert_alpha()

TILEWIDTH = 64
TILEHEIGHT = 64
TILEHEIGHT_HALF = TILEHEIGHT / 2
TILEWIDTH_HALF = TILEWIDTH / 2

### CHARACTER ###
class Ducky:
    def __init__(self):
        self.DIRECTIONS = {'UP': 0, 'RIGHT': 1, 'DOWN': 2, 'LEFT': 3}
        self.SPRITES = {'UP': pygame.image.load('player_up.png').convert_alpha(),
                        'RIGHT': pygame.image.load('player_right.png').convert_alpha(),
                        'DOWN': pygame.image.load('player_down.png').convert_alpha(),
                        'LEFT': pygame.image.load('player_left.png').convert_alpha()}
                        
        self.i, self.j = 0, 0
        self.facing = self.DIRECTIONS['UP']
        self.sprite = self.SPRITES['UP']
    
    def blit(self):
        cart_x = self.j * TILEWIDTH_HALF
        cart_y = self.i * TILEHEIGHT_HALF
        iso_x = (cart_x - cart_y)
        iso_y = (cart_x + cart_y) / 2
        x = DISPLAYSURF.get_rect().centerx + iso_x
        y = DISPLAYSURF.get_rect().centery / 2 + iso_y
    
        DISPLAYSURF.blit(self.sprite, (x, y))
        
    def go_forward(self):
        if self.facing == self.DIRECTIONS['UP']:
            self.i -= 1
        if self.facing == self.DIRECTIONS['RIGHT']:
            self.j += 1
        if self.facing == self.DIRECTIONS['DOWN']:
            self.i += 1
        if self.facing == self.DIRECTIONS['LEFT']:
            self.j -= 1
            
    def turn_right(self):
        next_direction = list(self.DIRECTIONS.keys())[(self.facing + 1) % 4]
        self.facing = self.DIRECTIONS.get(next_direction)
        self.sprite = self.SPRITES.get(next_direction)
        
    def turn_left(self):
        next_direction = list(self.DIRECTIONS.keys())[(self.facing - 1) % 4]
        self.facing = self.DIRECTIONS.get(next_direction)
        self.sprite = self.SPRITES.get(next_direction)

### INITIALIZATION ###
ducky = Ducky()

### GAME LOOP ###
while True:
    DISPLAYSURF.fill((0, 0, 0))
    
    for j, row in enumerate(map_data):
        for i, tile in enumerate(row):
            tile_image = wall if tile == 1 else grass
            cart_x = j * TILEWIDTH_HALF
            cart_y = i * TILEHEIGHT_HALF  
            iso_x = (cart_x - cart_y) 
            iso_y = (cart_x + cart_y) / 2
            centered_x = DISPLAYSURF.get_rect().centerx + iso_x
            centered_y = DISPLAYSURF.get_rect().centery / 2 + iso_y
            DISPLAYSURF.blit(tile_image, (centered_x, centered_y))
    
    ducky.blit()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        key_pressed_is = pygame.key.get_pressed()
        
        if key_pressed_is[pygame.K_UP]:
            ducky.go_forward()
        if key_pressed_is[pygame.K_RIGHT]:
            ducky.turn_right()
        if key_pressed_is[pygame.K_LEFT]:
            ducky.turn_left()
    
    pygame.display.flip()
    FPSCLOCK.tick(30)
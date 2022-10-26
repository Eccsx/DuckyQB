from duckyqb import level
import pygame
from pygame.locals import DOUBLEBUF
import time

DISPLAYSURF = pygame.display.set_mode((640, 480), DOUBLEBUF)

TILEWIDTH, TILEHEIGHT = 68, 68
TILEHEIGHT_HALF, TILEWIDTH_HALF = TILEHEIGHT / 2, TILEWIDTH / 2

TIMESLEEP = 0.5

CHARACTER = None
LEVEL = {'map': None, 'start_position': None}

WALL = pygame.image.load('wall.png').convert_alpha()
GRASS = pygame.image.load('grass.png').convert_alpha()

def create():
    pygame.init()
    pygame.display.set_caption('Ducky: the Quest of the Baguette')
    
def update():
    DISPLAYSURF.fill((30, 30, 30))
    
    level.blit()
    CHARACTER.blit()
    
    pygame.display.flip()
    
    time.sleep(TIMESLEEP)
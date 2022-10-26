import time
import pygame
from duckyqb import level


DISPLAYSURF = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)

TILEWIDTH, TILEHEIGHT = 68, 68
TILEHEIGHT_HALF, TILEWIDTH_HALF = TILEHEIGHT / 2, TILEWIDTH / 2

TIMESLEEP = 0.5

CHARACTER = None
LEVEL = {"map": [], "start_position": (0, 0)}

WALL = pygame.image.load("wall.png").convert_alpha()
GRASS = pygame.image.load("grass.png").convert_alpha()


def create():
    pygame.init()
    pygame.display.set_caption("Ducky: the Quest of the Baguette")


def update():
    DISPLAYSURF.fill((30, 30, 30))

    level.blit()
    CHARACTER.blit()

    pygame.display.flip()

    time.sleep(TIMESLEEP)

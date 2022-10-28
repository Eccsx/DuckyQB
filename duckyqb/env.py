import time
import pygame
from duckyqb import level


DISPLAYSURF = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF)

LEVELWIDTH, LEVELHEIGHT = 11, 11
TILEWIDTH, TILEHEIGHT = 64, 32

TIMESLEEP = 0.5

LEVELPATH = "duckyqb/assets/levels"
TILEPATH = "duckyqb/assets/tiles"
CHARACTERPATH = "duckyqb/assets/characters"

CHARACTER = None
LEVEL = None

TILES = []


def create():
    pygame.init()
    pygame.display.set_caption("Ducky: the Quest of the Baguette")


def update():
    DISPLAYSURF.fill((60, 71, 75))
    level.blit()
    CHARACTER.blit()

    pygame.display.flip()
    time.sleep(TIMESLEEP)

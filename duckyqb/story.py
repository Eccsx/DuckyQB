from duckyqb import env
import pygame
import sys

def begins():
    env.create()
    
def ends():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         
import pygame
from duckyqb import env

def load():
    map_data = [[1, 1, 1, 1, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 0, 0, 0, 1],
                [1, 1, 1, 1, 1]]
    
    env.LEVEL['map'] = map_data
    env.LEVEL['start_position'] = (0, 0)
    
def blit():
    for j, row in enumerate(env.LEVEL['map']):
        for i, tile in enumerate(row):
            tile_image = env.WALL if tile == 1 else env.GRASS
            
            cart_x = j * env.TILEWIDTH_HALF
            cart_y = i * env.TILEHEIGHT_HALF
            
            iso_x = (cart_x - cart_y) 
            iso_y = (cart_x + cart_y) / 2
            
            centered_x = env.DISPLAYSURF.get_rect().centerx + iso_x
            centered_y = env.DISPLAYSURF.get_rect().centery / 2 + iso_y
            
            env.DISPLAYSURF.blit(tile_image, (centered_x, centered_y))
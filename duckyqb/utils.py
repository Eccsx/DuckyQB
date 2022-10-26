from duckyqb import env
import math


def cartesian_to_isometric(cart_x, cart_y):
    iso_x = (cart_x - cart_y) * env.TILEWIDTH / 2
    iso_y = (cart_x + cart_y) * env.TILEHEIGHT / 2

    iso_x += (
        env.DISPLAYSURF.get_rect().centerx
        - env.LEVELWIDTH / 2
        - env.TILEWIDTH / 2
    )
    iso_y += (
        env.DISPLAYSURF.get_rect().centery
        - env.LEVELHEIGHT / 2
        - env.TILEHEIGHT * (env.LEVELHEIGHT / 2)
    )

    return iso_x, iso_y

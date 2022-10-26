from duckyqb import env, utils


def load():
    map_data = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1],
    ]

    env.LEVEL["map"] = map_data
    env.LEVEL["start_position"] = (0, 0)


def blit():
    for j, row in enumerate(env.LEVEL["map"]):
        for i, tile in enumerate(row):
            tile_image = env.WALL if tile == 1 else env.GRASS

            iso_x, iso_y = utils.cartesian_to_isometric(i, j)

            env.DISPLAYSURF.blit(tile_image, (iso_x, iso_y))

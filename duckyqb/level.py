from duckyqb import env, utils
import os
import json
import pygame


def load(level_id):
    with open(os.path.join(env.TILEPATH, "tile_index.json"), "r") as f:
        for data in json.load(f):
            env.TILES.append(
                pygame.image.load(data["filename"]).convert_alpha()
            )

    with open(os.path.join(env.LEVELPATH, level_id + ".json"), "r") as f:
        env.LEVEL = json.load(f)


def blit():
    for j, row in enumerate(env.LEVEL["tiles"]):
        for i, tile in enumerate(row):
            tile_image = env.TILES[tile]

            iso_x, iso_y = utils.cartesian_to_isometric(i, j)

            env.DISPLAYSURF.blit(tile_image, (iso_x, iso_y))

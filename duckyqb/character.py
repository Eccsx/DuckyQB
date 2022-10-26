import pygame
from duckyqb import env


class Ducky:
    DIRECTIONS = {"UP": 0, "RIGHT": 1, "DOWN": 2, "LEFT": 3}
    SPRITES = {
        "UP": pygame.image.load("player_up.png").convert_alpha(),
        "RIGHT": pygame.image.load("player_right.png").convert_alpha(),
        "DOWN": pygame.image.load("player_down.png").convert_alpha(),
        "LEFT": pygame.image.load("player_left.png").convert_alpha(),
    }

    def update(func):
        def inner(self):
            func(self)
            env.update()

        return inner

    @update
    def __init__(self):
        self.i, self.j = env.LEVEL["start_position"]
        self.facing = self.DIRECTIONS["UP"]
        self.sprite = self.SPRITES["UP"]

        env.CHARACTER = self

    def blit(self):
        cart_x = self.j * env.TILEWIDTH_HALF
        cart_y = self.i * env.TILEHEIGHT_HALF
        iso_x = cart_x - cart_y
        iso_y = (cart_x + cart_y) / 2
        x = env.DISPLAYSURF.get_rect().centerx + iso_x
        y = env.DISPLAYSURF.get_rect().centery / 2 + iso_y

        env.DISPLAYSURF.blit(self.sprite, (x, y))

    @update
    def go_forward(self):
        if self.facing == self.DIRECTIONS["UP"]:
            self.i -= 1
        if self.facing == self.DIRECTIONS["RIGHT"]:
            self.j += 1
        if self.facing == self.DIRECTIONS["DOWN"]:
            self.i += 1
        if self.facing == self.DIRECTIONS["LEFT"]:
            self.j -= 1

    @update
    def turn_right(self):
        next_direction = list(self.DIRECTIONS.keys())[(self.facing + 1) % 4]
        self.facing = self.DIRECTIONS.get(next_direction)
        self.sprite = self.SPRITES.get(next_direction)

    @update
    def turn_left(self):
        next_direction = list(self.DIRECTIONS.keys())[(self.facing - 1) % 4]
        self.facing = self.DIRECTIONS.get(next_direction)
        self.sprite = self.SPRITES.get(next_direction)

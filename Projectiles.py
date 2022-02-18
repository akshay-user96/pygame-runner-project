import random

import pygame as pg
from pygame.math import Vector2
import util as ut
import constants as const

class Weapon(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.pos = Vector2(0.0, 0.0)
        self.vel = Vector2(0.0, 0.0)

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if not ut.check_if_within_screen_limit(self.pos.x, self.pos.y):
            self.kill()


class Bullet(Weapon):
    def __init__(self, screen_rect, start_x, start_y, start_vel_direction):
        super().__init__()
        radius = 2
        self.image = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)
        pg.draw.circle(self.image, const.COLOR_PLAYER_BULLET, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(start_x, start_y))
        self.vel = start_vel_direction * 30.0
        self.pos = Vector2(self.rect.center)
        self.screen_rect = screen_rect
        print(" created bullet at ", self.pos, self.vel, self.rect.center)

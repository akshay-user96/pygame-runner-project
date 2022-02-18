import random

import pygame as pg
from pygame.math import Vector2
import time
import util as ut
import sys
import constants as const


class Enemy(pg.sprite.Sprite):

    def __init__(self, screen_rect, radius):
        super().__init__()
        self.radius = radius
        self.value = 400
        self.image = pg.Surface((self.radius*2, self.radius*2), pg.SRCALPHA)
        pg.draw.circle(self.image, const.COLOR_ENEMY , (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center = (random.uniform(0, const.SCREEN_WIDTH),
                                                  random.uniform(0, const.SCREEN_LENGTH)))
        self.vel = Vector2(random.uniform(-1, 1), random.uniform(-1, 1))
        self.pos = Vector2(self.rect.center)
        self.screen_rect = screen_rect

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if not ut.check_if_within_screen_limit(self.pos.x, self.pos.y):
            self.kill()
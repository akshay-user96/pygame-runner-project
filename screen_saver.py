import random
import sys

import pygame as pg
from pygame.math import Vector2
import time
import Projectiles as pj
import util as ut
import Enemy as enem

### Reference : https://stackoverflow.com/questions/48711791/how-do-i-pass-a-rect-into-pygame-display-update-to-update-a-specific-area-of-t


SCREEN_WIDTH = 800
SCREEN_LENGTH = 600

import constants as const

class WarShip(pg.sprite.Sprite):
    def __init__(self, screen_rect):
        super().__init__()
        radius = 10
        self.speed = 2
        self.score = 0
        self.image = pg.Surface((radius*2, radius*2), pg.SRCALPHA)
        pg.draw.circle(self.image, const.COLOR_PLAYER , (radius, radius), radius)
        self.rect = self.image.get_rect(center=screen_rect.center)
        self.vel = Vector2(1.0, 0.0) * self.speed
        self.pos = Vector2(self.rect.center)
        self.screen_rect = screen_rect

    def turn(self, direction):
        self.vel = direction * self.speed

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if not ut.check_if_within_screen_limit(self.pos.x, self.pos.y):
            self.kill()
            print(" Game Over !! BattleShip out of range... ")
            sys.exit(0)

def create_battle(ship_sprite_group):
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_LENGTH))
    screen.fill((150, 255, 190))
    pg.display.update()
    screen_rect = screen.get_rect()
    # Pass this rect to `pg.display.update` to update only this area.
    #update_rect = pg.Rect(200, 1, 100, 200)
    warship = WarShip(screen_rect)
    ship_sprite_group.add(warship)
    ship_sprite_group.update()
    ship_sprite_group.draw(screen)
    print("a")
    print(len(ship_sprite_group))
    # Update only the area that we specified with the `update_rect`.
    pg.display.update()
    return screen, warship

def fire_weapon(weapon_sprite_group, screen_rect,start_x, start_y, start_velocity):
    weapon_sprite_group.add(pj.Bullet(screen_rect, start_x, start_y, start_velocity))

def create_enemies(enemy_sprite_group, screen_rect):
    num = int(random.uniform(-96,4))
    if(num < 0):
        return
    for i in range(0, num):
        enemy_sprite_group.add(enem.Enemy(screen_rect,random.uniform(10,30)))

def update_battle(all_sprites_groups, screen):
    screen.fill((10, 250, 25))
    for sprite_group in all_sprites_groups:
        sprite_group.update()
        sprite_group.draw(screen)
        print(" sprites in group ", len(sprite_group))
    # Update only the area that we specified with the `update_rect`.
    pg.display.update()

def check_collisons(all_sprites):
    ## check if any bullet and enemy collided
    score = 0
    shoots_into_enemies = pg.sprite.groupcollide(all_sprites[2], all_sprites[1], True, True)
    for enemy in shoots_into_enemies:
        score = score + enemy.value
    collisions_to_enemies = pg.sprite.groupcollide(all_sprites[0], all_sprites[2], True, True)
    if len(collisions_to_enemies) > 0:
        print(" collided with enemy .. Game Over !!! ")
        sys.exit(0)
    return score

def main():
    sprite_groups = []
    ship_sprite_group = pg.sprite.Group()
    weapon_sprite_group = pg.sprite.Group()
    enemy_sprite_group = pg.sprite.Group()
    sprite_groups.append(ship_sprite_group)
    sprite_groups.append(weapon_sprite_group)
    sprite_groups.append(enemy_sprite_group)
    screen, warship = create_battle(ship_sprite_group)
    clock = pg.time.Clock()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    print("Fire Bullet ... ")
                    fire_weapon(weapon_sprite_group, screen, warship.pos.x, warship.pos.y, warship.vel/warship.vel.length())
                elif event.key == pg.K_a:
                    print(" Turning left ... ")
                    warship.turn(Vector2(-1.0, 0.0))
                elif event.key == pg.K_d:
                    print(" Turning right ... ")
                    warship.turn(Vector2(1.0, 0.0))
                elif event.key == pg.K_s:
                    print(" Turning Up ... ")
                    warship.turn(Vector2(0.0, 1.0))
                elif event.key == pg.K_w:
                    print(" Turning Down ... ")
                    warship.turn(Vector2(0.0, -1.0))

        create_enemies(enemy_sprite_group,screen)
        value_received = check_collisons(sprite_groups)
        warship.score = warship.score + value_received
        print(" current _ score" , warship.score)
        update_battle(sprite_groups, screen)
        clock.tick(20)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()




















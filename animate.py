#! /usr/bin/python
import sys

import pygame
from pygame.locals import *

from animated_sprite import AnimatedSprite

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player_animations = {
    "running": AnimatedSprite("imgs", "L", 9, fps=3),
    "standing": AnimatedSprite("imgs", "standing", 1),
}
x = 0
y = 0
vel = 3
current_player_animation = "running"

while True:
    clock.tick(60)
    screen.fill((23, 174, 174))

    animation = player_animations[current_player_animation]

    animation.draw(screen, (x, y))

    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        current_player_animation = "running"
        x += vel
        animation.flipX = True
    elif keys[K_LEFT]:
        current_player_animation = "running"
        x -= vel
        animation.flipX = False
    else:
        current_player_animation = "standing"

    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    pygame.display.update()

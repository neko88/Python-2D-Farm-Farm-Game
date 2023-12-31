import pygame
from settings import *
from pytmx.util_pygame import load_pygame
from random import randint


class Sprite(pygame.sprite.Sprite):
    def __init__(self, position, surface, groups, z=LAYERS['main']):
        super().__init__(groups)

        self.image = surface
        self.rect = self.image.get_rect(topleft=position)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)


class Water(Sprite):
    def __init__(self, position, frames, groups, z=LAYERS['water']):
        ## Sprite setup
        ## Frames is indexed because the water will be animated (each as a Sprite)
        ## Animation setup
        self.frames = frames
        self.frames_index = 0

        super().__init__(position, self.frames[self.frames_index], groups, z)

    def animate(self, dt):
        self.frames_index += 5 * dt
        if self.frames_index >= len(self.frames):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]

    def update(self, dt):
        self.animate(dt)


class WildFlower(Sprite):
    def __init__(self, position, surface, groups):
        super().__init__(position, surface, groups)
        self.hitbox = self.rect.copy().inflate(-20, -self.rect.height * 0.9)

class Tree(Sprite):
    def __init__(self, position, surface, groups, name):
        super().__init__(position, surface, groups)
        # inherits the hitbox from Srite

        self.apples_surf = pygame.image.load(APPLES_PATH)
        self.apple_pos = APPLES_POS[name]
        self.apple_sprites = pygame.sprite.Group()

    def create_fruit(self):
        for pos in self.apple_pos:
            if randint(0, 10) < 2:
                x = self.rect.left + pos[0]  # left side of tree + apple position x
                y = self.rect.top + pos[1]   # top side of tree + apple position y
                Sprite((x, y), self.apples_surf, [self.apple_sprites, self.groups()[0]])    ## all the groups that the tree sprite is in, pick the first group index (all_sprites)
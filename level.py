import pygame
from settings import *
from player import Player
from settings import *
from overlay import *
from sprites import Sprite


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = CameraGroup()
        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        Sprite(
            pos=(0, 0),
            surf=pygame.image.load(BG_PATH).convert_alpha(),
            groups=self.all_sprites)

        self.player = Player((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), self.all_sprites)

    def run(self, dt):
        # DELETE:
        self.all_sprites.draw()
        self.all_sprites.update(dt)  ## From pygame.sprite
        self.overlay.display()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()

    def draw(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image, sprite.rect)

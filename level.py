import pygame
from settings import *
from player import Player
from constants import *


class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()
        self.all_sprites = pygame.sprite.Group()
        self.setup()

    def setup(self):
        self.player = Player((SCREEN_WIDTH//2,SCREEN_HEIGHT//2), self.all_sprites)

        ### DELETE BELOW
        bg_image = pygame.image.load(BG_PATH).convert_alpha()
        self.surf = pygame.Surface.convert_alpha(bg_image)
        self.surf = pygame.transform.scale(self.surf, (self.surf.get_width()//2,self.surf.get_height()//2)).convert_alpha()

    def run(self,dt):
        #DELETE:
        self.display_surface.blit(self.surf,(0,0))

       #self.display_surface.fill('black')
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)

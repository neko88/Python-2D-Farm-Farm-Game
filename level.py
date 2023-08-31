import pygame
from settings import *
from player import Player
from support import *
from overlay import *
from sprites import *
from pytmx.util_pygame import load_pygame

class Level:
    def __init__(self):
        self.all_sprites = CameraGroup()
        self.collision_sprites = pygame.sprite.Group()

        self.background = None
        self.display_surface = pygame.display.get_surface()
        self.setup()
        self.overlay = Overlay(self.player)

    def setup(self):
        self.background = Sprite((0,0), pygame.image.load(BG_PATH).convert_alpha(),self.all_sprites, z=LAYERS['ground'])
        self.tmx_data = load_pygame(MAP_PATH)
        self.draw_layer(PLAYER, self.all_sprites, self.collision_sprites)
        self.draw_layer(LAYER, self.all_sprites, ['HouseFloor', 'HouseFurnitureBottom'], 'house bottom')
        self.draw_layer(LAYER, self.all_sprites, ['HouseWalls', 'HouseFurnitureTop'], 'main')
        self.draw_layer(LAYER, [self.all_sprites, self.collision_sprites], ['Fence'], 'main')
        self.draw_layer(WATER, self.all_sprites)
        self.draw_layer(WILD_PLANT, self.all_sprites)
        self.draw_layer(TREE, [self.all_sprites, self.collision_sprites])
        self.draw_layer(COLLISION, self.collision_sprites)


    def run(self, dt):
        self.all_sprites.draw(self.player)
        self.all_sprites.update(dt)  ## From pygame.sprite
        self.overlay.display()

    def draw_layer(self, layer_type, group, layer_name=None, layer_category=None):
        layer_type = layer_type.lower()
        if layer_type == LAYER:
            for lay_name in layer_name:
                for x, y, surf in self.tmx_data.get_layer_by_name(lay_name).tiles():  ## get all tiles of this layer
                    Sprite((x * TILE_SIZE, y * TILE_SIZE), surf, group, LAYERS[layer_category])  # Creat

        elif layer_type == WATER:
            water_frames = import_folder(WATER_PATH)
            for x, y, surf in self.tmx_data.get_layer_by_name('Water').tiles():  ## get all tiles of this layer
                Water((x * TILE_SIZE, y * TILE_SIZE), water_frames, group, LAYERS[WATER])

        elif layer_type == WILD_PLANT:
            for obj in self.tmx_data.get_layer_by_name('Decoration'):
                WildFlower((obj.x, obj.y), obj.image, group)        ## Deco layer has absolute (x,y) vals

        elif layer_type == TREE:
            for obj in self.tmx_data.get_layer_by_name('Trees'):
                Tree((obj.x, obj.y), obj.image, group, obj.name)    ## Tree layer has abs (x,y)

        elif layer_type == PLAYER:
            for obj in self.tmx_data.get_layer_by_name('Player'):
                if obj.name == 'Start':
                    self.player = Player((obj.x, obj.y), group, self.collision_sprites)

        elif layer_type == COLLISION:
            for x, y, surf in self.tmx_data.get_layer_by_name('Collision').tiles():
                Sprite((x * TILE_SIZE, y * TILE_SIZE), pygame.Surface((TILE_SIZE, TILE_SIZE)), self.collision_sprites) ## Empty surface so that it is invisible on screen

## CameraGroup is pygame sprite class ***
class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def draw(self, player):
        self.offset.x = player.rect.centerx - (SCREEN_WIDTH/2)
        self.offset.y = player.rect.centery - (SCREEN_HEIGHT/2)

        for layer in LAYERS.values():
            for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
                if sprite.z == layer:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)    #image gets drawn at the rect

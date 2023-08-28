import pygame
from settings import *
from constants import *
from support import *


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.import_assets()

        self.status = UP
        self.frame_index = 0

        ## General setup
        self.image = self.animations[self.status][self.frame_index]
        self.rect = self.image.get_rect(center=pos)

        ## Movement
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = PLAYER_SPEED

        ## Tools
        self.selected_tool = AXE


    def import_assets(self):
        ## Dictionary storing { 'folder_name' : ['img1.png', 'img2.png] } access by 'folder_name'
        self.animations = {UP: [], DOWN: [], LEFT: [], RIGHT: [],
                           RIGHT+IDLE: [], LEFT+IDLE: [], UP+IDLE: [], DOWN+IDLE: [],
                           RIGHT+HOE: [], LEFT+HOE: [], UP+HOE: [], DOWN+HOE: [],
                           RIGHT+AXE: [], LEFT+AXE: [], UP+AXE: [], DOWN+AXE: [],
                           RIGHT+WATER: [], LEFT+WATER: [], UP+WATER: [], DOWN+WATER: []}

        for animation in self.animations.keys():
            full_path = 'assets/s2 - basic player/graphics/character/' + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self, dt):
        self.frame_index += 4 * dt
        if self.frame_index >= len(self.animations[self.status]):
            self.frame_index = 0
        self.image = self.animations[self.status][int(self.frame_index)]

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.status = UP
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.status = DOWN
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.status = RIGHT
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.status = LEFT
        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE]:
            s=0
        #timer for tool use


    def get_status(self):
        # if the player is not moving
        if self.direction.magnitude() == 0:
            # add _idle to the status
            self.status = self.status.split('_')[0] + IDLE

    def move(self, dt):
        ## Normalize the vector movement
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        ## Horizontal movement:
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        ## Vertical movement:
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def update(self, dt):
        self.input()
        self.move(dt)  ## This is the FR independency!
        self.get_status()
        self.animate(dt)

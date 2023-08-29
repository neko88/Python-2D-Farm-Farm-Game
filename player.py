import pygame
from settings import *
from constants import *
from support import *
from timer import *
from item import *

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

        ## Timers
        self.timers = {
            TOOL_USE_TIMER : Timer(350, self.use_tool),
            TOOL_SWITCH_TIMER: Timer(200)
        }

        ## Tools
        self.tools = Item(TOOLS)
        self.selected_tool = self.tools.get(WATER)


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

        if not self.timers[TOOL_USE_TIMER].active:      # move only if not using tool
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

            ## Use Tool
            if keys[pygame.K_SPACE]:
                self.timers[TOOL_USE_TIMER].activate()
                self.direction = pygame.math.Vector2()      # Stops the player movement in a direction
                self.frame_index = 0

            ## Switch Tool
            if keys[pygame.K_m] and not self.timers[TOOL_SWITCH_TIMER].active:
                self.timers[TOOL_SWITCH_TIMER].activate()
                self.selected_tool = self.tools.get_next()


    def move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()     ## Normalize the vector movement

        ## Horizontal movement:
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = self.pos.x

        ## Vertical movement:
        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = self.pos.y

    def get_status(self):
        # if the player is not moving
        if self.direction.magnitude() == 0:
            # add _idle to the status
            self.status = self.status.split('_')[0] + IDLE

        if self.timers[TOOL_USE_TIMER].active:
            self.status = self.status.split('_')[0] + self.selected_tool

    def use_tool(self):
        print("")

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        self.input()
        self.move(dt)  ## This is the FR independency!
        self.get_status()
        self.update_timers()
        self.animate(dt)

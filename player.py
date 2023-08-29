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

        self.status = DOWN
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
            TOOL_SWITCH_TIMER: Timer(200),
            SEED_USE_TIMER : Timer(350, self.use_tool),
            SEED_SWITCH_TIMER: Timer(200)
        }

        ## Tools
        self.tools = Item(TOOLS)
        self.selected_tool = self.tools.get(WATER)

        self.seeds = Item(SEEDS)
        self.selected_seed = self.seeds.get(CORN)


    def import_assets(self):
        ## Dictionary storing { 'folder_name' : ['img1.png', 'img2.png] } access by 'folder_name'
        self.animations = {UP: [], DOWN: [], LEFT: [], RIGHT: [],
                           RIGHT+'_'+IDLE: [], LEFT+'_'+IDLE: [], UP+'_'+IDLE: [], DOWN+'_'+IDLE: [],
                           RIGHT+'_'+HOE: [], LEFT+'_'+HOE: [], UP+'_'+HOE: [], DOWN+'_'+HOE: [],
                           RIGHT+'_'+AXE: [], LEFT+'_'+AXE: [], UP+'_'+AXE: [], DOWN+'_'+AXE: [],
                           RIGHT+'_'+WATER: [], LEFT+'_'+WATER: [], UP+'_'+WATER: [], DOWN+'_'+WATER: []}

        for animation in self.animations.keys():
            full_path = CHARACTER_PATH + animation
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

        if keys[pygame.K_SPACE] and not self.timers[TOOL_USE_TIMER].active:
            self.tool(USE)
        if keys[pygame.K_q] and not self.timers[TOOL_SWITCH_TIMER].active:
            self.tool(SWITCH)
        if keys[pygame.K_v] and not self.timers[SEED_USE_TIMER].active:
            self.seed(USE)
        if keys[pygame.K_e] and not self.timers[SEED_SWITCH_TIMER].active:
            self.seed(SWITCH)

    def tool(self, action):
        ## Use Tool
        if action == USE:
            self.timers[TOOL_USE_TIMER].deactivate()
            self.timers[TOOL_USE_TIMER].activate()
            self.direction = pygame.math.Vector2()  # Stops the player movement in a direction
            self.frame_index = 0
        elif action == SWITCH:
            self.timers[TOOL_SWITCH_TIMER].activate()
            self.selected_tool = self.tools.get_next()

    def seed(self, action):
        if action == USE:
            self.timers[SEED_USE_TIMER].activate()
            self.direction = pygame.math.Vector2()  # Stops the player movement in a direction
            self.frame_index = 0
        elif action == SWITCH:
            self.timers[SEED_SWITCH_TIMER].activate()
            self.selected_seed = self.seeds.get_next()



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
            self.status = self.status.split('_')[0] + '_' + IDLE

        if self.timers[TOOL_USE_TIMER].active:
            self.status = self.status.split('_')[0] + '_' + self.selected_tool

    def use_tool(self):
        var = None

    def update_timers(self):
        for timer in self.timers.values():
            timer.update()

    def update(self, dt):
        self.input()
        self.move(dt)  ## This is the FR independency!
        self.get_status()
        self.update_timers()
        self.animate(dt)

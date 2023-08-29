import pygame
from settings import *
from constants import *

class Overlay:
    def __init__(self, player):
        self.display_surface = pygame.display.get_surface()
        self.player = player

        #imports
        self.tools_surf = {tool: pygame.image.load(f'{TOOL_PATH}{tool}' + '.png').convert_alpha() for tool in player.tools.item_list}
        self.seeds_surf = {seed: pygame.image.load(f'{SEED_PATH}{seed}' + '.png').convert_alpha() for seed in player.seeds.item_list}

    def display(self):
        tool_surf = self.tools_surf[self.player.selected_tool]
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

PLAYER_SPEED = 200

CHARACTER_PATH = 'assets/graphics/character/'
TOOL_PATH = 'assets/graphics/overlay/tool/'
SEED_PATH = 'assets/graphics/overlay/seed/'
BG_PATH = 'assets/graphics/world/ground.png'

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'
IDLE = 'idle'

USE = 'use'
SWITCH = 'switch'

HOE = 'hoe'
AXE = 'axe'
WATER = 'water'
TOOLS = {HOE, AXE, WATER}
TOOL_USE_TIMER = 'tool use timer'
TOOL_SWITCH_TIMER = 'tool switch timer'

CORN = 'corn'
TOMATO = 'tomato'
SEEDS = {CORN, TOMATO}
SEED_USE_TIMER = 'seed use timer'
SEED_SWITCH_TIMER = 'seed switch timer'

OVERLAY_POSITIONS = {
    'tools': (40, SCREEN_HEIGHT - 15),
    'seeds': (70, SCREEN_HEIGHT - 5)
}

LAYERS = {
    'water': 0,
    'ground': 1,
    'soil': 2,
    'soil water': 3,
    'rain floor': 4,
    'house bottom': 5,
    'ground plant': 6,
    'main': 7,
    'house top': 8,
    'fruit': 9,
    'rain drops': 10
}
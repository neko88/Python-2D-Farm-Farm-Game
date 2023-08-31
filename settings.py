SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
TILE_SIZE = 64

PLAYER_SPEED = 500
PLAYER = 'player'

CHARACTER_PATH = 'assets/graphics/character/'
TOOL_PATH = 'assets/graphics/overlay/tool/'
SEED_PATH = 'assets/graphics/overlay/seed/'
BG_PATH = 'assets/graphics/world/ground.png'
MAP_PATH = 'assets/data/map.tmx'
WATER_PATH = 'assets/graphics/water/'
APPLES_PATH = 'assets/graphics/fruit/apple.png'

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

LAYER = 'layer'
GROUND = 'ground'
SOIL = 'soil'
RAIN = 'rain'
FLOOR = 'floor'
FENCE = 'fence'
HOUSE = 'house'
BOTTOM = 'bottom'
TOP = 'top'
PLANT = 'plant'
WILD_PLANT = 'wild plant'
FRUIT = 'fruit'
RAINDROPS = 'rain drops'
TREE = 'tree'
COLLISION = 'collision'
SMALL = 'small'
LARGE = 'large'

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
## Values are (x, y) for the location on the Tree's rect, not screen
APPLES_POS = {
    SMALL: [ (18,17), (30,37), (12,50), (30,45), (20,30), (30,10) ],
    LARGE: [ (30,24), (60,65), (50,50), (16,40), (45,50), (42,70) ]
}
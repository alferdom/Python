import pyglet
from .State import *
from .StateAstar import *
from pathlib import Path
from argparse import ArgumentParser as Ap

# parser definition for arguments to define game behavior before playing
parser = Ap(description="Snake game: User controlling Snake type game extended with Astar pathfinding algorithm.",
            epilog="OPTIONAL ARGUMENT: speed, size, fullscreen, astar")

parser.add_argument("-s", "--size", help="Define size of images", action='store', dest='size', default=1,
                    type=int, metavar='INT')

parser.add_argument("-v", "--velocity", help="Set the velocity of the Snake.", action='store', dest='velocity',
                    default=1,
                    type=int, metavar='INT')

parser.add_argument("-f", "--fullscreen", help="Turn the game in fullscreen mode.", action='store_true',
                    dest='fullscreen')
parser.add_argument("--astar", "-a", help="Play the game with A* pathfinding algorithm.", action='store_true',
                    dest='astar')
parser.add_argument("--wall", "-w", help="Turn on arena wall.", action='store_true', dest='wall')
args = parser.parse_args()

# get path for snake body images and size of pixels
TILE_SIZE = int(50 * (1.0 + (args.size / 2 - 0.5)))

# start game in fullscreen/window mode
config = pyglet.gl.Config(double_buffer=True)
window = pyglet.window.Window(fullscreen=args.fullscreen, config=config)

# choose which object to create and work with
if not args.astar:
    state = State(window.width // TILE_SIZE, window.height // TILE_SIZE, args.wall)
else:
    state = StateAstar(window.width // TILE_SIZE, window.height // TILE_SIZE)

# text labels definitions and positions
endLabel = pyglet.text.Label("", font_name='Arial', font_size=TILE_SIZE, x=(window.width // 2),
                             y=(window.height // 2), anchor_x='center', anchor_y='center', color=(255, 0, 0, 255))

endScoreLabel = pyglet.text.Label("", font_name='Arial', font_size=TILE_SIZE,
                                  x=(window.width // 2) - TILE_SIZE - 5, y=(window.height // 2) - TILE_SIZE - 5,
                                  anchor_x='center', anchor_y='center', color=(0, 255, 255, 255))

score = pyglet.text.Label("0", font_name='Times New Roman', font_size=TILE_SIZE // 2,
                          x=(window.width // 10), y=(window.height // 10), color=(255, 255, 0, 255))
# load audio options and game sounds
pyglet.options['audio'] = ('openal', 'pulse', 'directsound', 'silent')
death_sound = pyglet.media.load('SnakePYT/Audio/roblox-death-sound-effect.mp3')
eat_sound = pyglet.media.load('SnakePYT/Audio/eatingnoises.mp3')

# load snake body parts and rest game images
SNAKE_DIR = Path('SnakePYT/Image/snake-tiles')
snake_tiles = {}
for path in SNAKE_DIR.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)

apple_image = pyglet.image.load('SnakePYT/Image/apple.png')
grass_image = pyglet.image.load('SnakePYT/Image/grass.jpg')

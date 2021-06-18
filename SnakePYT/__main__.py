from .windowFunc import *


# turn on game with define velocity of snake movement
def main():
    pyglet.clock.schedule_interval(move, 1 / (args.velocity + 5))
    pyglet.app.run()


if __name__ == '__main__':
    main()

from .config import *


# resizing to fullscreen or back to window mode
def go_fullscreen():
    global TILE_SIZE
    # changing size of pixels for images and labels
    if not window.fullscreen:
        window.set_fullscreen(True)
        TILE_SIZE = TILE_SIZE * 2
        labelSIZE = 100
    else:
        window.set_fullscreen(False)
        TILE_SIZE = TILE_SIZE // 2
        labelSIZE = 50

    # get new width and length for snake and food
    new_width = window.width // TILE_SIZE
    new_height = window.height // TILE_SIZE
    state.food[0] = (int(state.food[0][0] / (state.width / new_width)),
                     int(state.food[0][1] / (state.height / new_height)))
    state.width = new_width
    state.height = new_height
    # resizing and repositioning labels
    endLabel.x = (window.width // 2)
    endLabel.y = (window.height // 2)
    endLabel.font_size = labelSIZE
    score.x = (window.width // 10)
    score.y = (window.height // 10)
    score.font_size = labelSIZE // 2
    endScoreLabel.x = (window.width // 2) - labelSIZE - 5
    endScoreLabel.y = (window.height // 2) - labelSIZE - 5
    endScoreLabel.font_size = labelSIZE
    return TILE_SIZE


# func to draw images on screen
@window.event
def on_draw():
    window.clear()
    # get sharper image displaying
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
    # background draw
    grass_image.blit(0, 0, width=window.width, height=window.height)
    # snake body draw
    for x, y in state.snake[:-1]:
        snake_tiles['end-end'].blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)
    x, y = state.snake[-1]
    # snake head draw
    snake_tiles["fronthead"].blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)
    # food draw
    for x, y in state.food:
        apple_image.blit(x * TILE_SIZE, y * TILE_SIZE, width=TILE_SIZE, height=TILE_SIZE)
    # labels draw
    endLabel.draw()
    score.text = str(state.score)
    score.draw()
    endScoreLabel.draw()


@window.event
# when window is closed
def on_close():
    print("Your score:", state.score)


# func to get key input from player
# snake controlling keys disabled when A* is active
@window.event
def on_key_press(key_code, modifier):
    if not args.astar:
        if key_code == pyglet.window.key.LEFT:
            new_direction = -1, 0
            state.pushed_buttons.append(new_direction)
        if key_code == pyglet.window.key.RIGHT:
            new_direction = 1, 0
            state.pushed_buttons.append(new_direction)
        if key_code == pyglet.window.key.UP:
            new_direction = 0, 1
            state.pushed_buttons.append(new_direction)
        if key_code == pyglet.window.key.DOWN:
            new_direction = 0, -1
            state.pushed_buttons.append(new_direction)
        # close window and end the game
    if key_code == pyglet.window.key.ESCAPE:
        pyglet.app.exit()
        print("Game closed")
        return 0
        # turn on and off fullscreen
    if key_code == pyglet.window.key.ENTER:
        global TILE_SIZE
        TILE_SIZE = go_fullscreen()


# func to get snake position every new frame and define text labels and play sound when food was eaten
def move(dt):
    if state.move == 'END':
        if endLabel.text != 'GAME OVER':
            death_sound.play()
        endLabel.text = 'GAME OVER'
        endScoreLabel.text = '      Score: ' + str(state.score)

    if state.score != int(score.text):
        eat_sound.play()

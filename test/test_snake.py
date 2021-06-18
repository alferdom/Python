import pytest
import pyglet
import argparse
from SnakePYT import State, windowFunc, config, Astar, StateAstar


def test_state_class():
    state = State.State(10, 10, False)
    assert state.snake_alive
    assert state.food
    assert (5, 5) in state.snake


def test_enable_wall():
    state = State.State(10, 10, True)
    assert state.wall


def test_snake_dead():
    state = State.State(10, 10, True)
    state.snake_alive = False
    assert state.move == 'END'


def test_bump_to_wall():
    state = State.State(10, 10, True)
    state.snake = [(10, 0)]
    state.move
    assert not state.snake_alive
    assert state.move == 'END'


def test_move_behind_wall():
    state = State.State(10, 10, False)
    state.snake.append((10, 10))
    state.snake_direction = 1, 0
    state.move
    state.food[0] = (0, 0)
    snakeposition = (1, 0)
    assert snakeposition == state.snake[-1]
    assert len(state.snake) == 2


def test_eaten_food():
    state = State.State(10, 10, False)
    state.snake_direction = 1, 0
    state.food.append((6, 5))
    state.move
    assert state.score == 1


def test_create_food():
    state = State.State(10, 10, False)
    for i in range(1000):
        state.add_food()
        assert state.food[-1] < (state.width, state.height)


def test_starting_position():
    width = 15
    height = 12
    state = State.State(width, height, False)
    assert width > state.snake[0][0] >= 0
    assert height > state.snake[0][1] >= 0


def test_game_end():
    ret = windowFunc.on_key_press(pyglet.window.key.ESCAPE, False)
    assert not ret


def test_astar_found():
    start = 0, 0
    end = 10, 5
    arenawidth = 15
    arenaheight = 15
    ret = Astar.astar(start, end, start, arenawidth, arenaheight)
    assert ret


def test_astar_not_found():
    start = 0, 0
    end = 10, 5
    arenawidth = 5
    arenaheight = 5
    ret = Astar.astar(start, end, start, arenawidth, arenaheight)
    assert ret is None


def test_astar_path():
    start = 0, 0
    end = 2, 2
    arenawidth = 15
    arenaheight = 15
    ret = Astar.astar(start, end, start, arenawidth, arenaheight)
    path = [(0, 0), (0, 1), (1, 1), (1, 2), (2, 2)]
    assert ret == path


def test_class_astar():
    state = StateAstar.StateAstar(10, 10)
    assert len(state.path) > 1

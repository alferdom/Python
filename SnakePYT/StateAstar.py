import random
from .Astar import *


class StateAstar:
    """
        State class for finding snake path with A*
        """

    def __init__(self, width, heigth):
        self.width = width
        self.height = heigth
        self.snake = [(self.width // 2, self.height // 2)]
        self.food = []
        self.add_food()
        self.snake_alive = True
        self.score = 0
        self.path = astar(self.snake[0], self.food[0], self.snake, self.width, self.height)

    # movement definition
    @property
    def move(self):
        # no path found
        if not self.path:
            self.snake_alive = False
            return "END"

        # get new coordinates
        new_x = self.path[0][0]
        new_y = self.path[0][1]
        new_head = new_x, new_y
        del self.path[0]

        # append new coordinates
        self.snake.append(new_head)

        # if snake head reach the food
        if new_head in self.food:
            self.food.remove(new_head)
            self.add_food()
            self.score += 1
            self.path = astar(self.snake[-1], self.food[-1], self.snake, self.width, self.height)
        else:
            del self.snake[0]

    # adding new food
    def add_food(self):
        # try if food spawns at an empty position
        for try_number in range(100):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake) and (position not in self.food):
                self.food.append(position)
                return

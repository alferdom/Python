import random


class State:
    """
      State class for snake snake movement and food creation
      """

    def __init__(self, width, heigth, wall=False):
        self.width = width
        self.height = heigth
        self.snake = [(self.width // 2, self.height // 2)]
        self.snake_direction = 1, 0
        self.food = []
        self.add_food()
        self.snake_alive = True
        self.wall = wall
        self.pushed_buttons = []
        self.score = 0

    # movement definition
    @property
    def move(self):
        # if snake is dead
        if not self.snake_alive:
            return "END"

        # if more keys were pushed
        if self.pushed_buttons:
            new_direction = self.pushed_buttons[0]
            del self.pushed_buttons[0]
            old_x, old_y = self.snake_direction
            new_x, new_y = new_direction
            if (old_x, old_y) != (-new_x, -new_y):
                self.snake_direction = new_direction

        # if wall is present
        if not self.wall:
            new_x = (self.snake[-1][0] + self.snake_direction[0]) % self.width
            new_y = (self.snake[-1][1] + self.snake_direction[1]) % self.height
        else:
            new_x = self.snake[-1][0] + self.snake_direction[0]
            new_y = self.snake[-1][1] + self.snake_direction[1]

            if new_x < 0:
                self.snake_alive = False

            if new_y < 0:
                self.snake_alive = False

            if new_x >= self.width:
                self.snake_alive = False

            if new_y >= self.height:
                self.snake_alive = False

        # get new coordinates
        new_head = new_x, new_y
        # if snake get to himself
        if new_head in self.snake:
            self.snake_alive = False

        # append new coordinates
        self.snake.append(new_head)
        # if snake head reach the food
        if new_head in self.food:
            self.food.remove(new_head)
            self.add_food()
            self.score += 1
        else:
            del self.snake[0]

        # no food created
        if not self.food:
            self.add_food()

    # adding new food
    def add_food(self):
        # try if food spawns at an empty position
        for try_number in range(100):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake) and (position not in self.food):
                self.food.append(position)
            return 1

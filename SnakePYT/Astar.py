import heapq


class Node:
    """
    A node class for A* Pathfinding
    """

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position

    # defining less than for heap queue
    def __lt__(self, other):
        return self.f < other.f

    # defining greater than for heap queue
    def __gt__(self, other):
        return self.f > other.f


def return_path(current_node):
    path = []
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    # return reversed path
    return path[::-1]


def astar(start, end, snakepos, arenawidth, arenaheight):
    # create start and end node
    start_node = Node(None, start)
    end_node = Node(None, end)

    # initialize both open and closed list
    open_list = []
    closed_list = []

    # heapify the open_list and Add the start node
    heapq.heapify(open_list)
    heapq.heappush(open_list, start_node)

    # nodes around current node do we search
    squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)

    # while until the end is found
    while len(open_list) > 0:

        # get the current node
        current_node = heapq.heappop(open_list)
        closed_list.append(current_node)

        # if we reached the goal
        if current_node == end_node:
            return return_path(current_node)

        # initialize children
        children = []

        # search around curr node
        for new_position in squares:

            # get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # search if node is in arena range and not in snake position
            if node_position[0] < 0 or node_position[1] < 0 or node_position[0] >= arenawidth \
                    or node_position[1] > arenaheight or node_position in snakepos:
                continue

            # create new node
            new_node = Node(current_node, node_position)

            # append node
            children.append(new_node)

        # loop through children
        for child in children:
            # if child is on the closed list
            if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                continue

            # create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                    (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # define if child is already in the open list
            for i in range(len(open_list)):
                if child.position == open_list[i].position:
                    if child.g >= open_list[i].g:
                        continue
                    else:
                        open_list[i] = open_list[-1]
                        open_list.pop()
                        if i < len(open_list):
                            sorted(open_list, reverse=False)
                    break

            # add the child to the open list
            heapq.heappush(open_list, child)
    # when we path not found
    print("No path to a destination")
    return None

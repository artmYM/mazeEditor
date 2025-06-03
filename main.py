'''
maze generation and pathfinding using recursive backtracking and A* algorithm
--------------------------------------------------------------------------------

'''

import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from collections import deque
from heapq import heappop, heappush
from matplotlib.widgets import Button, TextBox

class Maze:
    def __init__(self, size):
        # Initialize the maze with walls
        self.width = size
        self.height = size
        self.maze = [[1] * size for _ in range(size)]
        self.visited = [[False] * size for _ in range(size)]
        self.directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def generate_maze(self, x=0, y=0):
        # Mark the starting cell as visited and create a path
        self.visited[y][x] = True
        self.maze[y][x] = 0

        # Randomize directions
        directions = self.directions[:]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2

            # Check if the new cell is within bounds and not visited
            if 0 <= nx < self.width and 0 <= ny < self.height and not self.visited[ny][nx]:
                # Carve a path to the new cell and visit it
                self.maze[y + dy][x + dx] = 0
                self.generate_maze(nx, ny)

    def create_entrance_and_exit(self):
        self.maze[0][0] = 0  # Start point
        self.maze[self.height - 1][self.width - 1] = 0  # End point

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def find_shortest_path(self):
        start = (0, 0)
        end = (self.height - 1, self.width - 1)
        open_set = []
        heappush(open_set, (0, start))
        came_from = {}
        g_cost = {start: 0}
        f_cost = {start: self.heuristic(start, end)}

        while open_set:
            current = heappop(open_set)[1]

            if current == end:
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path

            for dx, dy in self.directions:
                neighbor = (current[0] + dx, current[1] + dy)
                tentative_g_cost = g_cost[current] + 1

                if 0 <= neighbor[0] < self.width and 0 <= neighbor[1] < self.height and self.maze[neighbor[1]][neighbor[0]] == 0:
                    if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                        came_from[neighbor] = current
                        g_cost[neighbor] = tentative_g_cost
                        f_cost[neighbor] = tentative_g_cost + self.heuristic(neighbor, end)
                        heappush(open_set, (f_cost[neighbor], neighbor))

        return []

    def display_maze(self, path=None):
        cmap = mcolors.ListedColormap(['white', 'black', 'red'])
        display_maze = [[self.maze[y][x] for x in range(self.width)] for y in range(self.height)]

        if path:
            for (x, y) in path:
                display_maze[y][x] = 2  # Mark the path in red

        self.ax.clear()
        self.ax.imshow(display_maze, cmap=cmap, interpolation='nearest')
        self.ax.set_xticks([]), self.ax.set_yticks([])
        plt.draw()

    def set_axes(self, ax):
        self.ax = ax

def on_generate(event):
    try:
        size = int(size_text_box.text)

        # Ensure the maze size is an odd number
        if size % 2 == 0:
            size += 1

        maze.width, maze.height = size, size
        maze.maze = [[1] * size for _ in range(size)]
        maze.visited = [[False] * size for _ in range(size)]

        maze.generate_maze()
        maze.create_entrance_and_exit()
        maze.display_maze()
    except ValueError:
        print("Please enter a valid integer value for size.")

def on_find_path(event):
    path = maze.find_shortest_path()
    maze.display_maze(path)

fig, ax = plt.subplots(figsize=(10, 10))
plt.subplots_adjust(bottom=0.2)

maze = Maze(20)
maze.set_axes(ax)

# Initial maze generation and display.
maze.generate_maze()
maze.create_entrance_and_exit()
maze.display_maze()

# Add interactive widgets
ax_generate = plt.axes([0.7, 0.05, 0.1, 0.075])
btn_generate = Button(ax_generate, 'Generate')

ax_find_path = plt.axes([0.81, 0.05, 0.1, 0.075])
btn_find_path = Button(ax_find_path, 'Find Path')

ax_size = plt.axes([0.3, 0.05, 0.1, 0.075])
size_text_box = TextBox(ax_size, 'Size', initial="20")

btn_generate.on_clicked(on_generate)
btn_find_path.on_clicked(on_find_path)

plt.show()

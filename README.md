# Maze Editor

## Description
This script generates a random maze, in a square with the dimensions set by the user, using DFS algorithm, ensuring, that a path from the start to the end is possible. Then, using the A* algorithm, it finds the shortest path from the start to the finish

## Code

### Class Initialization
- self.maze: A 2D list representing the maze grid, initialized with walls (1).
- self.visited: A 2D list to track which cells have been visited during maze generation.
- self.directions: A list of possible movement directions (right, down, left, up).

### Maze Generation Algorithm
#### Depth-First Search (DFS) for Maze Generation
- Initialization: Marks the starting cell as visited and creates a path (0).
- Randomize Directions: Shuffles the directions to ensure randomness in the maze structure.
- Recursive Path Carving: For each direction, it calculates the new coordinates (nx, ny) and recursively visits the new cell if it's within bounds and not visited. This creates paths and ensures the maze is solvable.

### Pathfinding Algorithm
- Heuristic Function: Uses Manhattan distance to estimate the cost from the current cell to the end cell.
#### A Algorithm*:
- Open Set: Priority queue to explore the most promising nodes first.
- g_cost: Dictionary to store the cost from the start node to each node.
- f_cost: Dictionary to store the total estimated cost (g_cost + heuristic) from start to the goal.
- came_from: Dictionary to store the path history.
- Main Loop: Explores nodes with the lowest f_cost. If the end is reached, reconstructs the path by backtracking through came_from.

### Maze Display
- display_maze: Uses matplotlib to visualize the maze.
- Path Display: If a path is provided, marks the path in red.
- set_axes: Sets the axes for plotting the maze.

## Installation Requirements
Python:
- Ensure you have Python installed (preferably Python 3.6 or later)

Required Packages:
- matplotlib: For plotting the maze and creating interactive widgets.

## Project's future
I aim to revise this script and make the maze generation algorithm more versitile and robust.  

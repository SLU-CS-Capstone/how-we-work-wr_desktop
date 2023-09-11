from maze import Maze
import random
import sys

if len(sys.argv) > 1:
    maze = Maze(30, sys.argv[0])
else:
    maze = Maze(30, random.randint(0, 1000))


maze.generate_maze()
maze.print()
print("Welcome to 2D maze")

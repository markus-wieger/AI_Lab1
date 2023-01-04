import numpy as np
from Puzzle import Puzzle


if __name__ == '__main__':
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goal = np.array(goal)
    goal = goal.reshape((3, 3))
    print(goal)
    puzzle = Puzzle(goal)
    print(puzzle.printIndex())
    puzzle.solve()


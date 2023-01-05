import numpy as np
from Puzzle import Puzzle


def hamming():
    puzzle = Puzzle(create_goal(), 1)
    puzzle.solve()


def manhattan():
    puzzle = Puzzle(create_goal(), 2)
    puzzle.solve()

def create_goal():
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    goal_state = np.array(goal_state)
    goal_state = goal_state.reshape((3, 3))
    return goal_state


if __name__ == '__main__':
    print("What would you like to do?")
    print("1: Calculate Hamming")
    print("2: Calculate Manhattan")
    inp = int(input())
    if inp == 1:
        hamming()
    elif inp == 2:
        manhattan()


import numpy as np
from Puzzle import Puzzle


def hamming(runs):

    time = 0
    f = open("output.txt", "w")
    f.write("Documentation of A* Algorithm\n"
            "Used Heuristic: Hamming\n\n")
    f.close()
    for x in range(0, runs):
        puzzle = Puzzle(create_goal(), 1)
        f = open("output.txt", "a")
        f.write("Run: " + str(x+1))
        f.close()
        puzzle.solve()
    f = open("output.txt", "a")
    f.write("Total time: " + str(time))
    f.close()


def manhattan(runs):
    time = 0
    f = open("output.txt", "w")
    f.write("Documentation of A* Algorithm\n"
            "Used Heuristic: Manhattan\n\n")
    f.close()
    for x in range(0, runs):
        puzzle = Puzzle(create_goal(), 2)
        f = open("output.txt", "a")
        f.write("Run: " + str(x + 1))
        f.close()
        time += puzzle.solve()
    f = open("output.txt", "a")
    f.write("Total time: " + str(time))
    f.close()


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
    num = int(input("How many times should it run?\n"))
    if inp == 1:
        hamming(num)
    elif inp == 2:
        manhattan(num)


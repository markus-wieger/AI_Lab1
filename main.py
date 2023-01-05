import numpy as np
from Puzzle import Puzzle


def hamming(runs):
    """
    Starts the puzzle solving algorithm using the hamming heuristic.
    Also makes a file called output and writes the number of runs as well as 
    the total time needed.
   
    :param runs: Number of runs the system should do
    :return: None
    """
    time = 0
    f = open("output.txt", "w")
    f.write("Documentation of A* Algorithm\n"
            "Used Heuristic: Hamming\n\n")
    f.close()
    for x in range(0, runs):
        puzzle = Puzzle(1)
        f = open("output.txt", "a")
        f.write("Run: " + str(x+1))
        f.close()
        puzzle.solve()
    f = open("output.txt", "a")
    f.write("Total time: " + str(time))
    f.close()


def manhattan(runs):
    """
        Starts the puzzle solving algorithm using the manhattan heuristic.
        Also makes a file called output and writes the number of runs as well as 
        the total time needed.

        :param runs: Number of runs the system should do
        :return: None
        """
    time = 0
    f = open("output.txt", "w")
    f.write("Documentation of A* Algorithm\n"
            "Used Heuristic: Manhattan\n\n")
    f.close()
    for x in range(0, runs):
        puzzle = Puzzle(2)
        f = open("output.txt", "a")
        f.write("Run: " + str(x + 1))
        f.close()
        time += puzzle.solve()
    f = open("output.txt", "a")
    f.write("Total time: " + str(time))
    f.close()


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


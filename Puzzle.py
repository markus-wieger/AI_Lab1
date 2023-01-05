import numpy as np
import heapq
import random
from State import State


def check_if_solvable(list_check):
    """
    Helper function for create_gameboard().
    Takes a list and performs a check whether it is a solvable possibility for an 8-Puzzle.

    :param list_check: a randomized list with 9 items.
    :return: boolean: True if solvable. False if not solvable
    """
    inversions = 0
    empty_space = 0
    for i in range(0, 9):
        for j in range(i + 1, 9):
            if list_check[j] != empty_space and list_check[i] != empty_space and list_check[i] > list_check[j]:
                inversions += 1
    if inversions % 2 == 0:
        return True
    else:
        return False


def create_gameboard():
    """
    creates a suitable gameboard

    :return:
    """
    tmp_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    solvable = False
    while not solvable:
        random.shuffle(tmp_list)
        # print(tmp_list)

        if check_if_solvable(tmp_list):
            print("Solvable")
            solvable = True
        else:
            print("Not solvable!")
            solvable = False

    res = np.array(tmp_list)
    # print(res)
    initial_state = res.reshape((3, 3))
    print(initial_state)
    return initial_state


class Puzzle:

    def __init__(self, goal, heuristic):
        self.used_heuristic = heuristic  # 1 == Hamming; 2 == Manhattan
        self.initial = create_gameboard()
        self.g_val = 0
        self.num_of_states = 0
        self.goal = goal
        self.states_pq = []
        init_state = State(self.initial, 0, self.goal, self.used_heuristic)
        heapq.heappush(self.states_pq, (init_state.f_val, self.num_of_states, init_state))

        # self.states = []
        # self.states.append(State(self.initial, 0, self.goal))

    def printIndex(self):
        return self.states_pq[0].getIndexOfTile(0)

    def solve(self):
        while not self.check_if_solved((self.states_pq[0])[2]):
            self.where_to_go()
        print("Solved")
        print("Depth: " + str(self.g_val))
        print("Number of States: " + str(self.num_of_states))

    def where_to_go(self):
        out = heapq.heappop(self.states_pq)
        # print(out)
        state = out[2]
        self.g_val = state.g_val
        self.g_val += 1
        index = state.getIndexOfTile(0)

        if index[0] == 0:
            if index[1] == 0:
                self.add_to_heap(self.switch(0, 1, 0, 0, state))
                self.add_to_heap(self.switch(1, 0, 0, 0, state))
            elif index[1] == 1:
                self.add_to_heap(self.switch(0, 2, 0, 1, state))
                self.add_to_heap(self.switch(0, 0, 0, 1, state))
                self.add_to_heap(self.switch(1, 1, 0, 1, state))
            elif index[1] == 2:
                self.add_to_heap(self.switch(0, 1, 0, 2, state))
                self.add_to_heap(self.switch(1, 2, 0, 2, state))
        elif index[0] == 1:
            if index[1] == 0:
                self.add_to_heap(self.switch(0, 0, 1, 0, state))
                self.add_to_heap(self.switch(1, 1, 1, 0, state))
                self.add_to_heap(self.switch(2, 0, 1, 0, state))
            elif index[1] == 1:
                self.add_to_heap(self.switch(1, 0, 1, 1, state))
                self.add_to_heap(self.switch(1, 2, 1, 1, state))
                self.add_to_heap(self.switch(0, 1, 1, 1, state))
                self.add_to_heap(self.switch(2, 1, 1, 1, state))
            elif index[1] == 2:
                self.add_to_heap(self.switch(0, 2, 1, 2, state))
                self.add_to_heap(self.switch(1, 1, 1, 2, state))
                self.add_to_heap(self.switch(2, 2, 1, 2, state))
        elif index[0] == 2:
            if index[1] == 0:
                self.add_to_heap(self.switch(1, 0, 2, 0, state))
                self.add_to_heap(self.switch(2, 1, 2, 0, state))
            elif index[1] == 1:
                self.add_to_heap(self.switch(1, 1, 2, 1, state))
                self.add_to_heap(self.switch(2, 0, 2, 1, state))
                self.add_to_heap(self.switch(2, 2, 2, 1, state))
            elif index[1] == 2:
                self.add_to_heap(self.switch(2, 1, 2, 2, state))
                self.add_to_heap(self.switch(1, 2, 2, 2, state))

    def add_to_heap(self, state):
        """
        Adds a state to the heap of Puzzle object

        :param state: State to be added to the heap
        :return: none
        """
        self.num_of_states += 1
        heapq.heappush(self.states_pq, (state.f_val, self.num_of_states, state))

    def switch(self, zeile, spalte, alt_zeile, alt_spalte, state):
        """
        Performs a switch of two locations that are defined in the method head

        :param zeile: y_axis of new location
        :param spalte: x_axis of new location
        :param alt_zeile: y_axis of old location
        :param alt_spalte: x_axis of old location
        :param state: State object to get current array
        :return: New State object with switched numbers
        """

        old = np.copy(state.current)
        new = np.copy(state.current)
        new[zeile][spalte] = old[alt_zeile][alt_spalte]
        new[alt_zeile][alt_spalte] = old[zeile][spalte]
        return State(new, self.g_val, self.goal, self.used_heuristic)

    def check_if_solved(self, state):
        if np.array_equal(state.current, self.goal):
            return True
        else:
            return False

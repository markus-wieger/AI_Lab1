class State:
    def __init__(self, current, gval, goal, heuristic):
        """
        Constructor for State object.
        Automatically calculates heuristic value and f_value.

        :param current: numpy array: 3x3 array, puzzle state to be added to the heap
        :param gval: int: Depth of the nodes, counted in Puzzle class
        :param goal: numpy array: 3x3 array, containing goal state of Puzzle
        :param heuristic: int: 1 for Hamming; 2 for Mannhattan
        """
        self.used_heuristic = heuristic  # 1 == Hamming; 2 == Manhattan
        self.current = current
        self.g_val = gval
        self.goal = goal
        if self.used_heuristic == 1:
            self.h_val = self.calculateHamming()
        else:
            self.h_val = self.calculateManhattan()
        self.f_val = self.g_val + self.h_val

    def getIndexOf0(self):
        """
        Searches for the Index of the "blank" space in the 3x3 array in the current state

        :return: Tuple of the Index (row, column)
        """
        current = self.current
        for i in range(0, len(self.current)):
            for j in range(0, len(self.current)):
                if current[i][j] == 0:
                    return i, j

    def getIndexOfTileGoal(self, Tile):
        """
        Searches for the Index of the provided tile in the 3x3 array in the goal state

        :return: Tuple of the Index (row, column)
        """
        current = self.goal
        for i in range(0, len(self.goal)):
            for j in range(0, len(self.goal)):
                if current[i][j] == Tile:
                    return i, j

    def calculateHamming(self):
        """
        Calculates the h_val for the current state based on the hamming heuristic

        :return: An Integer Value that is the calculated heuristic
        """
        misplacedTilesCount = 0
        for i in range(3):
            for j in range(3):
                if self.current[i][j] != self.goal[i][j] and (self.current[i][j] != 0):
                    misplacedTilesCount += 1
        return misplacedTilesCount

    def calculateManhattan(self):
        """
        Calculates the h_val for the current state based on the manhattan heuristic

        :return: An Integer Value that is the calculated heuristic
        """
        sum = 0
        for i in range(3):
            for j in range(3):
                currentTile = self.current[i][j]
                if self.current[i][j] != 0:
                    x1 = i
                    y1 = j
                    x2, y2 = self.getIndexOfTileGoal(currentTile)
                    val = abs(x1 - x2) + abs(y1 - y2)
                    sum = sum + val
        return sum
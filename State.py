class State:
    def __init__(self, current, gval, goal):
        self.current = current
        self.g_val = gval
        self.goal = goal
        self.h_val = self.calculateHamming()
        self.f_val = self.g_val + self.h_val

    def getIndexOf0(self):
        current = self.current
        for i in range(0, len(self.current)):
            for j in range(0, len(self.current)):
                if current[i][j] == 0:
                    return i, j

    def calculateHamming(self):
        misplacedTilesCount = 0
        for i in range(3):
            for j in range(3):
                if self.current[i][j] != self.goal[i][j] and (self.current[i][j] != "0"):
                    misplacedTilesCount += 1
        return misplacedTilesCount

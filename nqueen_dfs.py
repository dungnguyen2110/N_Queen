import random
import time

class NQueens:
    def __init__(self, N):
        self.N = N
        self.queenPosSol = None

    # check for row violate exists
    def checkRowViolate(self, queenPos, N):
        col = [0] * N
        for i in range(len(queenPos)):
            col[queenPos[i][0]] += 1
            if col[queenPos[i][1]] > 1:
                return True
        return False

    # check for Collumn violate exists
    def checkColViolate(self, queenPos, N):
        col = [0] * N
        for i in range(len(queenPos)):
            col[queenPos[i][1]] += 1
            if col[queenPos[i][1]] > 1:
                return True
        return False

    # check for positive diagonal violate exists
    def checkPosDiagViolate(self, queenPos, N):
        diag = [0] * (2*N - 1)
        for i in range(len(queenPos)):
            diag[queenPos[i][0] + queenPos[i][1]] += 1
            if diag[queenPos[i][0] + queenPos[i][1]] > 1:
                return True
        return False

    # check for negative diagonal violate exists
    def checkNegDiagViolate(self, queenPos, N):
        diag = [0] * (2*N - 1)
        for i in range(len(queenPos)):
            diag[queenPos[i][0] - queenPos[i][1]] += 1
            if diag[queenPos[i][0] - queenPos[i][1]] > 1:
                return True
        return False

    # return True if exists any violation
    def isNotSafe(self, queenPos):
        if self.checkRowViolate(queenPos, self.N):
            return True
        if self.checkColViolate(queenPos, self.N):
            return True
        if self.checkPosDiagViolate(queenPos, self.N):
            return True
        if self.checkNegDiagViolate(queenPos, self.N):
            return True
        return False

    # check right, wrong or no solution
    def checkSolution(self):
        if self.queenPosSol == None:
            print("Doesnt have solution")
        elif not self.isNotSafe(self.queenPosSol):
            print("Has right solution")
        else:
            print("Wrong solution")

    # prints out all positions of queens
    def printQueen(self):
        if self.queenPosSol == None:
            print("No solution")
            return
        print("Solution: [", end='')
        for i in range(self.N):
            if i == self.N - 1:
                print((self.queenPosSol[i][1]), end='')
            else:
                print((self.queenPosSol[i][1]), ' ', end='')
        print(']\n', end='')

    # print demo board
    def printBoard(self):
        if self.queenPosSol == None:
            print("No solution")
            return

        for i in range(self.N):
            for j in range(self.N):
                if (i, j) in self.queenPosSol:
                    print('Q ', end='')
                else:
                    print('. ', end='')
            print('\n', end='')

    # Depth-first search algorithm - DFS
    def dfs(self):
        nodes = [[]]

        while nodes != []:
            pos = nodes.pop()
            queennum = len(pos)

            # shuffle range for better performance
            l = list(range(self.N))
            random.shuffle(l)

            for i in l:
                sample = pos + [(queennum, i)]
                if not self.isNotSafe(sample):
                    if (len(sample) == self.N):
                        self.queenPosSol = sample
                        return

                    nodes.append(sample)

        return

if __name__ == "__main__":
    N = int(input("Enter N: "))
    q = NQueens(N)

    start_time = time.time()
    q.dfs()
    # q.printQueen()
    q.printBoard()

    q.checkSolution()
    end_time = time.time()
    print("Time elapsed: %s" % (end_time - start_time))
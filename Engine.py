class gameState():
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0], 
                      [0, 0, 0, 0, 0, 0, 0]]
        self.redTurn = False
        self.rowCounter = [5, 5, 5, 5, 5, 5, 5]
        self.moveLog = [] #move log used for the undoMove method

    def allMoves(self):
      moves = []
      for i in range(7):
        if self.rowCounter[i] >= 0:
          moves.append(i)
      return(moves)

    def move(self, column):
        if column <= 6 and column >= 0:
            if self.rowCounter[column] >= 0:
                if self.redTurn:
                    self.board[self.rowCounter[column]][column] = 1
                else:
                    self.board[self.rowCounter[column]][column] = 2
                self.rowCounter[column] -= 1
                self.redTurn = not self.redTurn
                self.moveLog.append(column)


    


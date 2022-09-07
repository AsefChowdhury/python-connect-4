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

  def isWin(self):
    done = False
    a = 5
    b = 0
    while not done:

      piece = self.board[a][b]
      if piece != 0: 
        if piece == self.board[a - 1][b]:
          if piece == self.board[a - 2][b]:
            if piece == self.board[a - 3][b]:
                return True

        if b <= 3:
          if piece == self.board[a][b + 1]:
            if piece == self.board[a][b + 2]:
              if piece == self.board[a][b + 3]:
                return True
  
        if piece == self.board[a - 1][b + 1]:
          if piece == self.board[a - 2][b + 2]:
            if piece == self.board[a - 3][b + 3]:
              return True
  
        elif b > 3:
          if piece == self.board[a - 1][b - 1]:
            if piece == self.board[a - 2][b - 2]:
              if piece == self.board[a - 3][b - 3]:
                return True
      if a == 3:
        done = True
      if b == 6:
        a -= 1
        b = 0
      else:
        b += 1
    return False
    

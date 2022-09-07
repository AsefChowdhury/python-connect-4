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

  def isWin(self, column):
    #done = False
    diagonalLefts, verticals, horizontals, diagonalRights = 0, 0, 0, 0
    piece = self.board[self.rowCounter[column] + 1][column]
    row = self.rowCounter[column] + 1
    # Horizonals:
    positiveDir, negativeDir = False, False
    col = 1
    while (positiveDir == False or negativeDir == False) and horizontals < 3:       
      if negativeDir == False:
        if column - col >= 0:
          if piece == self.board[row][column - col]:
            horizontals += 1
          else:
            negativeDir = True
        else: 
          negativeDir = True
  
      if positiveDir == False:
        if column + col <= 6:
          if piece == self.board[row][column + col]:
            horizontals += 1
          else:
            positiveDir = True
        else:
          positiveDir = True
      col += 1
    if horizontals == 3:
      return True
      
    # Veritcals:  
    negativeDir = False
    r = 1
    while negativeDir == False and verticals < 3:
      if negativeDir == False:
        if row + r <= 5:
          if piece == self.board[row + r][column]:
            verticals += 1
          else:
            negativeDir = True
        else:
          negativeDir = True
      r += 1
    if verticals == 3:
      return True
    # diagonalLefts:
    positiveDir, negativeDir = False, False
    r = 1
    col = 1
    while (positiveDir == False or negativeDir == False) and diagonalLefts < 3:  
      if positiveDir == False:
        if column - col >= 0 and row - r <= 0:
          if piece == self.board[row - r][column - col]:
            diagonalLefts += 1
          else:
            positiveDir = True
        else:
            positiveDir = True

      if negativeDir == False:
        if row + r <= 5 and column + col <= 6:
          if piece == self.board[row + r][column + col]:
            diagonalLefts += 1
          else:
            negativeDir = True
        else:
            negativeDir = True
      r += 1
      col += 1
    if diagonalLefts == 3:
      return True
      
    # diagonalRights:
    positiveDir, negativeDir = False, False
    r = 1
    col = 1
    while (positiveDir == False or negativeDir == False) and diagonalRights < 3:
      if negativeDir == False:
        if column - col >= 0 and row + r <= 5:
          if piece == self.board[row + r][column - col]:
            diagonalRights += 1
          else:
            negativeDir = True
        else:
            negativeDir = True
  
      if positiveDir == False:
        if row - r >= 0 and column + col <= 6:
          if piece == self.board[row - r][column + col]:
            diagonalRights += 1
          else:
            positiveDir = True
        else:
            positiveDir = True
      r += 1
      col += 1
    if diagonalRights == 3:
      return True
    return False

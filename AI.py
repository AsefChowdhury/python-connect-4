import random
maxDepth = 7

def movefinder(gameState, moves):
    global bestMove
    random.shuffle(moves)
    minmax(gameState, moves, gameState.redTurn, maxDepth, -10000000, 10000000)
    return (bestMove)

def minmax(gameState, moves, redTurn, depth, alpha, beta):
    global bestMove
    if depth == 0 or len(moves) == 0:
        return totalScore(gameState)
            
    if redTurn:
        maxScore = -10000000
 
        for move in moves:
            gameState.move(move)
            nextMoves = gameState.allMoves()
            score = minmax(gameState, nextMoves, False, depth - 1, alpha, beta)
            if score > maxScore:
                maxScore = score
                if depth == maxDepth:
                    bestMove = move
                    
            gameState.undoMove()
            if maxScore > alpha:
                alpha = maxScore
            if alpha >= beta:
                break
            
        return maxScore
    else:
        minScore = 100000000
        for move in moves:
            gameState.move(move)
            nextMoves = gameState.allMoves()
            score = minmax(gameState, nextMoves, True, depth - 1, alpha, beta)
            if score < minScore:
                minScore = score
                if depth == maxDepth:
                    bestMove = move
            gameState.undoMove()
            if minScore < beta:
                beta = minScore
            if alpha >= beta:
                break
        return minScore

      
def totalScore(gameState):
  score = 0
  if gameState.win:
      if gameState.redTurn:
          return (-1000 * gameState.turns)
      else:
          return(1000 * gameState.turns)
  ## Score Horizontal
  for r in range(6):
    for c in range(4):
      counters = gameState.board[r][c:c+4]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
  
        ## Score Vertical
  for c in range(7):
    col_array = [i[c] for i in gameState.board]
    for r in range(4):
      counters = col_array[r:r+4]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10


  ## Score negative sloped diagonal
  for r in range(3):
    for c in range(4):
      counters = [gameState.board[r+i][c+i] for i in range(4)]
      #print(counters)
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
      
  ## Score positive sloped diagonal
  for r in range(3):
    for c in range(4):
      counters = [gameState.board[r+3-i][c+i] for i in range(4)]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
  return(score * gameState.turns)


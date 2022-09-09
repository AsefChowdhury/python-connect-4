import random

maxDepth = 6

def movefinder(gameState, moves):
    global bestMove
    random.shuffle(moves)
    bestMove = moves[0]
    minmax(gameState, moves, gameState.redTurn, maxDepth, -1000, 1000)
    return (bestMove)

def minmax(gameState, moves, redTurn, depth, alpha, beta):
    global bestMove
    if depth == 0:
        return totalScore(gameState)
            
    if redTurn:
        maxScore = -1000
 
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
        minScore = 1000
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
  ## Score Horizontal
  for r in range(6):
    for c in range(4):
      counters = gameState.board[r][c:c+4]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 4:
        score += 1000
      if oranges == 4:
        score -= 1000
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
      if reds == 1 and spaces == 3:
        score += 2
      if oranges == 1 and spaces == 3:
        score -= 2
  
	## Score Vertical
  for c in range(7):
    col_array = [i[c] for i in gameState.board]
    for r in range(4):
      counters = col_array[r:r+4]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 4:
        score += 1000
      if oranges == 4:
        score -= 1000
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
      if reds == 1 and spaces == 3:
        score += 2
      if oranges == 1 and spaces == 3:
        score -= 2 


  ## Score negative sloped diagonal
  for r in range(3):
    for c in range(4):
      counters = [gameState.board[r+i][c+i] for i in range(4)]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 4:
        score += 1000
      if oranges == 4:
        score -= 1000
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
      if reds == 1 and spaces == 3:
        score += 2
      if oranges == 1 and spaces == 3:
        score -= 2
      
  ## Score positive sloped diagonal
  for r in range(3):
    for c in range(4):
      counters = [gameState.board[r+3-i][c+i] for i in range(4)]
      reds = counters.count(1)
      oranges = counters.count(2)
      spaces = counters.count(0)
      if reds == 4:
        score += 1000
      if oranges == 4:
        score -= 1000
      if reds == 2 and spaces == 2:
        score += 5
      if oranges == 2 and spaces == 2:
        score -= 5
      if reds == 3 and spaces == 1:
        score += 10
      if oranges == 3 and spaces == 1:
        score -= 10
      if reds == 1 and spaces == 3:
        score += 2
      if oranges == 1 and spaces == 3:
        score -= 2
  return(score)

#gameState = gameState()



  


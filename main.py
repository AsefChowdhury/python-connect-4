import Engine
import AI
import pygame
import math
import Menu

circleDiam = 64
radius = circleDiam / 2
HEIGHT = 480
WIDTH = 640
backgroundColour = [99, 163, 250]
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT + 68))
pygame.display.set_caption("connect 4")
clock = pygame.time.Clock()

boardImage = pygame.transform.scale(
    pygame.image.load("images/Connect4Board.png"), (WIDTH, HEIGHT))
redPiece = pygame.transform.scale(pygame.image.load("images/redPiece.png"),
                                  (circleDiam + 2, circleDiam + 2))
orangePiece = pygame.transform.scale(
    pygame.image.load("images/orangePiece.png"),
    (circleDiam + 2, circleDiam + 2))
redWins = pygame.image.load("images/redWins.png")
orangeWins = pygame.image.load("images/orangeWins.png")
def dropPiece(gameState, column):
  y = 0
  acc = 0.3
  yPos = 465 - (78 * (5 - gameState.rowCounter[column]))
  xPos = 17 + 89.6 * column
  velocity = 0.02
  bounced = False
  if gameState.redTurn:
    piece = redPiece
  else:
    piece = orangePiece
  while y < yPos:
    velocity += acc
    y += velocity
    if y >= yPos:
      y = yPos
    pygame.draw.rect(screen, backgroundColour,
                     (xPos, 0, circleDiam + 2, yPos + circleDiam))
    screen.blit(piece, (xPos, y))
    if y >= yPos and bounced == False:
      y -= 1
      velocity = -velocity * 0.3
      bounced = True
    screen.blit(boardImage, (0, 66))
    pygame.display.update()

gameState = Engine.gameState()  
mode = Menu.menu(screen, backgroundColour, boardImage, HEIGHT)

gameOver = False
won = False
AImove = False

##if mode == True:
##  AIMode = True
##else:
##  AIMode = False

while not gameOver:
  if mode == True:
    AIMode = True
  else:
    AIMode = False
  if gameState.win == True:
    pygame.time.wait(2000)
    mode = Menu.menu(screen, backgroundColour, boardImage, HEIGHT)
    gameState = Engine.gameState()
    AImove = False
  for event in pygame.event.get():
    if not won:
      if event.type == pygame.MOUSEMOTION:
        posx = event.pos[0]
        if posx <= radius:
          posx = radius
        elif posx >= WIDTH - radius:
          posx = WIDTH - radius
        pygame.draw.rect(screen, backgroundColour, (0, 0, WIDTH, 66))
        if gameState.redTurn:
          screen.blit(redPiece, (posx - radius, 0))
        else:
          screen.blit(orangePiece, (posx - radius, 0))
      pygame.display.update()
      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.pos[0] <= 90:
          col = 0
        else:
          col = math.floor(round(event.pos[0], -2) / 100)
        if gameState.rowCounter[col] >= 0:
          pygame.draw.rect(screen, backgroundColour, (0, 0, WIDTH, 66))
          dropPiece(gameState, col)
        if gameState.move(col) == True:
          AImove = True
        if gameState.win == True:
          if gameState.redTurn:)
            screen.blit(orangeWins, (110, HEIGHT/2))
          else:    
            screen.blit(redWins, (170, HEIGHT/2))
          
      if AImove == True and gameState.win == False and AIMode == True:
        moves = gameState.allMoves()
        bestMove = AI.movefinder(gameState, moves)
        dropPiece(gameState, bestMove)
        gameState.move(bestMove)
        AImove = False
        if gameState.win == True:
          if gameState.redTurn:
            screen.blit(orangeWins, (110, HEIGHT/2))
          else:    
            screen.blit(redWins, (170, HEIGHT/2))

    if event.type == pygame.QUIT:
      gameOver = True
    pygame.display.update()
pygame.quit()

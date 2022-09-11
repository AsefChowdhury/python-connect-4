import Engine
import AI
import pygame
import sys
import math

circleDiam = 64
radius = circleDiam / 2
HEIGHT = 480
WIDTH = 640
backgroundColour = [99, 163, 250]

gameState = Engine.gameState()
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
screen.fill(backgroundColour)
screen.blit(boardImage, (0, 66))

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
        


gameOver = False
won = False
moveMade = False

while not gameOver:
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
        pygame.draw.rect(
          screen, backgroundColour, (0, 0, WIDTH, 66))  
        dropPiece(gameState, col)
        gameState.move(col)
        moveMade = True
        if gameState.win == True:
          if gameState.redTurn:
            print("orange wins")
          else:    
            print("red wins")
          won = True
          
  if moveMade == True and won == False:
    moves = gameState.allMoves()
    bestMove = AI.movefinder(gameState, moves)
    dropPiece(gameState, bestMove)
    gameState.move(bestMove)
    moveMade = False
    if gameState.win == True:
      if gameState.redTurn:
        print("orange wins")
      else:    
        print("red wins")
      won = True
  if event.type == pygame.QUIT:
    gameOver = True
  pygame.display.update()
pygame.quit()

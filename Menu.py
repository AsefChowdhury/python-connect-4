import pygame
pygame.init()

#display window:
screenHeight, screenWidth  = 375, 280
pvpImgHeight,pvpImgLength  = 200, 125
pvAIImgHeight,pvAIImgLength  = 200, 125


#load button images
pvp_img = pygame.transform.scale(pygame.image.load('images/PlayerVsPlayer.png'), (pvpImgHeight, pvpImgLength))
pvAI_img = pygame.transform.scale(pygame.image.load('images/PlayerVsAI.png'), (pvAIImgHeight, pvAIImgLength))
title_img = pygame.transform.scale(pygame.image.load('images/title.png'), (600, 80))
piece = pygame.transform.scale(pygame.image.load('images/redPiece.png'), (64, 64))
circleDiam = 64
#button class:
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #self.rect.topleft = (x, y)
        self.clicked = False
        self.hover = False
        
    def draw(self, screen, backgroundColour):
        action = False
        # get mouse pos:
        pos = pygame.mouse.get_pos()
        tintFactor = 1/2
        #check mouse over and clicked conditions:
        if self.rect.collidepoint(pos):
            pygame.draw.rect(screen, [backgroundColour[0] + (255 - backgroundColour[0]) * tintFactor, backgroundColour[1] + (255 - backgroundColour[1]) * tintFactor, backgroundColour[2] + (255 - backgroundColour[2]) * tintFactor], (self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()))
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        #draw button on screen
        else:
            pygame.draw.rect(screen, backgroundColour, (self.rect.x, self.rect.y, self.image.get_width(), self.image.get_height()))

        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action

def menuDrop(screen, backgroundColour):
    y = -100
    acc = 0.0003
    yPos = 35
    xPos = 100
    velocity = 0.0001
    bounced = False
    while y < yPos:
        velocity += acc
        y += velocity
        #print(y)
        if y >= yPos:
          y = yPos
        pygame.draw.rect(screen, backgroundColour,
                         (xPos, 0, circleDiam + 2, yPos + circleDiam))
        screen.blit(piece, (xPos, y))
        if y >= yPos and bounced == False:
          y -= 1
          velocity = -velocity * 0.5
          bounced = True
        pygame.display.update()
    
#game loop:
def menu(screen, backgroundColour, boardImage, HEIGHT):
  pvp_button = Button(160, HEIGHT/2, pvp_img)
  pvAI_button = Button(480, HEIGHT/2, pvAI_img)
  screen.fill(backgroundColour)
  screen.blit(title_img, (20, 20))
  menuDrop(screen, backgroundColour)
  run =  True
  AIMode = False
  quit = False
  while run:
  
      #screen.fill(backgroundColour)
      
      if pvp_button.draw(screen, backgroundColour)== True:
          run = False
      if pvAI_button.draw(screen, backgroundColour)== True:
          AIMode = True
          run = False
      
      #event handler:
      for event in pygame.event.get():
          #quit game:
          if event.type == pygame.QUIT:
              quit = True
              run = False
  
      pygame.display.update()
    
  screen.fill(backgroundColour)
  screen.blit(boardImage, (0, 66))
  
  if quit == True:
    pygame.quit()
    
  return(AIMode)   

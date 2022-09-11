# Richu, ive updated menu.py locally. imma update it more then paste it onto here so you could get started on trying to display whoever wins on the board. Only thing (i think) i got left to do with the menu is make it open PvP or PvAI. could be more. who knows. I'll try and do as much as i can. Again, dont worry about this. I'll probs ask for your help if im hella stuck :-)
import pygame
pygame.init()

#display window:
screenHeight, screenWidth  = 375, 280
pvpImgHeight,pvpImgLength  = 125, 125
pvAIImgHeight,pvAIImgLength  = 125, 125

#screen = pygame.display.set_mode((screenWidth, screenHeight))
#pygame.display.set_caption('Game Mode')

#load button images
pvp_img = pygame.transform.scale(pygame.image.load('images/PlayerVsPlayer.png'), (pvpImgHeight, pvpImgLength))
pvAI_img = pygame.transform.scale(pygame.image.load('images/PlayerVsAI.png'), (pvAIImgHeight, pvAIImgLength))


#button class:
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        #self.rect.topleft = (x, y)
        self.clicked = False
        
    def draw(self, screen):
        action = False
        # get mouse pos:
        pos = pygame.mouse.get_pos()

        #check mouse over and clicked conditions:
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        return action
    
    
#create button instances


#game loop:
def menu(screen, backgroundColour, boardImage, HEIGHT):
  pvp_button = Button(160, HEIGHT/2, pvp_img)
  pvAI_button = Button(480, HEIGHT/2, pvAI_img)
  screen.fill(backgroundColour)
  run =  True
  AIMode = False
  quit = False
  while run:
  
      screen.fill(backgroundColour)
      
      if pvp_button.draw(screen)== True:
          print("You have chosen Player Vs. Player")
          run = False
      if pvAI_button.draw(screen)== True:
          print("You have chosen Player Vs. AI")
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

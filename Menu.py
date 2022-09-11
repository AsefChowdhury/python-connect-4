import pygame

#display window:
screenHeight =  375
screenWidth = 280

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Main Menu')

#load button images
start_img = pygame.image.load('start_btn.png').convert_alpha()
#exit_img = pygame.image.load('exit_btn.png').convert_alpha()


#button class:
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        
    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

#create button instances
start_button = Button(50, 50, start_img)


#game loop:
run =  True
while run:

    screen.fill((99, 163, 250))

    start_button.draw()
    #event handler:
    for event in pygame.event.get():
        #quit game:
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

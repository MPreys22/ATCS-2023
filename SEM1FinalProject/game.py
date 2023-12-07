import pygame, sys
from codeblock import Codeblock

class Game:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    BACKGROUND = (255, 255, 255)


    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.codeblock = Codeblock(50,50,100,100,(255,0,0))
        self.codeblock_group = pygame.sprite.Group()
        self.codeblock_group.add(self.codeblock)

        # Game Window 
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.BACKGROUND)


        # Set the caption of the screen 
        pygame.display.set_caption('CS JOURNEY') 
        self.background_img = pygame.image.load("Assets/BackGround.jpg")
        self.intro_music = pygame.mixer.Sound('Assets/Sounds/Music.wav')
    def run(self):
        self.intro_music.play()

        # game loop 
        while True: 
            # for loop through the event queue   
            for event in pygame.event.get(): 
                # Check for QUIT event       
                if event.type == pygame.QUIT: 
                    pygame.quit()
                    sys.exit()


            # Update the display using flip 
            self.screen.blit(self.background_img, (0, 0))
            self.codeblock_group.draw(self.screen)
            self.clock.tick(60)

            pygame.display.flip() 

if __name__ == "__main__":
    g = Game()
    g.run()
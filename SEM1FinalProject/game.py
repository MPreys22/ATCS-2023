import pygame
from codeblock import Codeblock
from laptop import Laptop
from fsm import FSM

class Game:
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 800
    BACKGROUND = (255, 255, 255)


    def __init__(self):
        # Initialize pygame
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()

        # Game Window 
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.BACKGROUND)

        # Laptop
        self.laptop_image = pygame.image.load("Assets/laptop.png")
        self.laptop = Laptop(self.laptop_image, 500, 500)

        # Codeblock
        self.codeblock_image = pygame.image.load("Assets/codeblock.png")
        self.codeblock = Codeblock(self.codeblock_image, 200, 200)

        # Create the Bot's finite state machine (self.fsm) with initial state
        # The s stands for still 
        self.fsm = FSM('s')
        self.init_fsm()
        


        # Set the caption of the screen 
        pygame.display.set_caption('CS JOURNEY') 
        self.background_img = pygame.image.load("Assets/BackGround.jpg")
        self.intro_music = pygame.mixer.Sound('Assets/Sounds/Music.wav')

    # Add the transitions of the FSM. Insirtation taken from the mazebot lab
    def init_fsm(self):
        self.fsm.add_transition(0,'s', self.codeblock.chase, 'c')
        self.fsm.add_transition(120, 'c', self.codeblock.inc_speed, 'lu' )
        self.fsm.add_transition(0, 'lu', self.codeblock.chase, 'c')



    def run(self):
        self.intro_music.play()

        # game loop 
        while True: 
            # for loop through the event queue   
            for event in pygame.event.get(): 
                # Check for QUIT event       
                if event.type == pygame.QUIT: 
                    pygame.quit()


            # Update the display using flip 
            self.screen.blit(self.background_img, (0, 0))
            self.laptop.draw(self.screen)
            self.codeblock.draw(self.screen)
            self.clock.tick(60)

            pygame.display.flip() 

if __name__ == "__main__":
    g = Game()
    g.run()
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
        self.time = 0

        # Game Window 
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.BACKGROUND)
        # To make the game a sidescroller, we will be changing the x value of the backgrounds position
        self.background_x = 0
        self.background_velo = 1

        # Laptop
        self.laptop_image = pygame.image.load("Assets/laptop.png")
        self.laptop = Laptop(self.laptop_image, 500, 500)

        # Codeblock
        self.codeblock_image = pygame.image.load("Assets/codeblock.png")
        self.codeblock = Codeblock(self.codeblock_image, 200, 200)
        

        # Set the caption of the screen 
        pygame.display.set_caption('CS JOURNEY') 
        self.background_img = pygame.image.load("Assets/BackGround.jpg")
        # self.intro_music = pygame.mixer.Sound('Assets/Sounds/Music.wav')

    



    def run(self):
        # self.intro_music.play()

        # game loop 
        while True: 
            input = 0
            # for loop through the event queue   
            for event in pygame.event.get(): 
                # Check for QUIT event       
                if event.type == pygame.QUIT: 
                    pygame.quit()


            # Update the display using flip 
            self.background_x -= self.background_velo
            if self.background_x <= -self.background_img.get_width():
                self.background_x = 0

            self.screen.blit(self.background_img, (self.background_x, 0))
            self.screen.blit(self.background_img, (self.background_x + self.background_img.get_width(), 0))
            self.laptop.draw(self.screen)
            self.codeblock.draw(self.screen)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.laptop.move_left()
                    self.laptop.update()
                if event.key == pygame.K_RIGHT:
                    self.laptop.move_right()
                    self.laptop.update()
                # if event.key == pygame.K_UP:
                #     self.laptop.jump()

            self.time += self.clock.tick(120)
            
            if self.time >= 120:
                self.time = 0 
                input = 120
                # self.background_velo += 1
            self.codeblock.update(input)

            pygame.display.flip() 

if __name__ == "__main__":
    g = Game()
    g.run()
import pygame
from obstacle import Obstacle
from codeblock import Codeblock
from laptop import Laptop
from submit import Submit
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
        self.score = 0
        self.input =0 

        # Game Window 
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.screen.fill(self.BACKGROUND)
        # To make the game a sidescroller, we will be changing the x value of the backgrounds position
        self.background_x = 0
        self.background_velo = 1

        #Submit 
        self.submit_image = pygame.image.load("Assets/submit.png")
        self.submit = Submit(self.submit_image)

        #Obstacle 
        self.obstacle_image = pygame.image.load("Assets/brick.png")
        self.obstacle = Obstacle(self.obstacle_image)

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

            # Draw every object 
            self.laptop.draw(self.screen)
            self.codeblock.draw(self.screen)
            self.obstacle.draw(self.screen)
            self.submit.draw(self.screen)

            # Movement using keydown 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.laptop.move_left()
                if event.key == pygame.K_RIGHT:
                    self.laptop.move_right()   
                if event.key == pygame.K_UP:
                    self.laptop.move_up()
                if event.key == pygame.K_DOWN:
                    self.laptop.move_down()



            # Everything that goes on when the laptop beats the first stage of the game 
            # Beating the level is making it past the x and y coordinate of the submit button
            if self.laptop.pos_x >= self.submit.pos_x and self.laptop.pos_y <= self.submit.pos_y:
                self.codeblock.pos_x = 0 
                self.laptop.pos_x = 100
                self.laptop.update()
                self.submit.update()
                self.codeblock.fsm.process(0)
                self.score +=1 

            # Set FPS
            self.time += self.clock.tick(120)
            # Perframe, update the position of the obstacle 
            if self.time >= 120:
                self.obstacle.update()
                self.time = 0 
                input = 120
                
            self.codeblock.update(input)
            input = 0
            
            pygame.display.flip() 

             # Check for Win 
            if self.score == 3:
                print("You Win!")
                pygame.quit()

            # Check for Loss
            if self.codeblock.pos_x >= self.laptop.pos_x:
                print("You lose")
                pygame.quit()

if __name__ == "__main__":
    g = Game()
    g.run()
import pygame 

class Game:
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    BACKGROUND = (255, 255, 255)


    # def __init__(self):
    #     # Initialize pygame
    #     pygame.init()
    #     pygame.mixer.init()
    #     self.clock = pygame.time.Clock()
    #     self.dt = 0

    # Game Window 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill(BACKGROUND)


    # Set the caption of the screen 
    pygame.display.set_caption('Geeksforgeeks') 
    
    # Update the display using flip 
    pygame.display.flip() 
    
    # Variable to keep our game loop running 
    running = True
    
    # game loop 
    while running: 
        
    # for loop through the event queue   
        for event in pygame.event.get(): 
        
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                running = False
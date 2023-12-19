import pygame
import random

class Obstacle(pygame.sprite.Sprite):
    # Initialize Obstacle
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image  = image
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = 0 
        
    # Randomize the position of the obstacle
    def update(self):
        self.pos_x = random.randrange(0, 1000)
        self.pos_y = random.randrange(0, 800)

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
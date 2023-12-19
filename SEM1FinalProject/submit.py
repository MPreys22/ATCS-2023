import pygame
import random

class Submit(pygame.sprite.Sprite):
    # Initialize submit button
    def __init__(self, image):
        pygame.sprite.Sprite.__init__(self)
        self.image  = image
        self.rect = self.image.get_rect()
        self.pos_x = 900
        self.pos_y = 0 
        
    # Every new stage give the submit button a random y coordinate
    def update(self):
        self.pos_y = random.randrange(0, 700)

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
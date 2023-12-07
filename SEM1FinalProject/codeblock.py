import pygame

class Codeblock(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
    

    
    def draw(self, screen):
         screen.blit(self.image, (200, 200))


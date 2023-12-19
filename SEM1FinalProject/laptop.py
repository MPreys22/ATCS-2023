import pygame

class Laptop(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = image
        self.rect = self.image.get_rect()
        self.pos_x = 100
        self.pos_y = 300
        self.velo = 10

    # All the functions called from the key clicks 
    def move_left(self):
        self.pos_x -= self.velo
    def move_right(self):
        self.pos_x += self.velo
    def move_up(self):
        self.pos_y -= self.velo
    def move_down(self):
        self.pos_y += self.velo

    #Increase and Decrease in velocity 
    def update(self):
        self.velo += 1
    def decrease(self):
        self.velo -= 1
        
    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
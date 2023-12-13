import pygame

class Laptop(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image  = image
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = 300
        self.velo = 0

    def move_left(self):
        self.pos_x -= 5
    def move_right(self):
        self.pos_x += 5

    # def update(self):
    #     self.pos_x += 1

    def draw(self, screen):
        screen.blit(self.image, (self.pos_x, self.pos_y))
import pygame
from fsm import FSM

class Codeblock(pygame.sprite.Sprite):
    def __init__(self, image, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.pos_x = 0
        self.pos_y = 300
        self.pos_change = 0

        # Create the Bot's finite state machine (self.fsm) with initial state
        # The s stands for still 
        self.fsm = FSM('s')
        self.init_fsm()
    

    # Add the transitions of the FSM. Insirtation taken from the mazebot lab
    def init_fsm(self):
        self.fsm.add_transition(0, 's', self.chase, 'c')
        self.fsm.add_transition(0, 'c', self.chase, 'c')
        self.fsm.add_transition(120, 's', self.chase, 'c')
        self.fsm.add_transition(120, 'c', self.inc_speed, 'inc' )
        self.fsm.add_transition(0, 'inc', self.chase, 'c')

    def chase(self):
        if self.pos_change == 0:
            self.pos_change = 1

    def inc_speed(self): 
        self.pos_change += 1


    def update(self, time):
        self.fsm.process(time)
        self.pos_x += self.pos_change


    def draw(self, screen):
         screen.blit(self.image, (self.pos_x, self.pos_y))


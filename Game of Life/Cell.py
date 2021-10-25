import pygame
from pygame.locals import *

class Cell:
    def __init__(self, life_state : bool):
        self.alive = life_state
        self.neighbours = 0

    def isAlive(self):
        return self.alive

    def revive(self):
        self.alive = True
    
    def kill(self):
        self.alive = False

    def increaseNeighbours(self,nbr:int):
        self.neighbours+=nbr

    def decreaseNeighbours(self,nbr:int):
        self.neighbours-=nbr

    def resetNeighborhood(self):
        self.neighbours=0

    def getNeighborhood(self):
        return self.neighbours

    def update(self):
        if self.isAlive():
            if self.neighbours != 3 and self.neighbours != 2:
                self.kill()
        else:
            if self.neighbours == 3:
                self.revive()
from Cell import *
import random
class Monde:
    
    def __init__(self, size,width,height):
        self.size = size
        self.map = []
        for i in range(size):
            row = []
            for j in range(size):
                row.append(Cell(False))
            self.map.append(row)
        self.width = width
        self.height = height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Game of Life')
        self.cellwidth = width/size
        self.cellheight = height/size 

    def display_map_shell(self):
        for j in range (0,self.size):
            for i in range (0,self.size):
                if self.map[i][j].isAlive():
                    print("+",end="   ")
                else:
                    print("-",end="   ")
            print("")

    def randomStart(self):
        for j in range(0,self.size):
            for i in range(0,self.size):
                if random.randint(0,1) == 1:
                    self.revive(i,j)
                

    def raw_map(self):
        self.screen.fill((250,250,250))
        # for i in range(1,self.size):
        #     pygame.draw.line(self.screen,(20,20,20),(self.cellwidth*i,self.height),(self.cellwidth*i,0))
        #     pygame.draw.line(self.screen,(20,20,20),(self.width,self.cellheight*i),(0,self.cellheight*i))

    def display_map(self):
        self.raw_map()
        for j in range (0,self.size):
            for i in range (0,self.size):
                if self.map[i][j].isAlive():
                    pygame.draw.rect(self.screen,
                                    (20,20,20),
                                    (i*self.cellwidth,j*self.cellheight,self.cellwidth,self.cellheight))
        pygame.display.flip()

    def getSize(self):
        return self.size

    def revive(self,i:int,j:int):
        self.map[i%self.size][j%self.size].revive()

    def kill(self,i:int,j:int):
        self.map[i%self.size][j%self.size].kill()
    
    def getCell(self,i,j):
        return self.map[i%self.size][j%self.size]

    def checkNeighborhood(self,posi,posj):
        self.map[posi][posj].resetNeighborhood()
        for j in range(posj-1,posj+2):
            for i in range(posi-1,posi+2):
                if self.map[i%self.size][j%self.size].isAlive() and (i!=posi or j != posj):
                    self.map[posi][posj].increaseNeighbours(1);
    
    def checkAllNeighborhoods(self):
        for j in range(0,self.size):
            for i in range(0,self.size):
                self.checkNeighborhood(i,j)
                # print(i,j,self.map[i][j].getNeighborhood())

    def updateAll(self):
        self.checkAllNeighborhoods()
        for j in range(0,self.size):
            for i in range(0,self.size):
                self.map[i][j].update()
                
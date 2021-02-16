import pygame
from pygame.locals import *
import sys
import random

class DogeJump:

    def __init__(self):
        self.screen = pygame.display.set_mode((800,600))
        self.green = pygame.image.load("doge").convert_alpha()
        self.platforms = []
        
    
    def updatePlayer(self):
        pass
    
    def updatePlatforms(self):
        pass
    
    
    
    def drawPlatforms(self):
        pass
   
    def generatePlatforms(self):
        pass
    
    def drawGrid(self):
        for x in range(80):
            pygame.draw.line(self.screen, (222,222,222), (x * 12, 0), (x * 12, 600))
            pygame.draw.line(self.screen, (222,222,222), (0, x * 12), (800, x * 12))
            
            
    
    def run(self):    
        clock = pygame.time.Clock()
        self.generatePlatforms()
        while True:
            self.screen.fill((255,255,255))
            clock.tick(60)
            for even in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                    
            self.drawGrid()
            pygame.display.flip()


DogeJump().run()

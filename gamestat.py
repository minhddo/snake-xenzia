import pygame

from food import Food
from obstacle import Obstacle

class GameStat:
    def __init__(self, width, height):
        self.score = 0
        self.end = False
        self.boardWidth = width 
        self.boardHeight = height 
        self.level = -1
        self.obstacle = Obstacle([])
    
    def setUpObstacle(self):
        if self.level == 0:
            return 
        if self.level == 1:
            for i in range(self.boardHeight):
                self.obstacle.blocks.append([0,i])
                self.obstacle.blocks.append([self.boardWidth-1, i])
            for i in range(self.boardWidth):
                self.obstacle.blocks.append([i, 0])
                self.obstacle.blocks.append([i, self.boardHeight-1])
        
    
    def animateObs(self, surface):
        self.obstacle.animate(surface)

        

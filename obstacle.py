import pygame
from gameobject import GameObject

gray = pygame.Color(196, 196, 196)
class Obstacle(GameObject):
    def __init__(self, obstacles):
        self.blocks = obstacles
    
    def animate(self, surface):
        for block in self.blocks:
            pygame.draw.rect(surface, gray, [20*block[0], 20*block[1], 20, 20])
    
    
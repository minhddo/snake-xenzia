import pygame

class GameObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def animate(self, surface, color):
        pygame.draw.circle(surface, color, [20*self.x + 10, 20*self.y + 10], 10, 0)
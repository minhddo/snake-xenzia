from random import randint
import pygame

from gameobject import GameObject
green = pygame.Color(0, 255, 0)
class Food(GameObject):
    def __init__(self, x, y):
        GameObject.__init__(self, x, y)

    def respawn(self, game_stats):
        self.x = randint(0, game_stats.boardWidth-1)
        self.y = randint(0, game_stats.boardHeight-1)
        for block in game_stats.obstacle.blocks:
            if self.x == block[0] and self.y == block[1]:
                Food.respawn(self, game_stats)

    def animate(self, surface):
        GameObject.animate(self, surface, green)
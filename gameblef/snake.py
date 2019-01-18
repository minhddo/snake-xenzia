import copy
import pygame
from game_object import GameObject


class Snake(GameObject):
    def __init__(self, snake_map, dire, input_manager):
        self.snake_map = snake_map
        self.dire = dire
        self.input_manager = input_manager

    def update(self):
        self.move()

    def move(self):
        temp = [None]*len(self.snake_map)
        for i in range(1, len(temp)):
            temp[i] = self.snake_map[i-1]
        newhead = copy.copy(self.snake_map[0])
        if self.dire == "right":
            newhead[0] += 1
        if self.dire == "left":
            newhead[0] -= 1
        if self.dire == "down":
            newhead[1] += 1
        if self.dire == "up":
            newhead[1] -= 1
        temp[0] = newhead
        self.snake_map = temp

    def changedir(self):
        if self.input_manager.right_pressed == True and self.dire != "left":
            self.dire = "right"
        if self.input_manager.left_pressed == True and self.dire != "right":
            self.dire = "left"
        if self.input_manager.up_pressed == True and self.dire != "down":
            self.dire = "up"
        if self.input_manager.down_pressed == True and self.dire != "up":
            self.dire = "down"
            

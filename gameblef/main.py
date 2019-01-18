import time
import pygame
import copy
import snake
import inputmanazer
from game_object import GameObject
import game_object

# init
red = pygame.Color(255, 0, 0)
pygame.init()
game_size = (800, 600)
game_display = pygame.display.set_mode(game_size)
clock = pygame.time.Clock()
background_image = pygame.image.load("background.png")

inputManagerInMain = inputmanazer.InputManager()

snake_map = [[5, 5], [4, 5], [3, 5]]
snake = snake.Snake(snake_map, "right", inputManagerInMain)

loop = True
while loop:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            inputManagerInMain.update(event)
            snake.changedir()
    snake.update()

    
    game_display.blit(background_image, (0, 0))
    for block in snake.snake_map:
        pygame.draw.circle(game_display, red, [20*block[0] + 10, 20*block[1] + 10], 10, 0)
    pygame.display.flip()
    # clock.tick(6000)
    time.sleep(0.1)


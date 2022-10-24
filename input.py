import pygame

class InputManager:
    def __init__(self):
        self.move = -1
        self.quit = 0
        self.restart = 1
        self.speed = 0.1

    def getEvent(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_s:
                    self.speed *= 1.5
                if event.key==pygame.K_f:
                    self.speed /= 1.5
                if event.key==pygame.K_ESCAPE:
                    self.quit = 1
                    self.restart = 0
                if event.key==pygame.K_SPACE:
                    self.quit = 1
                    self.restart = 1
                moves = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
                for i in range(4):
                    if event.key==moves[i]:
                        self.move = i
    
    def getLevel(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    return 0
                elif event.key == pygame.K_1:
                    return 1
                else:
                    return -1
            
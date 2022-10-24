import pygame

class Snake:
    def __init__(self, snake_body, snake_dir, snake_speed):
        self.body = snake_body
        self.dir = snake_dir
    
    def grow(self, game_stats):
        newhead = list(self.body[0])
        if self.dir==0:
            if newhead[0]==0:
                newhead[0] = game_stats.boardWidth
            else:
                newhead[0] -= 1
        elif self.dir==1:
            if newhead[0]==game_stats.boardWidth:
                newhead[0] = 0
            else:
                newhead[0] += 1
        elif self.dir==2:
            if newhead[1]==0:
                newhead[1] = game_stats.boardHeight
            else:
                newhead[1] -= 1
        elif self.dir==3:
            if newhead[1]==game_stats.boardHeight:
                newhead[1] = 0
            else:
                newhead[1] += 1
        self.body.insert(0, newhead)

    def move(self, game_stats):
        self.grow(game_stats)
        self.body.pop(-1)
    
    def changedir(self, dir):
        if (self.dir-1.5)*(dir-1.5) < 0:
            self.dir = dir
    
    def animate(self, surface, color):
        for parts in self.body:
            pygame.draw.circle(surface, color, [20*parts[0] + 10, 20*parts[1] + 10], 10, 0)
    
    def check_collide(self, food, game_stats):
        if self.body[0][0]==food.x and self.body[0][1]==food.y:
            self.grow(game_stats)
            food.respawn(game_stats)
            game_stats.score += 1
            print([food.x, food.y])
        for block in game_stats.obstacle.blocks:
            if self.body[0][0] == block[0] and self.body[0][1] == block[1]:
                return True
        for i in range(1, len(self.body)):
            if self.body[0]==self.body[i]:
                return True
        return False
            
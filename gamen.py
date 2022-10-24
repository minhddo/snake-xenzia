import pygame
import time
from food import Food
from gamestat import GameStat
import input
from input import InputManager
from snake import Snake

# pygame.init()
# games = GameStat(40, 30)

# game_size = (20*games.boardWidth, 20*games.boardHeight)
# game_display = pygame.display.set_mode(game_size)
# backgound_img = pygame.image.load("black.jpg")

# red = pygame.Color(255, 0, 0)
# gray = pygame.Color(196, 196, 196)
# black = pygame.Color(0, 0, 0)
# green = pygame.Color(0, 255, 0)
# blue = pygame.Color(0, 0, 255)
# white = pygame.Color(255, 255, 255)

pygame.init()
loopbig = True
while loopbig:
    
    games = GameStat(40, 30)

    game_size = (20*games.boardWidth, 20*games.boardHeight)
    game_display = pygame.display.set_mode(game_size)
    backgound_img = pygame.image.load("black.jpg")

    red = pygame.Color(255, 0, 0)
    gray = pygame.Color(196, 196, 196)
    black = pygame.Color(0, 0, 0)
    green = pygame.Color(0, 255, 0)
    blue = pygame.Color(0, 0, 255)
    white = pygame.Color(255, 255, 255)

    level_choose = InputManager()
    font = pygame.font.SysFont(None, 48)
    img = font.render('Please select your level: (0 or 1)', True, blue)
    game_display.blit(img, (20, 20))
    loop = True

    font1 = pygame.font.SysFont('chalkduster.ttf', 72)
    img1 = font1.render('chalkduster.ttf', True, blue)
    while loop:
        game_display.blit(img, (20, 20))
        pygame.display.update()
        n = level_choose.getLevel()
        if n==-1:
            pygame.quit()
        if n in [0,1]:
            games.level = n
            loop = False
        
    snake_coords = [[6, 5], [5, 5]]
    my_snake = Snake(snake_coords, 1, 0.1)
    input_manager  = InputManager()
    mfood = Food(7, 7)
    games.setUpObstacle()

    while games.end==False:
        score = font.render(str(games.score), True, white)
        games.animateObs(game_display)
        input_manager.getEvent()
        mfood.animate(game_display)
        my_snake.changedir(input_manager.move)
        my_snake.animate(game_display, red)
        my_snake.move(games)
        time.sleep(input_manager.speed)
        if my_snake.check_collide(mfood, games)==True:
            games.end=True
        pygame.display.flip()

        game_display.blit(backgound_img, (0,0))

    loop = True
    while loop:
        input_manager.getEvent()
        score = font.render("Your score: "+str(games.score)+", press esc to quit, space to restart", True, white)
        game_display.blit(score, (20, 20))
        pygame.display.update()
        if input_manager.restart == 0:
            loopbig = False
        if input_manager.quit == 1:
            loop = False











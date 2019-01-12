import pygame
import time
import copy
pygame.init()
b_size = 20
game_size = (20*b_size, 20*b_size)
game_display = pygame.display.set_mode(game_size)

red = pygame.Color(255, 0, 0)
gray = pygame.Color(196, 196, 196)
black = pygame.Color(0, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# xcord = 5
# ycord = 5
# for i in range(20):
#     if i%2 == 0:
#         pygame.draw.rect(game_display, gray, [xcord, ycord, 20, 20])
#     else:
#         pygame.draw.rect(game_display, black, [xcord, ycord, 20, 20])
#     xcord += b_size



snake_head = [5, 5, "right"]
snake_body = [[5, 5, "right"], [4, 5, "right"], [3, 5, "right"]]
# for block in snake_body:
#     pygame.draw.circle(game_display, red, [20*block[0] + 10, 20*block[1] + 10], 10, 0)
loop = True
while loop:
    def moving():
        before = copy.copy(snake_body)
        if snake_head[2] == "left":
            snake_head[0] -= 1
        if snake_head[2] == "right":
            snake_head[0] += 1
        if snake_head[2] == "up":
            snake_head[1] -= 1
        if snake_head[2] == "down":
            snake_head[1] += 1
        for i in range(1, len(snake_body)):
            snake_body[i] = before[i-1]



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT or event.key == ord("a"):
                change_dir("left")
            if event.key == K_RIGHT or event.key == ord("d"):
                change_dir("right")
            if event.key == K_UP or event.key == ord("w"):
                change_dir("up")
            if event.key == K_DOWN or event.key == ord("s"):
                change_dir("down")
            if event.key == K_BACKSPACE or event.key == K_ESCAPE:
                pygame.event.Event(pygame.QUIT)
        
    
    def change_dir(direction):
        if direction == "left" and snake_head[2] != "right":
            snake_head[2] = "left"
        if direction == "right" and snake_head[2] != "left":
            snake_head[2] = "right"
        if direction == "up" and snake_head[2] != "down":
            snake_head[2] = "up"
        if direction == "down" and snake_head[2] != "up":
            snake_head[2] = "down"
    
    for body in snake_body[1:]:
        if snake_head[0] == body[0] and snake_head[1] == body[1]:
            pygame.quit()
    
    
    

    for block in snake_body:
        pygame.draw.circle(game_display, red, [20*block[0] + 10, 20*block[1] + 10], 10, 0)

    moving()
    time.sleep(1)


pygame.display.flip()
pygame.quit()




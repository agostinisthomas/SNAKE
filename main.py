import pygame
import variables as vb
import objects as obj
import snake
import time


# Initialise Setup
pygame.init()
dis=pygame.display.set_mode(vb.board_size)
dis.fill(vb.background)
pygame.display.set_caption("Snake by Tom")
pygame.display.update()

# Coordinates & Time Initialisation
clock = pygame.time.Clock()

# Snake Initialisation
gameSnake = snake.Snake(vb.start_size)
print("Snake Squares : ", gameSnake.squares)

# Main Loop
turns=0
game_over=False
while not game_over :
    turns+=1
    # Go through squares in snake and colour them in :
    dis.fill(vb.background)
    for sq in gameSnake.squares :
        print("Square number ",gameSnake.squares.index(sq)," is ",sq)
        print("----------")
        pygame.draw.rect(dis, vb.white, ([sq[0],sq[1],10,10]))

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT :
            game_over=True
        if event.type == pygame.KEYDOWN :

            if event.key == pygame.K_LEFT :
                gameSnake.squares[0][2] = -1

            if event.key == pygame.K_RIGHT :
                gameSnake.squares[0][2] = 1

            if event.key == pygame.K_UP :
                gameSnake.squares[0][2] = -2

            if event.key == pygame.K_DOWN :
                gameSnake.squares[0][2] = 2



    gameSnake.move()
    # Update Display and tick forward
    pygame.display.update()
    clock.tick(10)
    # time.sleep(2)
    # if turns == 4 :
    #     game_over=True

pygame.quit()
quit()

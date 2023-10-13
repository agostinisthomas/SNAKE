import pygame
import variables as vb
import game
import snake
import time
import decor
import math


# Initialise Board, Time & Game
current_board = decor.Board()
current_game = game.Game(current_board.display)
current_food = game.Food()
clock = pygame.time.Clock()

# Main Loop
while current_game.state != -1 :

    # If player looses, he, she has option to play again
    while current_game.state == 0 :
        current_board.display.fill(vb.blue)
        decor.message("You Lost! Press C to Play Again or Q to Quit", vb.red, current_board.display)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    current_game.full_stop(current_board.display)
                elif event.key == pygame.K_c:
                    current_game = game.Game(current_board.display)
                    current_game.seed_food()

    current_game.updateView()

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT :
            game_over=True
        if event.type == pygame.KEYDOWN :

            if event.key == pygame.K_LEFT :
                dir=-1

            if event.key == pygame.K_RIGHT :
                dir=1

            if event.key == pygame.K_UP :
                dir=-2

            if event.key == pygame.K_DOWN :
                dir=2

            current_game.snake.change_direction(dir)

    current_game.snake.go_straight() # If no direction change, go straight

    # Check if snake encounters boundary, itself or finds food  :
    head = current_game.snake.get_head_pos()
    if (head[0]>vb.board_size[0]) or (head[0]<0) or (head[1]>vb.board_size[1]) or (head[1]<0) :
        current_game.state = 0

    for fd in current_game.foodList :
        if (abs(head[0] - fd.xcoord) < 20) and ((abs(head[1] - fd.ycoord) < 20)) :
            fd.eat(current_game)

    # Update Display and tick forward
    # pygame.display.update()
    current_game.updateView()
    clock.tick(vb.snakespeed)

current_game.full_stop(current_board.display)

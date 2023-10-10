import pygame
import variables as vb
import game
import snake
import time
import decor


# Initialise Board, Time & Game
current_board = decor.Board()
clock = pygame.time.Clock()
current_game = game.Game()

# Main Loop
while current_game.state != -1 :

    while current_game.state == 0 :
        current_board.display.fill(vb.blue)
        decor.message("You Lost! Press C to Play Again or Q to Quit", vb.red, current_board.display)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    current_game.full_stop(current_board.display)
                elif event.key == pygame.K_c:
                    current_game = game.Game()

    # Go through squares in snake and colour them in :
    current_board.display.fill(vb.background)
    for sq in current_game.snake.squares :
        pygame.draw.rect(current_board.display, vb.white, ([sq[0],sq[1],10,10]))

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

    # Check for boundary encounter :
    head = current_game.snake.get_head_pos()
    if (head[0]>vb.board_size[0]) or (head[0]<0) or (head[1]>vb.board_size[1]) or (head[1]<0) :
        current_game.state = 0

    # Update Display and tick forward
    pygame.display.update()
    clock.tick(10)

current_game.full_stop(current_board.display)

import variables as vb
import pygame
import snake
import decor
import time
import decor
import random

class Game :
    def __init__(self, display) :
        self.display = display
        self.snake = snake.Snake(vb.start_size)
        self.state = 1
        self.foodList = []

    def seed_food(self) :
        for i in range(vb.foodcount) :
            self.foodList.append(decor.Food())

    def gameOver(self) :
        self.state = -1

    def gameClose(self) :
        self.state = 0

    def full_stop(self,display) :
        display.fill(vb.white)
        decor.message("GAME OVER",vb.red,display)
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
        quit()

    def updateView(self) :
        print(self.foodList)
        self.display.fill(vb.background)
        # Draw food
        if self.foodList != [] :
            for fd in self.foodList :
                pygame.draw.rect(self.display, vb.green, ([fd.xcoord,fd.ycoord,10,10]))

        # Draw the snake
        for sq in self.snake.squares :
            pygame.draw.rect(self.display, vb.white, ([sq[0],sq[1],10,10]))

        pygame.display.update()

    def eat (self, food) :
        self.snake.grow()
        self.foodList.pop(self.foodList.index(food))
        foodx = round(random.randrange(0, vb.board_size[0] - vb.snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, vb.board_size[1] - vb.snake_block) / 10.0) * 10.0
        self.foodList.append([foodx, foody])
        # pygame.draw.rect(display, green, [foodx, foody, 10, 10])
        # pygame.display.update()

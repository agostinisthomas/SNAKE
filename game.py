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
        self.seed_food()
        self.score = 0

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

        # Display score :
        decor.score(self.score, self.display)

        pygame.display.update()



    def seed_food(self) :
        self.foodList = []
        for i in range(vb.foodcount) :
            self.foodList.append(Food())



class Food :
    def __init__(self) :
        foodx = int(random.randrange(0, vb.board_size[0] - vb.snake_block) / 10.0) * 10.0
        foody = int(random.randrange(0, vb.board_size[1] - vb.snake_block) / 10.0) * 10.0
        self.xcoord = foodx
        self.ycoord = foody
        self.coordinates = [foodx, foody]

    def get_position(self) :
        return [self.xcoord, self.ycoord]

    def eat (self, ongoingGame) :
        ongoingGame.snake.grow()
        ongoingGame.foodList.pop(ongoingGame.foodList.index(self))
        ongoingGame.foodList.append(Food())
        ongoingGame.score += 1
        # pygame.draw.rect(display, green, [foodx, foody, 10, 10])
        # pygame.display.update()

import variables as vb
import pygame
import snake
import decor
import time

class Game :
    def __init__(self) :
        self.snake = snake.Snake(vb.start_size)
        self.state = 1

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


class Food :
    def __init__(self,position) :
        self.position = position

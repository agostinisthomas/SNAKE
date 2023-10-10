import variables as vb
import pygame
import snake
import random

pygame.font.init()
font_style = pygame.font.SysFont("bahnschrift", 50)
def message (msg,color,display) :
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [20, vb.board_size[1]/2])

class Board :

    def __init__(self) :
        pygame.init()
        self.display = pygame.display.set_mode(vb.board_size)
        self.display.fill(vb.background)
        pygame.display.set_caption("Snake by Tom")
        pygame.display.update()


class Food :
    def __init__(self) :
        foodx = int(random.randrange(0, vb.board_size[0] - vb.snake_block) / 10.0) * 10.0
        foody = int(random.randrange(0, vb.board_size[1] - vb.snake_block) / 10.0) * 10.0
        self.xcoord = foodx
        self.ycoord = foody
        self.coordinates = [foodx, foody]

    def get_position(self) :
        return [self.xcoord, self.ycoord]

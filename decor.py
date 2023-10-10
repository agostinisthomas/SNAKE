import variables as vb
import pygame

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
    def __init__(self, count) :
        self.count=count

    

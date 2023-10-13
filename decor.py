import variables as vb
import pygame
import snake
import random

pygame.font.init()

def message (msg,color,display) :
    mesg = vb.messageFont.render(msg, True, color)
    display.blit(mesg, [20, vb.board_size[1]/2])

def score (score, display) :
    mesg = vb.score_Font.render("SCORE : "+str(score), True, vb.green)
    display.blit(mesg, [20, 20])

class Board :

    def __init__(self) :
        pygame.init()
        self.display = pygame.display.set_mode(vb.board_size)
        self.display.fill(vb.background)
        pygame.display.set_caption("Snake by Tom")
        pygame.display.update()

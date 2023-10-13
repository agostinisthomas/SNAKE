import pygame

# Board
board_size = (750,750)
x0, y0 = 350, 350
x1_change, y1_change = 0, 0
foodcount = 5

# Snake
start_size = 10
snakespeed = 10
snake_block = 10

# Colors

blue = (0,0,255)
red = (255,0,0)
green = (0,255,0)
white = (255,255,255)
black = (0,0,0)
background = black

# Fonts
pygame.font.init()
messageFont = pygame.font.SysFont("bahnschrift", 50)
score_Font = pygame.font.SysFont("bahnschrift", 50)

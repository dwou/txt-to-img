#!/usr/bin/env python3.9
import sys

import pygame
from pygame.locals import *

pygame.init()

fps = 600
clock = pygame.time.Clock()

width,height = 500,500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('TITLE')


WHITE = (255,255,255)
BLACK = (0,0,0)

font = pygame.font.Font('freesansbold.ttf', 60)

with open(r"input_text.txt","r") as f:
    lines = f.read().splitlines()
    print(lines)

# Game loop.
file_index = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
  
    screen.fill(WHITE)

    try:
        line = lines[file_index]
    except:
        pygame.quit()
        sys.exit()
    text = font.render(line,True,BLACK,WHITE)
    textRect = text.get_rect()
    textRect.center = (width//2,height//2)
    screen.blit(text,textRect)

    pygame.display.flip()
    pygame.image.save(screen, str("out" + str(file_index) + ".png"))
    
    clock.tick(fps)
    file_index += 1

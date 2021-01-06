import pygame
from pygame.locals import *

black = (9, 10, 10)
yellow = (255, 225, 0)
green = (0, 255, 81)
size = (600,500)

pygame.init()

myScreen = pygame.display.set_mode(size)

pygame.display.set_caption("Creator Of the Rectangles")

start = (0,0)
rect_list = []
drawing = False

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0,0
            drawing = True

        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0] - start [0], end[1] - start[1]
            rect = pygame.Rect(start,size)
            rect_list.append(rect)
            drawing =False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0] - start [0], end[1] - start[1]


        myScreen.fill(black)

        for rect in rect_list:
            pygame.draw.rect(myScreen,green,rect,4)

        pygame.draw.rect(myScreen, yellow, (start, size), 2)

        pygame.display.update()

pygame.quit()

#!/usr/bin/python3

import pygame, sys

GRID_HEIGHT = 8
GRID_WIDTH = 8
CELL_HEIGHT = 100
CELL_WIDTH = 100
BRD_THICKNESS = 1
BLACK = (0,0,0)
WHITE = (255, 255, 255)
GRAY = (90, 90, 90)
pygame.init()
screen = pygame.display.set_mode((CELL_WIDTH*GRID_WIDTH, CELL_HEIGHT*GRID_HEIGHT))

def createCells():
    x, y = 0, 0
    cells = []
    for row in range(GRID_HEIGHT):
        for column in range(GRID_WIDTH):
            cell = [x, y, CELL_WIDTH, CELL_HEIGHT]
            cells.append(cell)
            if column == GRID_WIDTH-1:
                x = 0
                y += 100
            else:
                x += 100
    #print(cells)
    return cells

def drawGrid(cells):
    for cell in cells:
        pygame.draw.rect(screen, BLACK, cell, BRD_THICKNESS)

def mouseHover():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for cell in cells:
        if cell[0] < mouse_x < cell[0] + cell[2] and cell[1] < mouse_y < cell[1] + cell[3]:
            pygame.draw.rect(screen, GRAY, cell)

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mouseHover()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill(WHITE)

cells = createCells()
screen.fill(WHITE)

while True:

    events()
    drawGrid(cells)
    pygame.display.update()

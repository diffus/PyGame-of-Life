import pygame, random, time, sys

def initializeRandomGeneration():
    generation = []
    for i in range(SIZE_X):
        cells = []
        for j in range(SIZE_Y):
            if random.randint(0, INITIAL_LIFE) == 0:
                cells += [ALIVE]
            else:
                cells += [DEAD]
        generation += [cells]
    return generation

def initializeEmptyGeneration():
    generation = []
    for i in range(SIZE_X):
        cells = []
        for j in range(SIZE_Y):
            cells += [DEAD]
        generation += [cells]
    return generation

def updateGeneration(generation):
    newGeneration = initializeEmptyGeneration()
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            newGeneration[i][j] = countNeighbours(i,j,generation)
    return newGeneration

def countNeighbours(x, y, generation):
    numNeighbours = 0
    for j in range(y-1, y+2):
        for i in range(x-1, x+2):
            if not(i == x and j == y):
                if i > 0 and i < SIZE_X and j > 0 and j < SIZE_Y:
                    numNeighbours += generation[i][j]
    if generation[x][y] == ALIVE and numNeighbours < 2:
        return DEAD
    if generation[x][y] == ALIVE and numNeighbours > 3:
        return DEAD
    if generation[x][y] == DEAD and numNeighbours == 3:
        return ALIVE
    else:
        return generation[x][y] 

def drawGeneration(windowSurface, generation):
    for i in range(SIZE_X):
        for j in range(SIZE_Y):
            if generation[i][j] == ALIVE:
                pygame.draw.rect(windowSurface, WHITE,(i*SCALE,j*SCALE,SCALE,SCALE), 0)

ALIVE = 1
DEAD = 0
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 720
SIZE_X = 150
SIZE_Y = 90
SCALE = 8
INITIAL_LIFE = 8

windowSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
generation = initializeRandomGeneration()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(BLACK)
    generation = updateGeneration(generation)
    drawGeneration(windowSurface, generation)
    pygame.display.update()
    



"""
Todo : 
Multicore processing
implementig neurons
Seperate the drawing function from updateing functions
You can call the drawing function indide the updating function and  then comment when you dont need to draw that is whole training
border and oragansim collision
get dynamic inputs to brain from the env for processig
"""

import pygame
import random
import pickle
from random import random, seed, randrange
from math import exp
import numpy as np
from brain import Brain
from organism import Organism
from datetime import datetime
#-----------------------------------
"""
This is our environment a n*n grid
Where in each a cell one and only one organism can live
Grid is initiated as a grid of None
Each step the grid will be updated
The grid will store the class organism
It will have all necessary attributes to draw it on the screen as well as to simulate it
"""
GRID_SIZE   = 64
ENV_GRID    = [[False for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
#-----------------------------------
WHITE       = (255,255,255)
RED         = (255, 0, 0)
FPS         = 30

SCALER      = 16
CIRCLE_SIZE = SCALER/2
WIDTH       = GRID_SIZE * SCALER
HEIGHT      = GRID_SIZE * SCALER
WIN         = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulation')
#-----------------------------------
"""
Populating the environment with the oraganisms
"""
NO_OF_STEPS     = 200
NO_ORGANISM     = GRID_SIZE
ORGANISMS       = []
NO_OF_INPUTS    = 2 
NO_OF_OUTPUTS   = 2
NO_OF_HIDDEN    = 2



def randColor():
    return (randrange(0,255),randrange(0,255),randrange(0,255))

def populate_env(no_of_organism):
    print('Populating environment : ')
    NO_OF_ORGANISM  = no_of_organism
    i = 0
    while i < NO_OF_ORGANISM:
        seed(datetime.now()) # for generating position
        x,y = randrange(0,GRID_SIZE-1), randrange(0,GRID_SIZE-1)
        if not ENV_GRID[x][y]:
            print(x,y)
            seed(datetime.now()) # for generating colors and brain
            randColor()
            brain = Brain(NO_OF_INPUTS, NO_OF_HIDDEN, NO_OF_OUTPUTS)
            #ENV_GRID[x][y] = Organism(randColor(), (x,y), CIRCLE_SIZE, brain) #obsolete
            ENV_GRID[x][y] = True
            ORGANISMS.append(Organism(randColor(), (x,y), CIRCLE_SIZE, brain))
            i += 1
    #helper function
    '''
    for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if ENV_GRID[i][j]:
                    print(ENV_GRID[i][j].pos)
    '''
    print('Done Populating environment : ')
populate_env(NO_ORGANISM)
#-----------------------------------
STEP = 0

def survialCheck(env):
    for i in rage(GRID_SIZE):
        for j in range(GRID_SIZE):
            if i < GRID_SIZE//2:
                env[i][j] = None

#do not implement yet

def update_env(clock):
    global STEP
    STEP += 1
    
    if STEP < NO_OF_STEPS:
        print(clock.get_fps(), STEP)
        WIN.fill(WHITE)
        for org in ORGANISMS:
            pygame.draw.circle(WIN, org.color, (org.pos[0] * SCALER, org.pos[1] * SCALER), org.radius)
            prev_pos = org.pos
            output = org.brain.forward_propogate([1,1])
            if org.move(output, ENV_GRID):
                ENV_GRID[prev_pos[0]][prev_pos[1]]   = False
                ENV_GRID[org.pos[0]][org.pos[1]]     = True
        """
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if ENV_GRID[i][j]:
                    pygame.draw.circle(WIN, ENV_GRID[i][j].color, (ENV_GRID[i][j].pos[0] * SCALER, ENV_GRID[i][j].pos[1] * SCALER), ENV_GRID[i][j].radius)
                    output = ENV_GRID[i][j].brain.forward_propogate([1,1])
                    ENV_GRID[i][j].move(output, ENV_GRID)
    #            print(output)
        """
    else:
        print('Done')
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        update_env(clock)    

    pygame.quit()

if __name__ == "__main__":
    main()
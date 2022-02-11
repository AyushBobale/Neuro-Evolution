"""
Todo : 
** Check update env function
Multicore processing
implementig neurons
Seperate the drawing function from updateing functions
You can call the drawing function indide the updating function and  then comment when you dont need to draw that is whole training
border and oragansim collision
get dynamic inputs to brain from the env for processig
evolution capture 
and evolution replay
so that at first the generation could be done and then replayed
"""

import pygame
import random
import pickle
from random import random, seed, randrange, choices
from math import exp
import numpy as np
from brain import Brain
from organism import Organism
from replay import Replay
from datetime import datetime
#-----------------------------------
"""
This is our environment a n*n grid
Where in each a cell one and only one organism can live
Grid is initiated as a grid of None
Each step the grid will be updated
The grid will store the class organism [modidfed for optimization]
It will have all necessary attributes to draw it on the screen as well as to simulate it
"""
GRID_SIZE       = 64
GEN             = 0
GENERATION      = [] # will be used to store snapshots of each gen either before survival check or after survival check
REPLAY_DUMP     = [] # possible functionality of dumping the animation of each gen if real time computation is not posible
ENV_GRID        = [[False for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
#-----------------------------------
WHITE           = (255,255,255)
RED             = (255, 0, 0)
FPS             = 5

SCALER          = 16
CIRCLE_SIZE     = SCALER/2
WIDTH           = GRID_SIZE * SCALER
HEIGHT          = GRID_SIZE * SCALER
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simulation')

"""
Populating the environment with the organisms
"""
MUTATION_FACTOR = 10 #% change in the weight for my own convinience
NO_OF_STEPS     = 25
NO_ORGANISM     = GRID_SIZE
ORGANISMS       = []
STEP            = 0
NO_OF_INPUTS    = 2 
NO_OF_OUTPUTS   = 2
NO_OF_HIDDEN    = 2
#-----------------------------------

REPLAY_DUMP = Replay(GRID_SIZE, SCALER)


#-----------------------------------
def object_to_color(object):
    h = hash(object)
    return (h%1000%255,h%1000000//1000%255,h%1000000000//1000000%255)

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
            brain = Brain(NO_OF_INPUTS, NO_OF_HIDDEN, NO_OF_OUTPUTS)
            #ENV_GRID[x][y] = Organism(randColor(), (x,y), CIRCLE_SIZE, brain) #obsolete
            ENV_GRID[x][y] = True
            ORGANISMS.append(Organism(object_to_color(brain), (x,y), CIRCLE_SIZE, brain))
            i += 1
    print('Done Populating environment : ')
populate_env(NO_ORGANISM)
#-----------------------------------


def survialCheck(ORGANISMS):
    for org in ORGANISMS:
        if int(org.pos[0] > GRID_SIZE / 2) and int(org.pos[1] > GRID_SIZE / 2):
            #print(org.pos[0], org.pos[1])
            ENV_GRID[org.pos[0]][org.pos[1]] = False
            ORGANISMS.remove(org)
    print('Surviors : ', len(ORGANISMS))

def genomeCombiner(parent_a, parent_b):
    #complex shit do not change
    new_brain   = Brain(NO_OF_INPUTS, NO_OF_HIDDEN, NO_OF_HIDDEN)
    brain_a     = parent_a.brain
    brain_b     = parent_b.brain
    temp_var    = [1,-1]
    for layer in range(len(brain_a.network)):
        for neuron in range(len(brain_a.network[layer])):
            for weight in range(len(brain_a.network[layer][neuron]['weights'])):
                seed(datetime.now())
                direction               = choices(temp_var)
                multiplicative_factor   = 1 + (direction[0] * MUTATION_FACTOR)/100
                new_brain.network[layer][neuron]['weights'][weight] = ((brain_a.network[layer][neuron]['weights'][weight] * multiplicative_factor) + (brain_b.network[layer][neuron]['weights'][weight] * multiplicative_factor))/2
            #for weight in neuron['weights']:
            #    print(layer, neuron, weight)
        #print(layer)
    return new_brain


def repopulate():
    global ENV_GRID, ORGANISMS, NO_ORGANISM
    new_generation  = []
    ENV_GRID        = [[False for i in range(GRID_SIZE)] for j in range(GRID_SIZE)]
    while len(new_generation) < NO_ORGANISM:
        seed(datetime.now()) # for generating position
        x,y = randrange(0,GRID_SIZE-1), randrange(0,GRID_SIZE-1)
        if not ENV_GRID[x][y]:
            parent_a, parent_b  = choices(ORGANISMS, k = 2)
            new_organism_brain  = genomeCombiner(parent_a, parent_b)
            new_color           = [(parent_a.color[i] + parent_b.color[i])/2 for i in range(len(parent_a.color))]
            new_color           = tuple(new_color)
            new_organism        = Organism(object_to_color(new_organism_brain), (x,y), CIRCLE_SIZE, new_organism_brain)
            new_generation.append(new_organism)
            ENV_GRID[x][y] = True
    ORGANISMS = new_generation

def update_env(clock):
    global STEP, GEN, GENERATION, ORGANISMS
    STEP += 1
    # to implement changing generation functionality basically implementing evolution
    if STEP < NO_OF_STEPS:
        #GENERATION.append(ORGANISMS)
        """
        The issue is in the else part
        how the generations are appended i guess
        """
        #print(ORGANISMS[0].pos, STEP)
        #print('FPS : ', clock.get_fps())
        WIN.fill(WHITE)
        for org in ORGANISMS:
            pygame.draw.circle(WIN, org.color, ((org.pos[0] * SCALER) + SCALER/2, (org.pos[1] * SCALER) + SCALER/2), org.radius)
            prev_pos = org.pos
            '''#implement dynamic input'''
            output = org.brain.forward_propogate([-10,-10])
            if org.move(output, ENV_GRID):
                ENV_GRID[prev_pos[0]][prev_pos[1]]   = False
                ENV_GRID[org.pos[0]][org.pos[1]]     = True
        GENERATION.append(ORGANISMS)
        print(ORGANISMS[0].pos)

    else:
        """REPLAY_DUMP.root.append(GENERATION)
        for ste in GENERATION:
            print('check', ste[0].pos)
        GENERATION = []"""
        """-----------------------------------------"""
        print('Gen : ',GEN)
        survialCheck(ORGANISMS)
        print('No of survivors', len(ORGANISMS))
        repopulate()
        WIN.fill(WHITE)
        for org in ORGANISMS:
            pygame.draw.circle(WIN, org.color, ((org.pos[0] * SCALER) + SCALER/2, (org.pos[1] * SCALER) + SCALER/2), org.radius)
        GEN += 1
        STEP = 0
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                REPLAY_DUMP.steps = GENERATION
                for ste in REPLAY_DUMP.steps:
                    print(ste[0].pos)
                print('rplydump len of steps', len(REPLAY_DUMP.steps))
                dumpfile = open('replay.dump', 'wb')
                #print('No of generations    :',len(REPLAY_DUMP.root))
                #print('No of steps          :',len(REPLAY_DUMP.root[0]))
                pickle.dump(REPLAY_DUMP, dumpfile)
                dumpfile.close()
                run = False
        update_env(clock)    

    pygame.quit()

'''class Evolution:
    def __init__(self, gridsize, no_of_steps, no_of_gens):
        self.organisms      = []
        self.replaydump     = None
        self.gridsize       = gridsize
        self.envgrid        = [[False for i in range(gridsize)] for j in range(gridsize)]
        self.no_of_steps    = no_of_steps
        self.no_of_gens     = no_of_gens
        self.replay         = []
        self.input          = [-10,-10]             # del this later just a temp fix need to take input dynamically from the env

    def object_to_color(object):
        h = hash(object)
        return (h%1000%255,h%1000000//1000%255,h%1000000000//1000000%255)

    def populate_env(self, no_of_inputs, no_of_hidden, no_of_outputs, cirle_size): 
        i = 0
        while i < self.no_of_organism:
            seed(datetime.now())
            x,y = randrange(0, self.gridsize-1), randrange(0, self.gridsize -1)
            if not self.envgrid:
                seed(datetime.now())
                brain = Brain(no_of_inputs, no_of_hidden, no_of_outputs)
                self.envgrid[x][y] = True
                self.organisms.append(Organism(object_to_color(brain), (x,y), cirle_size, brain))
                i += 1
        print("Done populating environment : ")

    def evolve(self):
        for gen in range(self.no_of_gens):#single gen
            step = []
            # this loop perfroms set tranformations for given no of steps
            for step in range(self.no_of_steps): # single step 
                # this for loop is perfroming transformation on over organisms
                for organism in self.organisms:
                    previous_pos    = oragansim.pos
                    direction       = oragansim.brain.forward_propogate(self.input)
                    if oragansim.move(direction):
                        self.envgrid[previous_pos[0]][previous_pos[1]]          = False
                        self.envgrid[oragansim.pos[0]][self.oragansim.pos[1]]   = True
                step.append(self.organisms)
            self.replay.append(step)
            print('Gen : ', gen)
            self.survialCheck'''
    



if __name__ == "__main__":
    #main()
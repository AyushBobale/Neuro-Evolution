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

'''
Try and remove the circle_size from this class 
changes needed to be made in organism class in order to make such modification
'''
class Evolution:
    def __init__(self, gridsize, no_of_steps, no_of_gens, circle_size, no_of_inputs, no_of_hidden, no_of_outputs, mutation_factor):
        self.mutation_factor    = mutation_factor
        self.no_of_inputs       = no_of_inputs
        self.no_of_hidden       = no_of_hidden
        self.no_of_outputs      = no_of_outputs
        self.circle_size        = circle_size
        self.organisms          = []
        self.replaydump         = None
        self.gridsize           = gridsize
        self.no_of_organisms    = gridsize
        self.envgrid            = [[False for i in range(gridsize)] for j in range(gridsize)]
        self.no_of_steps        = no_of_steps
        self.no_of_gens         = no_of_gens
        self.replay             = []
        self.input              = [-10,-10]             # del this later just a temp fix need to take input dynamically from the env

    def object_to_color(self,object):
        h = hash(object)
        return (h%1000%255,h%1000000//1000%255,h%1000000000//1000000%255)

    def populate_env(self): 
        i = 0
        while i < self.no_of_organisms:
            seed(datetime.now())
            x,y = randrange(0, self.gridsize-1), randrange(0, self.gridsize -1)
            if not self.envgrid[x][y]:
                seed(datetime.now())
                brain = Brain(self.no_of_inputs, self.no_of_hidden, self.no_of_outputs)
                self.envgrid[x][y] = True
                self.organisms.append(Organism(self.object_to_color(brain), (x,y), self.circle_size, brain))
                i += 1
        print("Done populating environment : ")

    def survial_check(self):
        for organism in self.organisms:
            if organism.pos[0] > self.gridsize/2 and organism.pos[1] > self.gridsize/2:
                self.envgrid[organism.pos[0]][organism.pos[1]]    = False
                self.organisms.remove(organism)
        print('Done survival check deleted unfit organisms :')

    def genome_combiner(self, parent_a, parent_b):
        #complex shot do not change
        new_brain       = Brain(self.no_of_inputs, self.no_of_hidden, self.no_of_outputs)
        brain_a         = parent_a.brain
        brain_b         = parent_b.brain
        temp_var        = [1, -1]
        for layer in range(len(brain_a.network)):
            for neuron in range(len(brain_a.network[layer])):
                for weight in range(len(brain_a.network[layer][neuron]['weights'])):
                    seed(datetime.now())
                    direction               = choices(temp_var)
                    multiplicative_factor   = 1 + (direction[0] * self.mutation_factor)/100
                    new_brain.network[layer][neuron]['weights'][weight] = ((brain_a.network[layer][neuron]['weights'][weight] * multiplicative_factor) + (brain_b.network[layer][neuron]['weights'][weight] * multiplicative_factor))/2
        return new_brain
    
    def repopulate(self):
        new_generation      = []
        self.envgrid        = [[False for i in range(self.gridsize)] for j in range(self.gridsize)]
        while len(new_generation) < self.no_of_organisms:
            seed(datetime.now())
            x,y = randrange(0, self.gridsize-1), randrange(0, self.gridsize -1)
            if not self.envgrid[x][y]:
                parent_a, parent_b  = choices(self.organisms, k = 2)
                new_organism_brain  = self.genome_combiner(parent_a, parent_b)
                new_color           = [(parent_a.color[i] + parent_b.color[i])/2 for i in range(len(parent_a.color))]
                new_organism        = Organism(self.object_to_color(new_organism_brain), (x,y), self.circle_size, new_organism_brain)
                new_generation.append(new_organism)
                self.envgrid[x][y]        = True
        self.organisms = new_generation
        print('Done repopulating')

    def evolve(self):
        for gen in range(self.no_of_gens):#single gen
            steps = []
            # this loop perfroms set tranformations for given no of steps
            for step in range(self.no_of_steps): # single step 
                # this for loop is perfroming transformation on over organisms
                for organism in self.organisms:
                    previous_pos    = organism.pos
                    direction       = organism.brain.forward_propogate(self.input)
                    if organism.move(direction, self.envgrid):
                        self.envgrid[previous_pos[0]][previous_pos[1]]          = False
                        self.envgrid[organism.pos[0]][organism.pos[1]]   = True
                steps.append(self.organisms)
            self.replay.append(steps)
            print('Gen : ', gen)
            self.survial_check()
            print('No of survivors : ', len(self.organisms))
            self.repopulate()
        print('Done evolution : ')
        return self.replay
    


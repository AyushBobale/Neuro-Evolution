from brain import Brain
from random import random, choices, seed
from datetime import datetime

bren1 = Brain(2,2,2)
bren2 = Brain(2,2,2)

for layer in bren1.network:
    print(layer)
print()
for layer in bren2.network:
    print(layer)
print()

NO_OF_INPUTS    = 2 
NO_OF_OUTPUTS   = 2
NO_OF_HIDDEN    = 2
MUTATION_FACTOR = 1

def genomeCombiner(parent_a, parent_b):
    #complex shit do not change
    new_brain   = Brain(NO_OF_INPUTS, NO_OF_HIDDEN, NO_OF_HIDDEN)
    brain_a     = parent_a#.brain
    brain_b     = parent_b#.brain
    temp_var    = [1,-1]
    for layer in range(len(brain_a.network)):
        for neuron in range(len(brain_a.network[layer])):
            for weight in range(len(brain_a.network[layer][neuron]['weights'])):
                seed(datetime.now())
                direction               = choices(temp_var)
                multiplicative_factor   = 1 + (direction[0] * MUTATION_FACTOR)/100
                print(multiplicative_factor) 
                new_brain.network[layer][neuron]['weights'][weight] = ((brain_a.network[layer][neuron]['weights'][weight] * multiplicative_factor) + (brain_b.network[layer][neuron]['weights'][weight] * multiplicative_factor))/2
            #for weight in neuron['weights']:
            #    print(layer, neuron, weight)
        #print(layer)
    return new_brain

new_brain = genomeCombiner(bren1, bren2)
print()
for layer in new_brain.network:
    print(layer)
print()
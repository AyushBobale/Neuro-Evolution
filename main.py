from evolution import Evolution
from displayreplay import DisplayReplay
import pickle
#import pandas as pd
"""
*******
Logging system
reworking the neurons
fitness function
Change the random number generator in the brain module the weights are getting instantiated pretty much the same
Implement 4 way ouput signifying up/down/left/right rather that taking in direction
sample size too small not enough diversity
Try to modify the neuron as much as possible
*******
Implement controls
"""
Simulation = Evolution( gridsize        = 128,
                        org_scaler      = 4,
                        no_of_steps     = 150,
                        no_of_gens      = 500,
                        no_of_inputs    = 2,
                        no_of_hidden    = 2,
                        no_of_outputs   = 2,
                        mutation_factor = 100, # acts as the learining rate
)

print('\n')
Simulation.populate_env()

replay = Simulation.evolve()

pickle_file = open('replay.pkl', 'wb')
pickle.dump(replay, pickle_file)

#replay = pickle.load()

print("Gens : ",len(replay))
print("Steps : ",len(replay[0]))

#show = DisplayReplay(replay, Simulation.gridsize, 8, 60, 'Simulation')
#show.run_replay()


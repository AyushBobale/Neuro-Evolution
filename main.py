from evolution import Evolution
from displayreplay import DisplayReplay
import pickle
"""
*******
Change the random number generator in the brain module the weights are getting instantiated pretty much the same
*******
Implement controls
"""
Simulation = Evolution( gridsize        = 64,
                        no_of_steps     = 150,
                        no_of_gens      = 200,
                        no_of_inputs    = 2,
                        no_of_hidden    = 2,
                        no_of_outputs   = 2,
                        mutation_factor = 1,
)

print('\n')
Simulation.populate_env()

replay = Simulation.evolve()

pickle_file = open('replay.pkl', 'wb')
pickle.dump(replay, pickle_file)

#replay = pickle.load()

print("Gens : ",len(replay))
print("Steps : ",len(replay[0]))

show = DisplayReplay(replay, 64, 10, 60, 'Simulation')
show.run_replay()


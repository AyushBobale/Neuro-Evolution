from evolution import Evolution
from displayreplay import DisplayReplay
import pickle

Simulation = Evolution( gridsize        = 128,
                        no_of_steps     = 200,
                        no_of_gens      = 120,
                        no_of_inputs    = 2,
                        no_of_hidden    = 2,
                        no_of_outputs   = 2,
                        mutation_factor = 10,
)

print('\n')
Simulation.populate_env()

replay = Simulation.evolve()

pickle_file = open('replay.pkl', 'wb')
pickle.dump(replay, pickle_file)

replay = pickle.load()

print("Gens : ",len(replay))
print("Steps : ",len(replay[0]))

show = DisplayReplay(replay, 128, 8, 60, 'Simulation')
show.run_replay()


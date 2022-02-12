from evolution import Evolution
from displayreplay import DisplayReplay

Simulation = Evolution( gridsize        = 128,
                        no_of_steps     = 200,
                        no_of_gens      = 50,
                        no_of_inputs    = 2,
                        no_of_hidden    = 2,
                        no_of_outputs   = 2,
                        mutation_factor = 10,
)

print('\n')
Simulation.populate_env()

replay = Simulation.evolve()
print("Gens : ",len(replay))
print("Steps : ",len(replay[0]))

show = DisplayReplay(replay, 128, 8)
show.run_replay()


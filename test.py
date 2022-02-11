from evolution import Evolution

SCALER     = 8
Simulation = Evolution( gridsize        = 64,
                        no_of_steps     = 25,
                        no_of_gens      = 5,
                        circle_size     = SCALER,
                        no_of_inputs    = 2,
                        no_of_hidden    = 2,
                        no_of_outputs   = 2,
                        mutation_factor = 10,
)
Simulation.populate_env()
replay = Simulation.evolve()
print("Gens : ",len(replay))
print("Steps : ",len(replay[0]))
for gen in replay:
    for step in gen:
        print(step[1].pos)
    break
from evolution import Evolution

SCALER     = 8
Simulation = Evolution( gridsize        = 8,
                        no_of_steps     = 5,
                        no_of_gens      = 1,
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

for gen in replay:
    for step in gen:
        pos = [i.pos for i in step]
        print(pos)
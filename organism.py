#-----------------------------------
"""
the brain has to spit out any possible action that can be performed in the environment
"""
class Organism:
    def __init__(self, color, pos, radius, brain):
        #unused yet 
        self.speed              = 1
        self.mutation_factor    = 1 # this is % chance
        
        self.brain              = brain #[gotta implemnent a neural network] initiated as random weights for each of the creature
        self.genome             = None

        #helper variables
        self.pos                = pos
        self.color              = color
        self.radius             = radius
    
    def move(self, direction, env): 
        pos = (round(self.pos[0] + direction[0] * self.speed), round(self.pos[1] + direction[1] * self.speed))
        if pos[0] < len(env) and pos[1] < len(env):
            if not env[pos[0]][pos[1]]:
                self.pos = pos
        
    

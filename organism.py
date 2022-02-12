#-----------------------------------
"""
the brain has to spit out any possible action that can be performed in the environment
"""
class Organism:
    def __init__(self, color, pos, brain):
        self.speed              = 1
        self.brain              = brain #[gotta implemnent a neural network] initiated as random weights for each of the creature

        #helper variables
        self.pos                = pos
        self.color              = color
    
    def move(self, direction, env): 
        pos = (round(self.pos[0] + direction[0] * self.speed), round(self.pos[1] + direction[1] * self.speed))
        #print(pos)
        if pos[0] < len(env) and pos[1] < len(env) and pos[0] >= 0 and pos[1] >= 0 :
            if not env[pos[0]][pos[1]]:
                self.pos = pos
                return True
            else:
                return False
        else:
            return False
        
    

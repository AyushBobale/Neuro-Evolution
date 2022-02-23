from gym import Env 
from gym.spaces import Discrete, Box
import numpy as np
import random
import logging

logging.basicConfig(level   = logging.DEBUG,
                    format  = '%(levelname)s : %(funcName)s : %(lineno)d : %(message)s' )

class MyEnv(Env):
    def __init__(self):
        logging.info('MyEnv initialized')
        
        self.action_space       = Discrete(4)
        # can be said as the state of the organism lets say health
        self.state              = 100
        #dunno what the heck is this
        self.observation_space  = Box(low=np.array([0]), high=np.array([100]))
        self.run_length         = 60

    def step(self):
        pass

    def render(self):
        pass

    def reset(self):
        pass

env = MyEnv()
logging.debug(f'Observation space : {env.action_space.sample()}')
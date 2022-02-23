import numpy as np
from gym.spaces import Discrete, Box
import logging
logging.basicConfig(level   = logging.INFO,
                    format  = '%(levelname)s : %(funcName)s : %(lineno)d : %(message)s' )
logging.info(Box(low=np.array([0]), high=np.array([100])))
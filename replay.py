class Replay:
    def __init__(self, grid_size, scaler):
        """ 
        Structure
        root_list = [
            [gen1
                [step1],
                [stepn]
            ],
            [genn
                [step1],
                [stepn]
            ],
        ]
        Impement draw function in itself so no extra dependencies are required
        """
        self.root       = []
        self.steps      = None
        self.grid_size  = grid_size
        self.scaler     = scaler



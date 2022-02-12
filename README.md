# Simulating Evolution using Simple Neural Networks

A simple python program that tries to simulate evolution using simple neural networks.

A random sample population is created with each having a feed forward neural network as it's brain attribute.

For each organism in the population the weights are choosen randomly the idea is that there will a certain organims with somewhat ideal weights according to the survival condition.

For each subsequent generation only the ones who survived are allowed to reproduce.

A random amount of mutation is done in each generation such that there is possiblity of finding more ideal weights than the ones found in first generation.

## Sample Screen shots 
The survival condition here is the organism survives if the it resides in the upper left hand corner

```python
    organism.pos[0] > self.gridsize/2 and organism.pos[1] > self.gridsize/2
```



The color is derived from the hashes of the neural networks thus representing the similarities/dissimilarities between each organism

1. ![Initial generation]('https://github.com/AyushBobale/Neuro-Evolution/blob/main/images/initialgen.png')

2. ![Later generation]('https://github.com/AyushBobale/Neuro-Evolution/blob/main/images/latergen.png')


## How to run 
1. Download the repo
2. Install pygame module 
    ```bash 
    pip install pygame 
3. Run main.py
    ```bash
    python main.py
[The main file upon running will create a file a dump file that can be loade later to run without running the simulation]

## Features to be implemented 
1. While drawing the simulation post evolution options to skip to generations / speed up drawing speed and reversing .
2. More dynamic and complex survival checks, multiple survival checks.
3. Increaing the complexity of the organims adding food, sensory organs, social interactions, etc.
5. A way to export the adjusted neural network that can be used as an actual problem solver for real world problems.
4. Trying multithreaded evolution capabilites.


## Refrences 
1. [The code for neural network with explanation](https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/)






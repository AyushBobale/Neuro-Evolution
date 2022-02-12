# Simulating Evolution using Simple Neural Networks

A simple python program that tries to simulate evolution using simple neural networks.

A random sample population is created with each having a feed forward neural network as it's brain attribute.

For each organism in the population the weights are choosen randomly the idea is that there will a certain organims with somewhat ideal weights according to the survival condition.

For each subsequent generation only the ones who survived are allowed to reproduce.

A random amount of mutation is done in each generation such that there is possiblity of finding more ideal weights than the ones found in first generation.

## How to run :
1. Download the repo
2. Install pygame module 
    ```bash 
    pip install pygame 
3. Run main.py
    ```bash
    python main.py
[The main file upon running will create a file a dump file that can be loade later to run without running the simulation]


## Refrences :
1. [The code for neural network with explanation](https://machinelearningmastery.com/implement-backpropagation-algorithm-scratch-python/)






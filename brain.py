from random import random, seed
from math import exp
import numpy as np

class Brain:    
    def __init__(self, n_inputs, n_hidden, n_outputs):
        self.network    = list()
        hidden_layer    = [{'weights': [random() for i in range(n_inputs + 1)]} for j in range(n_hidden)]
        self.network.append(hidden_layer)
        output_layer    = [{'weights':[random() for i in range(n_hidden + 1)]} for j in range(n_outputs)]
        self.network.append(output_layer)

    #there is no expected output
    def activate(self, weights, inputs):
        activation = weights[-1]
        for i in range(len(weights)-1):
            activation += weights[i] * inputs[i]
        return activation

    def transfer(self, activation):
        return np.tanh(activation)

    def forward_propogate(self, row):
        inputs = row
        for layer in self.network:
            new_inputs = []
            for neuron in layer:
                activation          = self.activate(neuron['weights'], inputs)
                neuron['output']    = self.transfer(activation)
                new_inputs.append(neuron['output'])
            inputs = new_inputs

        return inputs


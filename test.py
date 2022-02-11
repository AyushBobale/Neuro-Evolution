from brain import Brain
from random import random, choices, seed
from datetime import datetime
from organism import Organism
import pickle
from replay import Replay

dumpfile = open('replay.dump', 'rb')
gens = pickle.load(dumpfile)
print(len(gens.root))
print(len(gens.root[0]))
print(gens.root[0][1][0].pos)


for step in gens.root[10]:
    print(step[0].pos)
c = []
b = []
a = [i for i in range(5)]

def run():
    global b, a
    for i in range(5):
        b = []
        for j in range(5):
            temp_list = []
            for org in a:
                org += 1
                temp_list.append(org)
            a = temp_list
            b.append(temp_list)
        c.append(b)
run()
for gen in c:
    print(gen)



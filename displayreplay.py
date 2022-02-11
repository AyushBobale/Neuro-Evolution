from brain import Brain
from random import random, choices, seed
from datetime import datetime
from organism import Organism
import pickle

from replay import Replay
import pygame

dumpfile        = open('replay.dump', 'rb')
generations     = pickle.load(dumpfile)
WHITE           = (255,255,255)
BLACK           = (0,0,0)
SCALER          = generations.scaler
FPS             = 50
WIDTH           = generations.grid_size * generations.scaler
HEIGHT          = generations.grid_size * generations.scaler
WIN             = pygame.display.set_mode((WIDTH, HEIGHT))
GEN             = 0
STEP            = 0
NO_OF_STEPS     = len(generations.root[0])
print(NO_OF_STEPS)
print(len(generations.root))

"""
make it such that the game knows which step to display 
use while loops and increase the counter after a frame update
"""

def draw(clock):
    global GEN, STEP
    if_draw =  True
    #while if_draw:
    if GEN < len(generations.root):
        if STEP < NO_OF_STEPS:
            STEP += 1
            WIN.fill(WHITE)
            print(GEN, STEP, generations.root[GEN][STEP-1][0].pos)
            for org in generations.root[GEN][STEP-1]:
                #print(org.pos)
                pygame.draw.circle(WIN, org.color, ((org.pos[0] * SCALER) + SCALER/2, (org.pos[1] * SCALER) + SCALER/2), org.radius)
        else:
            STEP = 0
            GEN += 1
    else:
        WIN.fill(BLACK)
    pygame.display.update()
    

    """
    for generation in generations.root:
        for step in generation:
            WIN.fill(WHITE)
            for org in step:
                print(org.pos[0],org.pos[1])
                pygame.draw.circle(WIN, org.color, ((org.pos[0] * SCALER) + SCALER/2, (org.pos[1] * SCALER) + SCALER/2), org.radius)
                pygame.display.update()
    """

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            ''' Implement pausing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    continue
            '''
            if event.type == pygame.QUIT:
                run = False
        draw(clock)    

    pygame.quit()




if __name__ == "__main__":
    main()
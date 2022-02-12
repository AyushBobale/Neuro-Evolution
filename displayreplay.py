import pygame

"""
Implement dynamic fps
"""

class DisplayReplay:
    def __init__(self, replaydata, gridsize, scaler, fps, name):
        self.replaydata = replaydata
        self.bgcolor    = (255,255,255)
        self.scaler     = scaler
        self.circle_size= scaler/2
        self.fps        = fps
        self.gridsize   = gridsize
        self.width      = self.gridsize * self.scaler
        self.height     = self.gridsize * self.scaler
        self.window     = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(name)

    def draw(self):
        """
        will encounter the same problem as previous the animation will be too fast
        we will display all gens in a single frame gotta implement while loop
        """
        self.window.fill(self.bgcolor)
        for org in self.replaydata[self.gen_counter][self.step_counter]:
            position = ((org.pos[0] * self.scaler) + self.scaler/2, (org.pos[1] * self.scaler) + self.scaler/2)
            pygame.draw.circle(self.window, org.color, position, self.circle_size)
        self.step_counter += 1
        pygame.display.update()
    
    def run_replay(self):
        self.gen_counter    = 0
        self.step_counter   = 0
        self.clock          = pygame.time.Clock()
        self.run            = True
        while self.run:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            if self.gen_counter < len(self.replaydata):
                if self.step_counter < len(self.replaydata[0]):
                    self.draw()
                else:
                    self.step_counter   = 0
                    self.gen_counter    +=1
            else:
                self.window.fill((0,0,0))
        pygame.quit()
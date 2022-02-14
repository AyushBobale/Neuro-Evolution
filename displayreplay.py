import pygame

"""
Implement dynamic fps
"""

class DisplayReplay:
    def __init__(self, replaydata, gridsize, scaler, fps, name):
        self.replaydata = replaydata
        pygame.font.init()
        self.font       = pygame.font.Font("RobotoSerif-Light.ttf", scaler * 3)
        self.bgcolor    = (255,255,255)
        self.black      = (0,0,0)
        self.scaler     = scaler
        self.circle_size= scaler/2
        self.fps        = fps
        self.gridsize   = gridsize
        self.width      = self.gridsize * self.scaler
        self.height     = self.gridsize * self.scaler 
        #temp_var
        text            = self.font.render('Sample', True, (0,0,0))
        text_height     = text.get_height()
        #--------
        self.window     = pygame.display.set_mode((self.width,self.height + text_height))
        pygame.display.set_caption(name)
    
    def draw_text(self, text, pos):
        text            = self.font.render(text, True, self.black)
        text_width      = text.get_width()
        text_height     = text.get_height()
        text_rect       = text.get_rect()
        text_rect.center= (pos[0] + text_width/2, pos[1] + text_height/2)
        return text, text_rect

    def draw(self):
        text_gen        = "Gen : " + str(self.gen_counter) + " Step : " + str(self.step_counter)
        text, text_rect = self.draw_text(text_gen, (10, self.height +2))
        self.window.fill(self.bgcolor)
        for org in self.replaydata[self.gen_counter][self.step_counter]:
            position = ((org.pos[0] * self.scaler) + self.scaler/2, (org.pos[1] * self.scaler) + self.scaler/2)
            pygame.draw.circle(self.window, org.color, position, self.circle_size)
            pygame.draw.line(self.window,self.black, (0,self.height), (self.width, self.height))
            self.window.blit(text, text_rect)
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

            #-----------------------
            if self.gen_counter < len(self.replaydata):
                if self.step_counter < len(self.replaydata[0]):
                    self.draw()
                else:
                    self.step_counter   = 0
                    self.gen_counter    +=1
            else:
                self.window.fill((0,0,0))
        pygame.quit()
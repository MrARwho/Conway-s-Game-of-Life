import numpy as np
import matplotlib.pyplot as plt
import time 
import pygame


class Gameofline:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.old_state = np.zeros((self.height, self.width), dtype=int)
        self.new_state = np.zeros((self.height, self.width), dtype=int)
    
    #random initialization with more dead then alive 
    def inititalize(self, random=True):
        self.old_state = np.random.choice([0, 1], size=(self.height, self.width), p=[0.9, 0.1])
    
    #check for alive neighbors (8-directional(up down left right and diagonals)) of a cell using modulo for wrap around
    def alive_neighbors(self, x, y):
        total = int((self.old_state[x, (y-1)%self.width] + self.old_state[x, (y+1)%self.width] + 
                     self.old_state[(x-1)%self.height, y] + self.old_state[(x+1)%self.height, y] + 
                     self.old_state[(x-1)%self.height, (y-1)%self.width] + self.old_state[(x-1)%self.height, (y+1)%self.width] + 
                     self.old_state[(x+1)%self.height, (y-1)%self.width] + self.old_state[(x+1)%self.height, (y+1)%self.width]))
        return total
    #main nested for loop to update the state of each cell based on the rules of the game 
    def update(self):
        for x in range(self.height):
            for y in range(self.width):
                alive_neighbors = self.alive_neighbors(x, y)
                if self.old_state[x, y] == 1:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        self.new_state[x, y] = 0
                    else:
                        self.new_state[x, y] = 1
                else:
                    if alive_neighbors == 3:
                        self.new_state[x, y] = 1
                    else:
                        self.new_state[x, y] = 0
        self.old_state = np.copy(self.new_state)
  
def main():
    height = 100    
    width = 100
    game = Gameofline(height, width)
    game.inititalize()
    #visialization using pygame(each cell is represented as a 5x5 pixel square)
    pygame.init()
    screen = pygame.display.set_mode((width*5, height*5))
    pygame.display.set_caption("Conway's Game of Life")
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        game.update()
        screen.fill((0, 0, 0))
        for x in range(height):
            for y in range(width):
                if game.old_state[x, y] == 1:
                    pygame.draw.rect(screen, (255, 255, 255), (y*5, x*5, 10, 10))
        pygame.display.flip()
        clock.tick(10)
        
    
    
if __name__ == "__main__":    
    main()
    
    
    
    
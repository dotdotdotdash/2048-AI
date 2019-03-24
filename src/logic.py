#!/usr/bin/env python

import numpy as np
import random

class Game():
    def __init__(self):
        self.game_over = False
        self.current_matrix = np.zeros((4,4), dtype = np.int)
        for i in range(2):
            self.create_population()

    def create_population(self):
        i = random.randint(0,3)
        j = random.randint(0,3)
        populated = False
        while not populated:
            if self.current_matrix[i][j] == 0:
                self.current_matrix[i][j] = random.choice([2,4])
                populated = True
            else:
                i = random.randint(0,3)
                j = random.randint(0,3)
    
    def display(self):
        print(self.current_matrix)

game = Game()
game.display()

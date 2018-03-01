# -*- coding: utf-8 -*-
"""
Created on Sun Feb 18 13:19:12 2018

@author: venkatavaradhan lakshminarayanan
"""
import numpy as np
import random

class Board():
    def __init__(self):
        self.board = np.zeros((4,4), dtype = np.int)
        self.prev_board = np.zeros((4,4), dtype = np.int)
        self.new_game()
        print("New Board Created")
        self.newgame = False
        
    def new_game(self):
        for cnt in range(2):
            i = random.randint(0,3)
            j = random.randint(0,3)
            self.board[i][j] = random.choice([2,4])
            
    def populate(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] == 0:
                    empty.append([i,j])
        
        i,j = random.choice(empty)
        self.board[i][j] = random.choice([2,4])
                
    def move(self):
        k = 0
        for row in self.board:
            new_col = np.zeros(len(row), dtype=row.dtype)
            j = 0
            previous = None
            for i in range(row.size):
                if row[i] != 0:
                    if previous == None:
                        previous = row[i]
                    else:
                        if previous == row[i]:
                            new_col[j] = 2 * row[i]
                            j += 1
                            previous = None
                        else:
                            new_col[j] = previous
                            j += 1
                            previous = row[i]
            if previous != None:
                new_col[j] = previous  
            
            self.board[k] = new_col
            k += 1
            
    def next_move(self,direction):
        self.board = np.rot90(self.board, direction)
        self.move()
        self.board = np.rot90(self.board, -direction)
        
    def play_game(self,direction):
        self.next_move(direction)
        self.prev_board = self.board
        self.populate()
        
game = Board()
while True:
    print(game.board)
    key = int(input("Your move: "))
    game.play_game(key)
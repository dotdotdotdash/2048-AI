import numpy as np
import time
import os
import tensorflow as tf
from pyautogui import press
import random
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense
from logic import up, down, left, right
from tkinter import *

prev_mat = []
     
class agent:
    
    def __init__(self):
        self.states = []
        self.observation = []
        self.reward = []
        self.input_data = []
        self.output_data = []
        self.move_key = ['a','s','w','d']
        self.model = self.build_brain()
        
    def state_computation(self,observation):
        state_1 = sum(cell.count(0) for cell in observation)
        state_2 = 0
        for row in observation:
            state_2+=sum(row)
        
        self.states = [state_1,state_2]
                
    def choose_action(self):
        global prev_mat
        best_score = 0
        mat = []
        
        for index in self.move_key:
            score, mat = self.minimax(index)
        
            if mat != prev_mat:
                if score > best_score:
                    self.reward = [score, mat, index]
                    best_score = score
                        
        prev_mat = self.reward[1]
        return self.reward[2]
    
    def minimax(self,move):
        state_hat_2 = 0
        blocks = []
        
        if move =='a':
            next_matrix,_ = left(self.observation)
        elif move == 's':
            next_matrix,_ = down(self.observation)
        elif move == 'd':
            next_matrix,_ = right(self.observation)
        else:
            next_matrix,_ = up(self.observation)
            
        state_hat_1 = sum(cell.count(0) for cell in next_matrix)
        
#        for row in next_matrix:
#            for element in row:
#                blocks.append(element)
#        
#        blocks.sort(reverse=True)
#        state_hat_2 = max(blocks)
#        while 2**n == state_hat_2:
#            state_hat_2 = 10**n
#            if n != 1:
#                val = sum(cell.count(2**(n-1)) for cell in next_matrix)
                
        return state_hat_1, next_matrix
    
    def build_brain(self):
        self.model = Sequential()
        self.model.add(Dense(units=8,activation='relu',input_dim=2))
        self.model.add(Dense(units=1,activation='softmax'))
        self.model.compile(loss='mse',optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))
        return self.model
        
    def move(self,matrix,game_over):
        if game_over:
#            self.model.fit(np.asarray(self.input_data),np.asarray(self.output_data),epochs=5)
            print("Game Over ! Reinitializing")
            flag = True
        else:
            self.observation = matrix
            self.state_computation(self.observation)
            action = self.choose_action()
            press(action)
            self.input_data.append(self.states)
            self.output_data.append(action)
#            print("states: {} | action: {} | order: {}".format(self.states,action,self.move_key))
            flag = False
            
        return flag
            
        
        
        
        
        
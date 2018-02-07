import numpy as np
import time
import os
import tensorflow as tf
from pyautogui import press
import random
from keras.optimizers import SGD
from keras.models import Sequential
from keras.layers import Dense
     
class agent:
    
    def __init__(self):
        print("Agent Initialized")
        self.states = []
        self.reward = 0
        self.input_data = []
        self.output_data = []
        self.model = self.build_brain()
        
    def state_computation(self,observation):
        state_1 = sum(cell.count(0) for cell in observation)
        state_2 = 0
        for row in observation:
#            max_val = max(row)
            state_2+=sum(row)
#            if max_val >= state_2:
#                state_2 = max_val
        
        self.states = [state_1,state_2]
                
    def choose_action(self):
        moves_available = ['a','s','w','d']
        key_val = random.randint(0,3)
        key = moves_available[key_val]
        return key,key_val
    
    def build_brain(self):
        self.model = Sequential()
        self.model.add(Dense(units=8,activation='relu',input_dim=2))
        self.model.add(Dense(units=1,activation='softmax'))
        self.model.compile(loss='mse',optimizer=SGD(lr=0.01, momentum=0.9, nesterov=True))
        return self.model
        print("Brain initialized")
        
    def move(self,matrix,game_over):
        if game_over:
            self.model.fit(np.asarray(self.input_data),np.asarray(self.output_data),epochs=5)
            print("Agent trained")
        else:
            observation = matrix
            self.state_computation(observation)
            action,action_value = self.choose_action()
            press(action)
            self.input_data.append(self.states)
            self.output_data.append(action_value)
            print("states: {}".format(self.states))
        
        
        
        
        
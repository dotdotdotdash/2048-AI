import numpy as np
import time
import os
import tensorflow as tf
from pyautogui import press
import random
import keras
from keras.models import Sequential
from keras.layers import Dense
     
class agent:
    
    def __init__(self):
        print("Agent Initialized")
        self.states = []
        self.reward = 0
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
        key = moves_available[random.randint(0,3)]
        return key
    
    def build_brain(self):
        self.model = Sequential()
        self.model.add(Dense(units=8,activation='relu',input_dim=2))
        self.model.add(Dense(units=4,activation='softmax'))
        self.model.compile(loss='mse',optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
        print("Brain initialized")
        
    def move(self,matrix):
        observation = matrix
        self.state_computation(observation)
        press(self.choose_action())
        print("states: {}".format(self.states))
        
        
        
        
        
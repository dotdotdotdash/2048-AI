#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import numpy as np
from numpy import zeros

class Game:
    def __init__(self):
        rospy.init_node('game', anonymous=True)
        rospy.Subscriber("action", String, self.command_received)
        self.board = zeros((4, 4), dtype=np.int)
        self.game_over = False

    def command_received(self, msg):
        self.move(msg.data)

    def move(self, direction):
        self.display()

    def display(self):
        print(self.board)

    def is_game_over(self):
        pass

game = Game()
rospy.spin()

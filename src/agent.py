#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import random

def send_action():
    commands = ["w","s","a","d"]
    return commands[random.randint(0,3)]

if __name__ == "__main__":
    rospy.init_node('agent', anonymous=True)
    agent = rospy.Publisher("action", String, queue_size = 10)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        agent.publish(send_action())
        rate.sleep()

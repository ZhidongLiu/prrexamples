#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import random

rospy.init_node('Questions')

def choose_question(a):
    switcher = {
        1: "What is your favorite color?",
        2: "What is your name?",
        3: "Do you like Pito",
        4: "What kind os do you use?",
        5: "1+1=",
    }
    return switcher.get(a, "nothing")

pub = rospy.Publisher('Question', String, queue_size=10)
rate = rospy.Rate(0.5)
print "starting ask questions:"
print

while not rospy.is_shutdown(): 
    choice = random.randint(0,5)
    question = choose_question(choice)
    print question
    print
    pub.publish(question)
    rate.sleep()
rospy.spin()
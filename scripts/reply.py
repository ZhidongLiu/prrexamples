#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import random

def callback(msg):
    switcher = {
        "What is your favorite color?": random.choice(['Red', 'Black', 'White', 'Blue']),
        "What is your name?": 'Alex',
        "Do you like Pito": random.choice(['Yes! I like him.', 'No, he failed me!']),
        "What kind os do you use?": random.choice(['Windows', 'Linux', 'macOS']),
        "1+1=": random.choice(['2', 'You think I am stupid?']),
    }

    print switcher.get(msg.data, "nothing")
    print


rospy.init_node('Reply')

sub = rospy.Subscriber('Question', String, callback)
rospy.spin()
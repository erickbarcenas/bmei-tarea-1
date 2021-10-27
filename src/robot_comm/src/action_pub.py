#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Rate
from std_msgs.msg import String



def action_pub():
    pub = rospy.Publisher('topic', String, queue_size=1)
    rospy.init_node('action_pub', anonymous=True)
    print('Node created successfully!')
    rate = rospy.Rate(10) # 10 Hz
    # Below you write what you want to be published
    while not rospy.is_shutdown(): # While not pressing ctrl + c
        hello = "Hello world"
        pub.publish(hello)
        print(hello)
        rate.sleep()


if __name__ == '__main__':
    try:
        action_pub()
    except rospy.ROSInterruptException:
        pass

'''
class MoveRobot():
	def __init__(self):
	    pass
    
    def map_string(self):
		pass
    
    def stop(self):
        print('stop')




'''
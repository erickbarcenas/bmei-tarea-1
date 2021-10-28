#!/usr/bin/python3

import rospy
from geometry_msgs.msg import Twist
from rospy.timer import Rate
from std_msgs.msg import String



class MoveRobot():
    def __init__(self):

        if rospy.on_shutdown(self.get_stop):
            print('Program execution is stopped')

        self.mov_msg = Twist()
        # It does not move in Y because it is a plane
        self.mov_msg.linear.x = 0.0 # linear speed
        self.mov_msg.angular.z = 0.0 # angular speed

        # Depending on the text the Twist message will change
                    #      X  ,  Z
        self.mov_dic = {
            'avanza':   [0.15 , 0.0],
            'gira':     [0.0 , 0.5],
            'detente':  [0.0, 0.0]
        }

        # Creating the publisher with data type Twist (instead String)
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1) # cmd_vel is the topic
        
        # Creating the publisher
        rospy.Subscriber('/recognizer/output', String, callback=self.get_mov) # Subscribes to the /recognizer/output topic


        rate = rospy.Rate(10) # 10 Hz

        # Below you write what you want to be published
        while not rospy.is_shutdown(): # While not pressing ctrl + c
            self.pub.publish(self.mov_msg)
            print(self.mov_msg) # Shown on the console
            rate.sleep()  

    # Function that stops the movement of the robot
    def stop(self):
        stop = 0.0
        # linear
        self.mov_msg.linear.x = stop
        # angular
        self.mov_msg.angular.z = stop
        

    # Function that moves the robot
    def get_mov(self, mov): # The topic passes the value 'mov'
        key_txt = mov.data.lower() # The text is retrieved: avanza, gira or detente (if there is one)
        if key_txt in self.mov_dic:
            get_key = self.mov_dic[key_txt]
            self.mov_msg.linear.x = get_key[0]
            self.mov_msg.angular.z = get_key[1]

            print('Command executed successfully')
        else:
            self.stop()
            print('Command not recognized.')
            print('The recognized commands are the following three: avanza, gira y detente')

    # Function that runs when the program stops
    def get_stop(self):
        self.stop()
        msg = self.mov_msg
        rospy.loginfo(msg)
        self.pub.publish(msg)
        

# Function that initializes the node
def init_node():
    rospy.init_node('action_pub', anonymous=True)
    print('Node created successfully!')

if __name__ == '__main__':
    init_node()
    try:
        MoveRobot() 
    except rospy.ROSInterruptException:
        pass
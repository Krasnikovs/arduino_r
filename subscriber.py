#!/usr/bin/env python
import serial
import rospy
from std_msgs.msg import String
 
board = serial.Serial('/dev/ttyACM0')

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    board.write(data.data.encode())
    rospy.loginfo(board.readline())


def listener():
    rospy.init_node('listener', anonymous=True)
 
    rospy.Subscriber("chatter", String, callback)
 
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()
 
if __name__ == '__main__':
    listener()

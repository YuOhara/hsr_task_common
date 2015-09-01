#!/usr/bin/env python
import rospy
import sys
from std_msgs.msg import String
rospy.init_node("message_publisher", anonymous=True)
string_pub = rospy.Publisher("~output", String)

str = "msg:\n"
while not rospy.is_shutdown():
    print str,
    str = sys.stdin.readline()
    string_pub.publish(String(data=str))

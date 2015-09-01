#!/usr/bin/env python
import rospy
import commands
from std_msgs.msg import *

class ScriptInterface():
    def __init__(self):
        rospy.init_node('script_interface', anonymous=True)
        rate = rospy.get_param('~rate', 10)
        r = rospy.Rate(rate)
        rospy.Subscriber('/command1', Empty, self.command1_cb)
    def command1_cb(self, msg):
        check = commands.getoutput("rosrun hsr_task_common get_sound.sh")
        print check


if __name__ == '__main__':
    try:
        s_i = ScriptInterface()
        rospy.spin()
    except rospy.ROSInterruptException: pass

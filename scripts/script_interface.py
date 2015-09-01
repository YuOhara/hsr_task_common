#!/usr/bin/env python
import rospy
import commands
from std_msgs.msg import Empty as Empty_msg
from std_srvs.srv import *
class ScriptInterface():
    def __init__(self):
        rospy.init_node('script_interface', anonymous=True)
        rate = rospy.get_param('~rate', 10)
        r = rospy.Rate(rate)
        rospy.Subscriber('/command1', Empty_msg, self.command1_cb)
        rospy.Service('/play', Empty, self.play_cb)
    def command1_cb(self, msg):
        check = commands.getoutput("rosrun hsr_task_common get_sound.sh")
        print check
    def play_cb(self, req):
        check = commands.getoutput("rosrun hsr_task_common play_sound.sh")
        return EmptyResponse()

if __name__ == '__main__':
    try:
        s_i = ScriptInterface()
        rospy.spin()
    except rospy.ROSInterruptException: pass

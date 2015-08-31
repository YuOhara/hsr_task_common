#!/usr/bin/env python
import rospy

from sensor_msgs.msg import Image
from hsr_task_common.msg import UiOut
from dynamic_reconfigure.server import Server
from hsr_task_common.cfg import AdditionalRqtConfig

class UiOutPublisher():
    def __init__(self):
        rospy.init_node('dynamixel_joint_state_publisher', anonymous=True)
        self.srv = Server(AdditionalRqtConfig, self.reconfigure_callback)
        rate = rospy.get_param('~rate', 10)
        r = rospy.Rate(rate)
        self.ui_out_pub = rospy.Publisher("/ui_out", UiOut)
        self.call_msg = ""
        self.message = ""
        self.photo_msg = None
    def reconfigure_callback(self, config, level):
        self.call_msg = config.call_msg
        self.message = config.message
        rospy.loginfo(self.call_msg)
        return config





if __name__ == '__main__':
    try:
        u_p = UiOutPublisher()
        rospy.spin()
    except rospy.ROSInterruptException: pass


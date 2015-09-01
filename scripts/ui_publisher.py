#!/usr/bin/env python
import rospy

from sensor_msgs.msg import Image
from hsr_task_common.msg import UiOut, SimpleTime
from dynamic_reconfigure.server import Server
from hsr_task_common.cfg import AdditionalRqtConfig
from std_srvs.srv import *

class UiOutPublisher():
    def __init__(self):
        rospy.init_node('dynamixel_joint_state_publisher', anonymous=True)
        self.srv = Server(AdditionalRqtConfig, self.reconfigure_callback)
        rate = rospy.get_param('~rate', 10)
        r = rospy.Rate(rate)
        self.ui_out_pub = rospy.Publisher("/ui_out", UiOut)
        self.task = 0
        self.hours = 0
        self.minutes = 0
        self.call_msg = ""
        self.message = ""
        self.photo_msg = None
        rospy.Service('/send', Empty, self.send_cb)
        rospy.Subscriber('/image_raw', Image, self.image_cb)
        rospy.Service('/message', Empty, self.send_cb)
        rospy.Service('/eat', Empty, self.eat_cb)
        rospy.Service('/study', Empty, self.study_cb)
        rospy.Service('/sleep', Empty, self.sleep_cb)   
    def reconfigure_callback(self, config, level):
        self.call_msg = config.call_msg
        self.message = config.message
        self.hours = config.hours
        self.minutes = config.minutes
        rospy.loginfo(self.call_msg)
        return config
    def image_cb(self, msg):
        self.photo_msg = msg
    def send_cb(self, req):
        st = SimpleTime()
        st.hours = self.hours
        st.minutes = self.minutes
        self.ui_out_pub.publish(UiOut(face=self.photo_msg, call_msg=self.call_msg, message=self.message, obj_id=self.task, time=st))
        return EmptyResponse()
    def message_cb(self, req):
        self.task = 0
        return EmptyResponse()
    def eat_cb(self, req):
        self.task = 1
        return EmptyResponse()
    def study_cb(self, req):
        self.task = 2
        return EmptyResponse()
    def sleep_cb(self, req):
        self.task = 3
        return EmptyResponse()
    




if __name__ == '__main__':
    try:
        u_p = UiOutPublisher()
        rospy.spin()
    except rospy.ROSInterruptException: pass


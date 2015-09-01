#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hsrb_interface
import rospy
from hsr_task_common.msg import UiOut
from sensor_msgs.msg import Image
from std_srvs.srv import *
from std_msgs.msg import Empty as Empty_msg
this_obj_id=2
robot = hsrb_interface.Robot()
pub_parent_face = rospy.Publisher("/parent_face", Image)
req_send_face_srv = rospy.ServiceProxy("/snapshot/request", Empty)
pub_sound_save = rospy.Publisher("/command1", Empty_msg)

def yuusyoku_demo(data):
    print "start yuusyokudemo"
    global this_obj_id, robot, pub_parent_face, req_send_face_srv, pub_sound_save
    #if data.obj_id != this_obj_id:
    # return
    # MANUPUlATION_YUUSYOKU
    manip(data.obj_id)
    tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)
    face_flag = False
    while (not face_flag):
        tts.say(data.call_msg)
        rospy.sleep(10)
        # calc face pos
        if (True):
            face_flag = True
    # face
    pub_parent_face.publish(data.face)
    tts.say(data.message)
    rospy.sleep(10)
    pub_sound_save.publish(Empty_msg()) ## save sound
    tts.say("写真をとるよー")
    rospy.sleep(5)
    tts.say("はいチーズ")
    rospy.sleep(4)
    tts.say("かしゃしゃっ！")
    # rospy.Subscriber("/") KAO_NINSHIKI
    req_send_face_srv()
    

def manip(obj):
    pass
    

def execute_task_sub():
    rospy.Subscriber("/execute_task", UiOut, yuusyoku_demo)
    rospy.spin()

    
if __name__ == "__main__":
    execute_task_sub()

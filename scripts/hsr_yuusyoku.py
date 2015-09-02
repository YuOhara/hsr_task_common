#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hsrb_interface
import rospy
import math
from hsrb_interface from geometry
from hsr_task_common.msg import UiOut
from sensor_msgs.msg import Image
from std_srvs.srv import *
from std_msgs.msg import Empty as Empty_msg

this_obj_id=2
robot = hsrb_interface.Robot()
pub_parent_face = rospy.Publisher("/parent_face", Image)
req_send_face_srv = rospy.ServiceProxy("/snapshot/request", Empty)
pub_sound_save = rospy.Publisher("/command1", Empty_msg)

robot = hsrb_interface.Robot()
omni_base = robot.get('omni_base')
whole_body = robot.get('whole_body')
gripper = robot.get('gripper')

def yuusyoku_demo(data):
    print "start yuusyokudemo"
    global this_obj_id, robot, pub_parent_face, req_send_face_srv, pub_sound_save
    #if data.obj_id != this_obj_id:
    # return
    # MANUPUlATION_YUUSYOKU
    manip(data.obj_id)
    rospy.loginfo("make robot tts")
    tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)
    face_flag = False
    while (not face_flag):
        rospy.loginfo("call")
        tts.say(data.call_msg)
        rospy.sleep(10)
        # calc face pos
        if (True):
            face_flag = True
    # face
    rospy.loginfo("face")
    pub_parent_face.publish(data.face)
    tts.say(data.message)
    rospy.sleep(10)
    pub_sound_save.publish(Empty_msg()) ## save sound
    tts.say("写真をとるよー")
    rospy.sleep(5)
    tts.say("はい,笑顔")
    rospy.sleep(4)
    tts.say("かしゃしゃっ！")
    # rospy.Subscriber("/") KAO_NINSHIKI
    req_send_face_srv()

def manip(obj):
    # go to kitchen
    whole_body.move_to_go()
    omni_base.go(5.90, 0.0, -1.57, 60, relative=False)

    # IK and grasp
    whole_body.move_end_effector_pose(geometry.pose(ei=-1.10, y=-0.10, z=-0.05), 'recognized_object/4')
    whole_body.move_end_effector_pose(geometry.pose(z=0.05), 'hand_palm_link')
    gripper.grasp(-0.10) # -0.01 is too weak

    # go to table
    whole_body.move_end_effector_pose(geometry.pose(z=-0.1), 'hand_palm_link')
    omni_base.go(5.90, 4.4, -3.14, 60, relative=False)
    omni_base.go(5.25, 4.4, -3.14, 60, relative=False) # approach to table

    # IK and release
    whole_body.move_end_effector_pose(geometry.pose(z=0.090), 'hand_palm_link')
    gripper.command(1.25)
    whole_body.move_end_effector_pose(geometry.pose(z=-0.20), 'hand_palm_link') # move arm far from table
    whole_bode.move_to_go()
    # pass

def execute_task_sub():
    rospy.Subscriber("/execute_task", UiOut, yuusyoku_demo)
    rospy.spin()

if __name__ == "__main__":
    execute_task_sub()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hsrb_interface
import rospy
import math
from hsrb_interface import geometry
from hsr_task_common.msg import UiOut
from sensor_msgs.msg import Image
from std_srvs.srv import *
from std_msgs.msg import Empty as Empty_msg
from std_msgs.msg import UInt8
this_obj_id=2
robot = hsrb_interface.Robot()
tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)
print "before_init_yuushoku"
print "before_init_pub"
pub_parent_face = rospy.Publisher("/parent_face", Image)
req_send_face_srv = rospy.ServiceProxy("/snapshot/request", Empty)
pub_sound_save = rospy.Publisher("/command1", Empty_msg)

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
    photo()
    # rospy.Subscriber("/") KAO_NINSHIKI
    req_send_face_srv()

def say():
    global tts, pub_sound_save
    tts.say("Taro, Gohan-yo")
    rospy.sleep(10)
    rospy.loginfo("face")
    # pub_parent_face.publish(data.face)
    tts.say("Yasai mo nokosazu tabete ne!")
    rospy.sleep(10)
    pub_sound_save.publish(Empty_msg()) ## save sound

def photo():
    global tts, req_send_face_srv
    tts.say("写真をとるよー")
    rospy.sleep(5)
    tts.say("はい,笑顔")
    rospy.sleep(4)
    tts.say("かしゃしゃっ！")

def manip_e(obj):
    for i in [1, 2, 3]:
        try:
            whole_body.move_end_effector_pose(geometry.pose(ei=-1.10, y=-0.10, z=-0.05), 'recognized_object/4')
            break
        except:
            rospy.sleep(5)
            tts.say("うんち")
            rospy.loginfo("manip mistate no tf")
            rospy.sleep(5)
            omni_base.go(0.10, 0, 0, 10, relative=True)

def manip(obj):
    # go to kitchen
    whole_body.move_to_go()
    omni_base.go(5.90, 2.0, -3.14, 120, relative=False)
    rospy.sleep(5)

    # for i in [1, 2, 3]:
    #     try:
    #         whole_body.move_end_effector_pose(geometry.pose(ei=-1.10, y=-0.10, z=-0.05), 'recognized_object/4')
    #         break
    #     except:
    #         rospy.sleep(3)
    #         tts.say("うんち")
    #         rospy.loginfo("manip mistate no tf")
    #         rospy.sleep(3)
    #         omni_base.go(0.10, 0, 0, 10, relative=True)

    whole_body.move_end_effector_pose(geometry.pose(ei=-1.10, y=-0.10, z=-0.05), 'recognized_object/4')
    whole_body.move_end_effector_pose(geometry.pose(z=0.05), 'hand_palm_link')
    gripper.grasp(-0.10) # -0.01 is too weak

    # go to table
    whole_body.move_end_effector_pose(geometry.pose(z=-0.1), 'hand_palm_link')
    omni_base.go(5.90, 4.25, -3.14, 120, relative=False)
    omni_base.go(5.25, 4.25, -3.14, 120, relative=False) # approach to table
    # omni_base.go(5.90, 4.4, -3.14, 120, relative=False)
    # omni_base.go(5.25, 4.4, -3.14, 120, relative=False) # approach to table

    # IK and release
    whole_body.move_end_effector_pose(geometry.pose(z=0.090), 'hand_palm_link')
    gripper.command(1.25)
    whole_body.move_end_effector_pose(geometry.pose(z=-0.20), 'hand_palm_link') # move arm far from table
    whole_body.move_to_go()
    # pass

def manip_a():
    whole_body.move_to_go()
    omni_base.go(5.90, 2.0, -3.14, 120, relative=False)

def manip_b():
    # IK and grasp
    whole_body.move_end_effector_pose(geometry.pose(ei=-1.10, y=-0.10, z=-0.05), 'recognized_object/4')
    whole_body.move_end_effector_pose(geometry.pose(z=0.05), 'hand_palm_link')
    gripper.grasp(-0.10) # -0.01 is too weak
def manip_c():
    # go to table
    whole_body.move_end_effector_pose(geometry.pose(z=-0.1), 'hand_palm_link')
    omni_base.go(5.90, 4.4, -3.14, 120, relative=False)
    omni_base.go(5.25, 4.4, -3.14, 120, relative=False) # approach to table

def manip_d():
    # IK and release
    whole_body.move_end_effector_pose(geometry.pose(z=0.090), 'hand_palm_link')
    gripper.command(1.25)
    whole_body.move_end_effector_pose(geometry.pose(z=-0.20), 'hand_palm_link')    # move arm far from table
    whole_body.move_to_go()
def do_task(msg):
    hoge = msg.data
    if hoge==0:
        manip_a()
    elif hoge==1:
        manip_b()
    elif hoge==2:
        manip_c()
    elif hoge==3:
        manip_d()
    elif hoge==4:
        say()
    else:
        photo()

def execute_task_sub():
    rospy.Subscriber("/execute_task", UiOut, yuusyoku_demo)
    rospy.Subscriber("/task_command", UInt8, do_task)
    rospy.loginfo("main")
    rospy.spin()

if __name__ == "__main__":
    execute_task_sub()

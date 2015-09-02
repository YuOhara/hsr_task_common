#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hsrb_interface
import rospy

robot = hsrb_interface.Robot()

def kitaku_demo():
    print "start kitaku_demo"
    global robot

    tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)
    whole_body = robot.try_get('whole_body')
    
    try:
        whole_body.move_to_go()
    except:
        rospy.logerr('Fail move_to_neutral')

    tts.say("ご飯ですよ")
    rospy.sleep(3)

    face_flag = False
    # while (not face_flag):
    #     rospy.sleep(1)
    #     if (True):
    #         face_flag = True

    whole_body.move_to_joint_positions({'head_tilt_joint' : 0.2})

    tts.say("おいしかった？")
    rospy.sleep(3)
    tts.say("お母さんに伝えておくね")

    
if __name__ == "__main__":
    kitaku_demo()

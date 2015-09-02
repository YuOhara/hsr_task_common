#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hsrb_interface
import rospy

robot = hsrb_interface.Robot()

def kitaku_demo():
    print "start kitaku_demo"
    global robot

    tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)
    base = robot.try_get('omni_base')
    whole_body = robot.try_get('whole_body')
    
    try:
        whole_body.move_to_go()
    except:
        rospy.logerr('Fail move_to_neutral')

    tts.say("15時は帰宅の時間です")
    rospy.sleep(5)

    base.go(0.0, 0.0, 0.5, 10.0, relative=True)
    
    face_flag = False
    # while (not face_flag):
    #     rospy.sleep(1)
    #     if (True):
    #         face_flag = True

    tts.say("おかえりなさい")
    rospy.sleep(3)
    tts.say("写真を撮ってお母さんに送るね")
    rospy.sleep(4)
    tts.say("はいチーズ")
    rospy.sleep(2)
    tts.say("カシャ")

    
if __name__ == "__main__":
    kitaku_demo()

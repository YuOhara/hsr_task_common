#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hsrb_interface
import rospy

robot = hsrb_interface.Robot()

def kitaku_demo():
    print "start kitaku_demo"
    global robot

    tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)

    tts.say("21時は帰宅の時間です")
    rospy.sleep(5)

    face_flag = False
    # while (not face_flag):
    #     rospy.sleep(1)
    #     if (True):
    #         face_flag = True

    tts.say("寝る時間だよ")
    rospy.sleep(7)
    tts.say("寝る時間だよ")
    rospy.sleep(7)
    tts.say("ちゃんと寝ないからお母さんに言っておくね")

    
if __name__ == "__main__":
    kitaku_demo()

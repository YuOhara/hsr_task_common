#!/usr/bin/env python

import rospy
from hsr_task_common.msg import UiOut, SimpleTime

tasks=[]
rospy.init_node("schedule_sub", anonymous=True)
pub = rospy.Publisher("/execute_task", UiOut)

def schedule_sub_cb(data):
    global tasks
    tasks.append(data)
    print "received schedule! obj_id="+str(data.obj_id)+", time="+str(data.time.hours)+":"+str(data.time.minutes)

def time_sub_cb(data):
    rospy.loginfo("time rechieved")
    global tasks, pub
    rospy.loginfo("time rechieved")
    for task in tasks:
        if task.time.minutes == data.minutes and task.time.hours == data.hours:
            pub.publish(task)
            tasks.remove(task)
            print "published execute_task!"

def schedule_sub():
    rospy.Subscriber("/ui_out", UiOut, schedule_sub_cb)
    rospy.Subscriber("/time_input", SimpleTime, time_sub_cb)
    rospy.spin()

if __name__ == "__main__":
    schedule_sub()

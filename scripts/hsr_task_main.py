#!/usr/bin/env python

import rospy
from hsr_task_common.msg import UiOut, SimpleTime

tasks=[]

def schedule_sub_cb(data):
    print "schedule_sub_cb"
    tasks.append(data)

def time_sub_cb(data):
    global tasks
    print "time_sub_cb"
    ##tasks.append(data)
    for task in tasks:
        if task.time.minutes == data.minutes and task.time.hours == data.hours:
            tasks.remove(task)
            print "Event !!"
            ##pass
            ##Send Event Message
        

def schedule_sub():
    print "schedule_sub"
    rospy.init_node("schedule_listener", anonymous=True)
    rospy.Subscriber("/ui_out", UiOut, schedule_sub_cb)
    rospy.Subscriber("/time_input", SimpleTime, time_sub_cb)
    rospy.spin()
        

    
if __name__ == "__main__":
    schedule_sub()

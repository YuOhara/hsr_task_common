import hsrb_interface
import rospy
import sys
from hsrb_interface import geometry

# move timeout
_MOVE_TIMEOUT=60.0
# grasp torque
_GRASP_TORQUE=-0.01

_OBJECT_TF_1='recognized_object/1'
_OBJECT_TF_2='recognized_object/2'
_OBJECT_TF_3='recognized_object/3'

_HAND_TF='hand_palm_link'

def robot_init:
    robot = hsrb_interface.Robot()
    omni_base = robot.get('omni_base')
    whole_body = robot.get('whole_body')
    gripper = robot.get('gripper')
    tts = robot.get('default', robot.Items.TEXT_TO_SPEECH)
    manip_pos = (5.40, 4.30, 0.0)


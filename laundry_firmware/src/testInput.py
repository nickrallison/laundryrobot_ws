#!/usr/bin/env python3


import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

def controller():
    pub = rospy.Publisher('actuation/motor', Float32, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(0.1) # 0.1Hz
    while not rospy.is_shutdown():
        rpm = rospy.get_time() % 3000
        rospy.loginfo(rpm)
        pub.publish(rpm)
        rate.sleep()

if __name__ == '__main__':
    try:
        controller()
    except rospy.ROSInterruptException:
        pass

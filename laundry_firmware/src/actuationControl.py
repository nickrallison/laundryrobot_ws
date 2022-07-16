#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32

import RPi.GPIO as GPIO
from time import sleep


PWNPin = 10
rpm = -1
frequency = 1000

GPIO.setmode(GPIO.BOARD)
GPIO.setup(port_or_pin, GPIO.OUT)
pi_pwm = GPIO.PWM(PWMPin, frequency)
pi_pwm.start(0)

def rpmCB(data):
    pi_pwm.ChangeDutyCycle(data.data)
    print(data.data)

def main():
    rospy.init_node('pwmactuation', anonymous=True)
    rospy.Subscriber('/actuation/motor', Float32, rpmCB)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass


#!/usr/bin/env python
from cmath import pi
import termios, sys, os

from matplotlib.pyplot import get
import rospy
from turtlesim.srv import TeleportAbsolute, TeleportRelative
from geometry_msgs.msg import Twist 

TERMIOS = termios

def getkey():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~TERMIOS.ICANON & ~TERMIOS.ECHO
    new[6][TERMIOS.VMIN] = 1
    new[6][TERMIOS.VTIME] = 0
    termios.tcsetattr(fd, TERMIOS.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, TERMIOS.TCSAFLUSH, old)
    return c.decode("utf-8")

def teleport_abs(x, y, ang):
    rospy.wait_for_service('/turtle1/teleport_absolute')
    try:
        teleportA = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        resp1 = teleportA(x, y, ang)
        print('Teleported to x: {}, y: {}, ang: {}'.format(str(x),str(y),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

def teleport_rel(x, ang):
    rospy.wait_for_service('/turtle1/teleport_relative')
    try:
        teleportR = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
        resp1 = teleportR(x, ang)
        print('Teleported to x: {}, ang: {}'.format(str(x),str(ang)))
    except rospy.ServiceException as e:
        print(str(e))

def pubPose():
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('posePub', anonymous=False)
    vel = Twist()
    vel.linear.x = 0
    vel.linear.y = 0
    vel.angular.z = 0
    rate = rospy.Rate(20)
    pressedKey = "o" 
    while pressedKey!="x":
        pressedKey=getkey()
        if pressedKey == "a":
            vel.linear.x = 0
            vel.linear.y = 0
            vel.angular.z = pi/6
            pub.publish(vel)
        if pressedKey == "w":
            vel.linear.x = 1
            vel.linear.y = 0
            vel.angular.z = 0
            pub.publish(vel)
        if pressedKey == "s":
            vel.linear.x = -1
            vel.linear.y = 0
            vel.angular.z = 0
            pub.publish(vel)
        if pressedKey == "d":
            vel.linear.x = 0
            vel.linear.y = 0
            vel.angular.z = -pi/6
            pub.publish(vel)
        if pressedKey == " ":
            teleport_rel(0,pi);
        if pressedKey == "r":
            teleport_abs(5.5,5.5,0);
        rospy.loginfo(vel)
        rate.sleep()

if __name__ == '__main__':
    try:
        pubPose()
        #print("this is "+getkey())
    except rospy.ROSInterruptException:
        pass
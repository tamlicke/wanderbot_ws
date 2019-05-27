#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

# only buffer a single outboaund message. In case the node sending
# messages is transmitting at a higher rate then the receiving node(s)
# can receive them, rospy will simply drop any messages beyond the 
# queue_size.
cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
rospy.init_node('red_light_green_light')

# create an instance of a Twist object with all fields all zero
red_light_twist = Twist()
green_light_twist = Twist()

# by convention x should be aligned with the direction the robot is facing.
green_light_twist.linear.x = 0.5 # meters per second

driving_forward = False
light_change_time = rospy.Time.now()
print light_change_time
rate = rospy.Rate(10)

while not rospy.is_shutdown():
	if driving_forward:
		cmd_vel_pub.publish(green_light_twist)
		print "green"
	else:
		cmd_vel_pub.publish(red_light_twist)
		print "red"

	print light_change_time
	print rospy.Time.now()
	if light_change_time < rospy.Time.now():
		driving_forward = not driving_forward
		light_change_time = rospy.Time.now() + rospy.Duration(3)

	rate.sleep()	

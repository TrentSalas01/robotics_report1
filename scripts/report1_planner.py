#!/usr/bin/env python3

import rospy
import math

# import the plan message
from ur5e_control.msg import Plan
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    # initialize the node
    rospy.init_node('simple_planner', anonymous = True)
    # add a publisher for sending joint position commands
    plan_pub = rospy.Publisher('/plan', Plan, queue_size = 10)
    # set a 10Hz frequency for this loop
    loop_rate = rospy.Rate(10)
    # define a plan variable
    plan = Plan()
    
    #Motion 1: Starting place
    plan_point1 = Twist()
    plan_point1.linear.x = -0.53
    plan_point1.linear.y = -0.13
    plan_point1.linear.z = 0.37
    plan_point1.angular.x = -2.98
    plan_point1.angular.y = -0.03
    plan_point1.angular.z = 1.95
    # add point 1 to the plan
    plan.points.append(plan_point1)
    
    #Motion 2: "Pick Up" Object
    plan_point2 = Twist()
    plan_point2.linear.x = -0.53
    plan_point2.linear.y = -0.13
    plan_point2.linear.z = 0.03
    plan_point2.angular.x = -2.98
    plan_point2.angular.y = -0.13
    plan_point2.angular.z = 1.93
    # add point 2 to the plan
    plan.points.append(plan_point2)

    #Motion 3: Move Object Further
    plan_point3 = Twist()
    plan_point3.linear.x = -0.73
    plan_point3.linear.y = -0.13
    plan_point3.linear.z = 0.35
    plan_point3.angular.x = -3.1
    plan_point3.angular.y = -0.12
    plan_point3.angular.z = 1.93
    # add point 3 to the plan
    plan.points.append(plan_point3)

    #Motion 4: Lowering Object
    plan_point4 = Twist()
    plan_point4.linear.x = -0.87
    plan_point4.linear.y = -0.13
    plan_point4.linear.z = 0.1
    plan_point4.angular.x = -2.88
    plan_point4.angular.y = -0.00
    plan_point4.angular.z = 1.92
    # add tpoint 4 to the plan
    plan.points.append(plan_point4)

    while not rospy.is_shutdown():
        # publish the plan
        plan_pub.publish(plan)
        # wait for 0.1 seconds until the next loop and repeat
        loop_rate.sleep()

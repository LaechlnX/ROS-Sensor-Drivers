from __future__ import print_function
import sys
import rospy
from tsl2591_array.srv import *

def add_two_ints_client(status):
    rospy.wait_for_service('add_two_ints')
    try:
        light_sensor = rospy.ServiceProxy('add_two_ints', readings)
        resp1 = light_sensor(status)
        return resp1.r1, resp1.r2, resp1.r3, resp1.r4
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting %s+%s"%(x, y))
    print("%s + %s = %s"%(x, y, add_two_ints_client(x, y)))
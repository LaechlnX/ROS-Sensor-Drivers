from __future__ import print_function
import sys
import rospy
from tsl2591_array.srv import *

def tsl2591_driver_client(status):
    rospy.wait_for_service('add_two_ints')
    try:
        light_sensor = rospy.ServiceProxy('add_two_ints', readings)
        resp1 = light_sensor(status)
        return resp1.reading1, resp1.reading2, resp1.reading3, resp1.reading4
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [status]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 2:
        status = int(sys.argv[1])
    else:
        print(usage())
        sys.exit(1)
    print("Requesting status:%s"%(status))
    r1,r2,r3,r4 = tsl2591_driver_client(status)
    print("Status: %d\nr1: %d\nr2: %d\nr3: %d\nr4: %d\n"%(status, r1,r2,r3,r4))
    print("---------------------------------------------")
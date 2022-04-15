from __future__ import print_function

from tsl2591_array.srv import readings, readingsResponse
import rospy

def dummy_load1():
    return 300.12345
def dummy_load2():
    return 400.12345

def handle_tsl2591_driver(req):
    if req.start == 1:
        r1 = dummy_load1()
        r2 = dummy_load2()
        r3 = r1
        r4 = r2
        print("Status: %s, return lux reading:\n1: %f\n2: %f\n3: %f\n4: %f]"%(req.start, r1, r2,r3,r4))
        print("---------------------------------------------")
    return readingsResponse(r1,r2,r3,r4)

def tsl2591_driver_server():
    rospy.init_node('tsl2591_driver')
    s = rospy.Service('add_two_ints', readings, handle_tsl2591_driver)
    print("Ready to send readings.")
    rospy.spin()

if __name__ == "__main__":
    tsl2591_driver_server()
from __future__ import print_function

from tsl2591_array.srv import readings, readingsResponse
import rospy

def dummy_load1():
    return 300.12345
def dummy_load2():
    return 400.12345

def handle_add_two_ints(req):
    if req.start == 1:
        
    print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
    return readingsResponse(req.a + req.b)

def add_two_ints_server():
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add_two_ints)
    print("Ready to add two ints.")
    rospy.spin()

if __name__ == "__main__":
    add_two_ints_server()
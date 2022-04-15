from __future__ import print_function

from tsl2591_array.srv import readings, readingsResponse
import rospy

import board
import adafruit_tca9548a
import adafruit_tsl2591
# -------------- Dummy load functions for test only-------#
def dummy_load1():
    return 300.12345
def dummy_load2():
    return 400.12345
#-------------------------End of Dummy Loads--------------#
# Sensor manipulation functions
def sensors_init():
    i2c = board.I2C()
    mp_bus = adafruit_tca9548a.TCA9548A(i2c)
    ls1 = adafruit_tsl2591.TSL2591(mp_bus[0])
    ls2 = adafruit_tsl2591.TSL2591(mp_bus[1])
    ls3 = adafruit_tsl2591.TSL2591(mp_bus[2])
    ls4 = adafruit_tsl2591.TSL2591(mp_bus[3])
    return ls1, ls2, ls3, ls4

def detect_lux(ls1, ls2, ls3, ls4):
    return ls1.lux, ls2.lux, ls3.lux, ls4.lux

# ROS server initialization and sending readings
def handle_tsl2591_driver(req):
    if req.start == 1:
        ls1,ls2,ls3,ls4 = sensors_init()
        r1,r2,r3,r4 = detect_lux(ls1,ls2,ls3,ls4)
        print("Status: %s, return lux reading:\n1: %f\n2: %f\n3: %f\n4: %f"%(req.start, r1, r2,r3,r4))
        print("---------------------------------------------")
    return readingsResponse(r1,r2,r3,r4)

def tsl2591_driver_server():
    rospy.init_node('tsl2591_driver')
    s = rospy.Service('add_two_ints', readings, handle_tsl2591_driver)
    print("Ready to send readings.")
    rospy.spin()

if __name__ == "__main__":
    tsl2591_driver_server()
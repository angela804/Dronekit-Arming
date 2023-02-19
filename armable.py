from dronekit import connect, VehicleMode, LocationGlobalRelative
from pymavlink import mavutil
import time


vehicle = None

vehicle = connect('/dev/ttyS0', baud=57600, wait_ready=True)
#vehicle.armed = True #can't arm without Guided mode
print('Vehicle is ready and armed.')


def arm_and_take(aTargetAltitude):
    
    print('Basic pre-arm checks')
    #Don't let the user try to arm until autopilot is ready
    while not vehicle.is_armable:
        print("Waiting for vehicle ot initialise")
        time.sleep(1)
        
    
    print("Arming motors")
    #Copter should arm in GUIDED mode
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True
    
    #while not vehicle.armed:
     #   print("Waiting for arming...")
     #   vehicle.armed = True
     #   time.sleep(1)
        
        
    
arm_and_take(5)

#Hover for 10 seconds
time.sleep(15)

print("Now let's land")
vehicle.mode = VehicleMode("LAND")

#Close vehicle object
vehicle.close()
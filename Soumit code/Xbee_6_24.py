import serial
import time
import threading


global Xbee #xbee
Xbee = serial.Serial('/dev/ttyUSB0', 115200)


#Body
angle = 0
cycle_time = 10 #length of osc duration
time_base = time.time()
initial_heading  = float(input("Initial angle?" ));


while True:
	try:
                                             #While the heading of the roomba is <360 degrees, rotate the roomba by 2.5 degrees per second
                    angle = initial_heading + ((time.time() - time_base) * 360/cycle_time)

                if (angle => 360):       #When angle =360, send out a pulse 
			broadcast = '1'
			Xbee.write(broadcast.encode())
			print("output")
			time_base = time.time()


			def printit():          #print out the angle every 5 seconds
                          threading.Timer(5.0, printit).start()
                          print ("{0:.3f}".format(angle))

                        printit()

			
		if Xbee.inWaiting() > 0: # when recieve message, decrease the initial_heading by 25% of the difference 
			message = Xbee.read(Xbee.inWaiting()).decode()
                        initial_heading = initial_heading - ((360 - angle)*0.25)


                        
                        
                        
		

import serial
import time
import threading


global Xbee #xbee
Xbee = serial.Serial('/dev/ttyUSB0', 115200)

angle = 0

def printit():          #print out the angle every 5 seconds
        threading.Timer(5.0, printit).start()
        print ("{0:.3f}".format(angle))

#Body
cycle_time = 10 #length of osc duration
time_base = time.time()
initial_heading  = float(input("Initial angle?" ));


while True:
	try:
                except KeyboardInterrupt: break
                
                                        
                angle = initial_heading + ((time.time() - time_base) * 360/cycle_time)      #While the heading of the roomba is <360 degrees, rotate the roomba by 2.5 degrees per second

 
                if (angle >= 360):
                    broadcast = '1'
                    Xbee.write(broadcast.encode())
                    print("output")
                    time_base = time.time()
                    printit()


		

                       

			
                if Xbee.inWaiting() > 0:
                    message = Xbee.read(Xbee.inWaiting()).decode()
                    initial_heading = initial_heading - ((360 - angle)*0.25)


                if (initial_heading <= 0):
                    initial_heading = 360 - initial_heading

        

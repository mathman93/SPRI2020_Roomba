import serial
import time


global Xbee #xbee
Xbee = serial.Serial('/dev/ttyUSB0', 115200)


#Body
angle = 0
pulse = 0

while True:
	try:
                while(angle < 360):
                    def add():
                    angle =+ 2.5 

                    t = Timer(1, add)
                    t.start()
                    

                if (angle = 360):
                    angle = 0
                    pulse = 1
                

                    
		if (pulse = 1):
			broadcast = '1'
			Xbee.write(broadcast.encode())
			pulse = 0
			

			
		if Xbee.inWaiting() > 0: 
			message = Xbee.read(Xbee.inWaiting()).decode()
                        angle= angle - ((360 - angle)*0.25)

                        
                        
		

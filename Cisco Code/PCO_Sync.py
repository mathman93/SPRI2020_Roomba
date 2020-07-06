

global Xbee

import time
import serial

Xbee = serial.Serial('/dev/ttyUSB0', 115200)


syncLimit = 360 #Degree Limit of oscillator
cycleTime = 10 #Length (in seconds) of oscillator cycle
frequency = syncLimit/cycleTime #Cycle Rate (in degrees per second)
time_base = time.time()
currentPhase = 0 #Initialises Angle

while True:
    try:
        currentPhase = (time.time() - time_base) * frequency
        timeDiff = (time.time() - time_base)
        
        if currentPhase >= syncLimit:
            message = '1'  # Encoded message for the Xbee to send
            Xbee.write(message.encode())  # Encodes the message
            print("You sent a pulse")
            print(currentPhase)

            time_base += cycleTime #Increases thes




        if Xbee.inWaiting() > 0: #If the Xbee receives a message
            message = Xbee.read(Xbee.inWaiting()).decode() #Decodes and reads the data

            #Find difference between time of receiving pulse vs. time of next threshold
            #timeDiff = (time.time() - time_base)-cycleTime

            #currentPhase = currentPhase-(timeDiff*frequency*0.5) #Shifts phase forward by half of the difference.
            time_base += timeDiff*0.5

    except KeyboardInterrupt:
        print('Connection Terminated')
        break

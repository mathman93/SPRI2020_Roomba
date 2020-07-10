

global Xbee

import time
import serial

Xbee = serial.Serial('/dev/ttyUSB0', 115200)


syncLimit = 360 #Degree Limit of oscillator
cycleTime = 10 #Length (in seconds) of oscillator cycle
frequency = syncLimit/cycleTime #Cycle Rate (in degrees per second)
time_base = time.time()
heading = float(input("Please enter robot heading: "));


while True:
    try:
        timeDiff = (time.time() - time_base)
        
        currentPhase = heading + timeDiff * frequency
        
        if currentPhase >= syncLimit:
            message = '1'  # Encoded message for the Xbee to send
            Xbee.write(message.encode())  # Encodes the message
            print("You sent a pulse")
            print(currentPhase)

            time_base += cycleTime #Increases threshold




        if Xbee.inWaiting() > 0: #If the Xbee receives a message
            message = Xbee.read(Xbee.inWaiting()).decode() #Decodes and reads the data

            #Find difference between time of receiving pulse vs. time of next threshold
            #timeDiff = (time.time() - time_base)-cycleTime

            #currentPhase = currentPhase-(timeDiff*frequency*0.5) #Shifts phase forward by half of the difference.
            #time_base += timeDiff*0.5  
            if timeDiff >= cycleTime/2:
                heading =+ timeDiff*0.5*frequency
            elif timeDiff < cycleTime/2:
                heading =- timeDiff*0.5*frequency

    except KeyboardInterrupt:
        print('Connection Terminated')
        break

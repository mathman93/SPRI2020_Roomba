
import math
import time
import serial
import os.path

file_name_input=input("Name for date file: ")
dir_path="/home/pi/SPRI2020_Roomba/Data_Files/"
file_name= os.path.join(dir_path,file_name_input+".txt")
file=open(file_name,"w")
angle = int(input("intitial robot angle"))

global Xbee  # Specifies connection to Xbee
Xbee = serial.Serial('/dev/ttyUSB0', 115200)  # Baud rate should be 115200


def DisplayDateTime():
    # Month day, Year, Hour:Minute:Seconds
    date_time = time.strftime("%B %d, %Y, %H:%M:%S", time.gmtime())
    print("Program run: ", date_time)

DisplayDateTime()

threshold = 360
cycletime = 10
freq = threshold / cycletime
time_base = time.time()
count_base = time.time()
count_baseoffset = 1
# phase = angle + timer

while True:
    try:
        phase = angle + ((time.time() - time_base) * freq)
        timer = time.time()-count_base
        if timer > count_baseoffset:
            count_base += 1
            print("{0:.3f}, {1:.3f}, {2:.3f}".format(count_base, phase, angle))
            #file.write("{0:.3f}, {1:.3f}, {2:.3f}\n".format(count_base, phase, angle))

        if phase >= threshold:
            message = '1'  # Change this to any character string you want
            Xbee.write(message.encode())  # Send the number over the Xbee
            print("you sent stuff")
            time_base += cycletime  # Increase offset for next time to send message

        if Xbee.inWaiting() > 0:  # If there is something in the receive buffer
            message = Xbee.read(Xbee.inWaiting()).decode()  # Read all data in
            print(message)  # To see what the message is
            if message == '1':
                print(phase)
                if phase<=threshold/2:
                    #new_base =((phase/2)-angle)/freq-time.time()
                    #time_base = time_base + (1/2*((phase)-angle)/freq)
                    angle=angle-1/2*(phase)

                if phase>threshold/2:
                    #new_base =((360+phase/2)-angle)/freq-time.time()
                    #time_base = time_base - (((360-phase)/2)-angle)/freq
                    angle=angle+(360-phase)/2
                if angle<0:
                    angle+=360
                    time_base-=cycletime
                if angle<360:
                    angle-=360
                    time_base+=cycletime
        

		
    except KeyboardInterrupt:
        print('')
        break

Xbee.close()
file.close()

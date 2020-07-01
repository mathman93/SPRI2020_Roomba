import math
import time
import serial

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
angle = int(input("intitial robot angle"))

# phase = angle + timer

while True:
    try:
        phase = angle + ((time.time() - time_base) * freq)

        if phase >= threshold:
            message = '1'  # Change this to any character string you want
            Xbee.write(message.encode())  # Send the number over the Xbee
            print("you sent stuff")
            time_base += cycletime  # Increase offset for next time to send message

        if Xbee.inWaiting() > 0:  # If there is something in the receive buffer
            message = Xbee.read(Xbee.inWaiting()).decode()  # Read all data in
            print(message)  # To see what the message is
            print(timer)
            if message == '1':
                time_base = time_base + (360 - phase / 2)
                # angle+= something#based on value of phase
                # angle=angle+ x


    except KeyboardInterrupt:
        print('')
        break

Xbee.close()

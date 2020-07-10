''' Test Code
This is a test comment explaining the code.
'''

import math
import serial
import time
import os.path
#import numpy as np
#import matplotlib.plt as plt

# Open a text file for data retrieval
file_name_input = input("Name for data file: ")
dir_path = "/home/pi/SPRI2020_Roomba/Data_Files/" # Directory path to save file on Raspberry Pi
file_name = os.path.join(dir_path, file_name_input+".txt") # text file extension
file = open(file_name, "w") # Open a text file for storing data
    # Will overwrite anything that was in the text file previously

while True:
    try:
        heading = float(input("Initial robot heading? "))
        break
    except ValueError:
        print("Error message")
        continue
# End while

threshold = 360 # oscillator threshold (degrees)
cycle_time = 12 # Length of oscillator cycle (seconds)
freq = threshold/cycle_time # degrees per second
current_time = time.time()
time_base = current_time - (current_time%cycle_time)
# This modification ensures consistency between Raspberry Pis
print_offset = 1.0
print_base = current_time - (current_time%print_offset)

#phase = heading + timer

while True:
    try:
        # Get current value of timer
        phase = heading + ((time.time() - time_base) * freq)
        
        if phase >= threshold:
            # Send "pulse"
            # Reset phase value to zero
            time_base += cycle_time
            #time_base += threshold/freq
        # End if
        
        # If Xbee has received a "pulse"
            # Read "pulse"
            # Respond to pulse and adjust phase
            heading += something # Based on value of phase
        # End if

        # Normalize the heading value
        if heading >= threshold:
            heading -= threshold
            time_base -= cycle_time
        elif heading < 0:
            heading += threshold
            time_base += cycle_time

        if (time.time() - print_base) > print_offset:
            print_base += print_offset;
            print("{0:.3f}, {1:.3f}, {2:.3f}".format(print_base, phase, heading))
            file.write("{0:.3f}, {1:.3f}, {2:.3f}\n".format(print_base, phase, heading))
            # Timestamp, phase value, heading value
            # Could also just use time.time() instead of print_base.

        # Control robot angle to follow heading
        #angle = angle + x # Sort of
        
    except KeyboardInterrupt:
        break # Exit while loop
# End while

file.close() # Close file after running



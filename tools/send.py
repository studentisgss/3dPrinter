#!/usr/bin/env python
import time
import serial

# Configure the serial connections.
# The parameters differs on the device you are connecting to.
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=250000,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

if not ser.isOpen():
    ser.open()
else:
    print "Serial connection is already open."

print "Enter your commands below."
print "Insert 'exit' to leave the application."

input = 1
while True:
    # Get keyboard input.
    input = raw_input(">> ")
    # Python 3 users
    # input = input(">> ")
    if input == 'exit':
        ser.close()
        exit()
    else:
        # Send the character to the device.
        # Note that I happend a \r\n carriage return and line feed to the
        # characters - this is requested by my device.
        ser.write(input + '\r\n')
        out = ''
        # Let's wait one second before reading output.
        # Let's give device time to answer.
        time.sleep(1)
        while ser.inWaiting() > 0:
            out += ser.read(1)

        if out != '':
            print "-->" + out

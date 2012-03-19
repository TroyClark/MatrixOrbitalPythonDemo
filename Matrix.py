class Matrix:
""" This class defines functions for clearing a Matrix Orbital display, 
prining a message to the screen, and reading a number of keys.
	ClearScreen()
	HelloWorld()
	ReadKeys(number of keys)
"""

import serial
global port
#Set up a serial port object using COM9 (port counting starts at 0)
#Default Matrix Orbital settings are used with a timeout of 5 seconds
port = serial.Serial(8,19200,serial.EIGHTBITS,serial.PARITY_NONE,serial.STOPBITS_ONE,timeout=5)
port.close()

def HelloWorld():
        message = "Hello World!"	#Create a message string
        ClearScreen()				#Clear the screen
        port.open()					#Open the port stream specified above
        port.write(message)			#Write the message
        port.close()				#Always close the port stream when not in use

def ReadKeys(number):
        key = ''					#Create a variable to store a key press
        ClearScreen()
        port.open()
        port.flushInput()			#Remove any keys that may already be in the buffer
        for i in range(0,number):	#While the user has requested keys to be read...
                key += port.read(1)	#Keep adding them to the key variable...
                port.write(key[i])	#And write them to the Matrix Orbital display
        port.close()

def ClearScreen():
        clearscreen = [chr(254), chr(88)]	#Variable to hold command bytes for clear screen
        port.open()
        for i in clearscreen:				#For each byte in the command...
                port.write(i)				#Write the current byte to the display
        port.close()

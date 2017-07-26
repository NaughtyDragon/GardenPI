###################################
#This module controls the Shift registers
###################################


import time
import RPi.GPIO

bindings={
	"RCLK" : 15,  #Storage FlipFlop clock
	"SER" : 7,    #serial input
	"SRCLK" : 11, #serial input clock
	"SRCLR" : 13} #Clear all registers


# Use Pin numbers instead of GPIO ids.
GPIO.setmode(GPIO.BOARD)
for pin in bindings.keys():
	GPIO.setup(bindings[pin], GPIO.OUT)
	if pin == "SRCLR": #SRCLR is active low
		GPIO.setup(bindings[pin], GPIO.HIGH)
	else:
		GPIO.setup(bindings[pin], GPIO.LOW)

def __set__(binding, state):
	GPIO.output(bindings[binding], state)

def __valveOn__(vid):		#Values are identified 1...
	__set__("SER",1)	#Serial input to 1
	__set__("SRCLK",1)	#Store the 1 in the first register
	__set__("SER",0)	#Reset the input to not produce other 1
	__set__("SRCLK",0)
	for count in range(1, vid):
		__set__("SRCLK",1)
		__set__("SRCLK",0)

def __clear__():
	__set__("SRCLR", 0)
	__set__("RCLK", 1)
	#time.sleep(1)
	__set__("RCLK", 0)
	__set__("SRCLR", 1)
	

def valveControl(vid, time):
	#Enable one specific valve for a specific time in seconds
	__valveOn__(vid)
	time.sleep(seconds)
	__clear__()

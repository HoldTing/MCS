#!/usr/bin/env python3
import time, RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.IN,pull_up_down=GPIO.PDU_DOWN)
while True:
	SwitchStatus=GPIO.input(24)
	if(SwitchStatus == 0):
		print('Button pressed')
	else:
		print('Button released')

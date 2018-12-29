#!/usr/bin/env python
import RPi.GPIO as GPIO

read_pin_number=19

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(read_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if GPIO.input(read_pin_number):
	print('1')

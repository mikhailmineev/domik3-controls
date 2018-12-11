#!/usr/bin/env python
import RPi.GPIO as GPIO

pin_number=17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if not GPIO.input(pin_number):
    print('1')


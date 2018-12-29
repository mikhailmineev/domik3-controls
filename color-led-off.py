#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

gpio_pin_number=16
read_pin_number=17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(read_pin_number, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
if not GPIO.input(read_pin_number):
	GPIO.setup(gpio_pin_number, GPIO.OUT)
	GPIO.output(gpio_pin_number, GPIO.HIGH)
	time.sleep(0.1)
	GPIO.output(gpio_pin_number, GPIO.LOW)
	time.sleep(0.1)

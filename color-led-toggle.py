#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

gpio_pin_number=16

GPIO.setmode(GPIO.BCM) # BCM pin numbering
GPIO.setwarnings(False)
GPIO.setup(gpio_pin_number, GPIO.OUT)
GPIO.output(gpio_pin_number, GPIO.HIGH)

time.sleep(0.2)

GPIO.output(gpio_pin_number, GPIO.LOW)


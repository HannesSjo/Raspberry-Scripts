#!/usr/bin/env python
import RPi.GPIO as GPIO
import subprocess
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    while GPIO.input(3) == GPIO.LOW:
        time.sleep(2)
    time.sleep(10)
    if (GPIO.input(3) != GPIO.LOW):
        break
subprocess.call(['shutdown', '-h', 'now'], shell=False)
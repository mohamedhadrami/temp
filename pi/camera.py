#!/usr/bin/env python

from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.start_preview()
sleep(5)
camera.capture('/home/pi/pololu-rpi-slave-arduino-library/pi/templates/images/image.jpg')
camera.stop_preview()
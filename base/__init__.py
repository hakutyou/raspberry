#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

import speed

class Robot():
    def __init__(self):
        GPIO.cleanup()
        self.speed_left = speed.Speed(40, "speed-left")
        self.speed_right = speed.Speed(38, "speed-right")

    def run(self):
        self.speed_left.start()
        self.speed_right.start()
        return

    def stop(self):
        self.speed_left.stop()
        self.speed_right.stop()
        return

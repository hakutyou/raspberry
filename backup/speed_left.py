#!/usr/bin/python
import multiprocessing
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Speed(object):
    def __init__(self, right_out_pin):
        self.rpin = right_out_pin
        #self.lpin = left_out_pin
        GPIO.setup(right_out_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        #GPIO.setup(left_out_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def count(self):
        print "Start.\n"
        self.i = 0
        while True:
            try:
                GPIO.wait_for_edge(self.rpin, GPIO.FALLING)
                self.i = self.i+1
                print "L",
                print self.i
            except KeyboardInterrupt:
                GPIO.cleanup()
        GPIO.cleanup()

s = Speed(40)
# 38 = right, 40 = left
s.count()


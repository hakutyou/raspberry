#!/usr/bin/python
import multiprocessing
import RPi.GPIO as GPIO

# left = 40
# right = 38
class Speed(multiprocessing.Process):
    def __init__(self, out_pin, processname):
        multiprocessing.Process.__init__(self)
        self.processname = processname
        self.processrun = True
        self.pin = out_pin
        print "process: %s" %(processname)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def run(self):
        print "%s start" %(self.processname)
        while self.processrun:
            GPIO.wait_for_edge(self.pin, GPIO.FALLING)
            print "%s get" %(self.processname)
        GPIO.cleanup()
        return

    def stop(self):
        self.processrun = False
        return

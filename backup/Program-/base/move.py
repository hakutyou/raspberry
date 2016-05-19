#!/bin/python
import multiprocessing
import RPi.GPIO as GPIO

class Wheel(object):
    def __init__(self, in_pin1, in_pin2):
        self.pin1 = in_pin1
        self.pin2 = in_pin2

        GPIO.setup(in_pin1, GPIO.OUT)
        GPIO.setup(in_pin2, GPIO.OUT)

    def forward(self):
        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)
        return

    def backward(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, True)
        return

    def stop(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)
        return

class Car(multiprocessing.Process):
    def __init__(self, l_pin1, l_pin2, r_pin1, r_pin2, queue):
        multiprocessing.Process.__init__(self)
        self.pipe = multiprocessing.Pipe(duplex=False)
        self.processname = processname
        self.left_wheel = Wheel(l_pin1, l_pin2)
        self.right_wheel = Wheel(r_pin1, r_pin2)
        self.stop()

        self.queue = queue
        self.processrun = True
        self.automove = False

    def run(self): # it means automove
        while processrun:
            msg = self.queue.get(block=True, time=0)
            command = { 'f': self.forward,
                        'b': self.backward,
                        'l': self.left,
                        'r': self.right,
                        's': self.still,
                        'a': self.auto
            }
            command.get(msg)()
        return

    def stop(self):
        self.automove = False
        self.processrun = False
        return

    def forward(self):
        self.left_wheel.forward()
        self.right_wheel.forward()
        return

    def backward(self):
        self.left_wheel.backward()
        self.right_wheel.backward()
        return

    def left(self):
        self.left_wheel.stop()
        self.right_wheel.forward()
        return

    def right(self):
        self.left_wheel.forward()
        self.right_wheel.stop()
        return

    def still(self):
        self.left_wheel.stop()
        self.right_wheel.stop()
        return

    def auto(self):
        self.automove = True
        self.processrun = False
        while self.automove:
            if not self.queue.empty:
                self.still()
                self.automove = False
                self.processrun = True
            print "automove not support now....."
            # here automove code
        return

## test program
#a = Car(31, 33, 35, 37)
#while True:
#    cmd = raw_input("Command: ")
#    command.get(cmd)()
#    if cmd == 'q':
#        break
## end

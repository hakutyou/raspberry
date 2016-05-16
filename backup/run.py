#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

class Wheel(object):
    def __init__(self, in_pin1, in_pin2):
        self.pin1 = in_pin1
        self.pin2 = in_pin2

        GPIO.setup(in_pin1, GPIO.OUT)
        GPIO.setup(in_pin2, GPIO.OUT)

    def forward(self):
        GPIO.output(self.pin1, True)
        GPIO.output(self.pin2, False)

    def backward(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, True)

    def stop(self):
        GPIO.output(self.pin1, False)
        GPIO.output(self.pin2, False)

class Car(object):
    def __init__(self):
        self.left_wheel = Wheel(31, 33)
        self.right_wheel = Wheel(35, 37)
        self.stop()

    def forward(self):
        self.left_wheel.forward()
        self.right_wheel.forward()

    def backward(self):
        self.left_wheel.backward()
        self.right_wheel.backward()

    def left(self):
        self.left_wheel.stop()
        self.right_wheel.forward()

    def right(self):
        self.left_wheel.forward()
        self.right_wheel.stop()

    def stop(self):
        self.left_wheel.stop()
        self.right_wheel.stop()

    def shutdown(self):
        self.stop()
        GPIO.cleanup()

# test program
a = Car()
command = { 'f': a.forward,
            'b': a.backward,
            'l': a.left,
            'r': a.right,
            's': a.stop,
            'q': a.shutdown,
          }
while True:
    cmd = raw_input("Command: ")
    command.get(cmd)()
    if cmd == 'q':
        break
# end

#!/usr/bin/python
import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)

class Turn(object):
    def __init__(self, in_pin):
        self.pin = in_pin
        GPIO.setup(in_pin, GPIO.OUT)
        p = GPIO.PWM(in_pin, 50)
        p.start()
        time.sleep(2)

    def turn(self):
        GPIO.output(self.pin, True)

    def stop(self):
        GPIO.output(self.pin, False)
    def quit(self):

# test program
a = Turn(40)
while True:
    cmd = raw_input("Command: ")
    if cmd == 'q':
        a.turn()
    else:
        a.stop()
# end

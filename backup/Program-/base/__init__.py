#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

from multiprocess import Queue
import speed
import move

class Robot():
    def __init__(self):
        GPIO.cleanup()
        self.speed_left = speed.Speed(40, "speed-left")
        self.speed_right = speed.Speed(38, "speed-right")
        self.move = move.Car(31, 33, 35, 37)

        self.robotrun = True
        self.movequeue = Queue()

    def run(self):
        self.speed_left.start()
        self.speed_right.start()
        self.move.start()
        while robotrun:
            try:
                command = raw_input("Command: ")
                self.movequeue.put(command)
            except KeyboardInterrupt:
                self.stop()
        self.stop()
        return

    def stop(self):
        self.speed_left.stop()
        self.speed_right.stop()
        self.move.stop()
        GPIO.cleanup()
        robotrun = False
        return

#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

import multiprocessing
import Queue
import time

import speed
import move

class Robot(multiprocessing.Process):
    def __init__(self):
        self.movequeue = multiprocessing.Queue()
        self.speedqueue = multiprocessing.Queue()
        self.exit = multiprocessing.Event()
        multiprocessing.Process.__init__(self)

        self.speed_left = speed.Speed(40, "left_speed", timeout=500, rqueue=self.speedqueue)
        self.speed_right = speed.Speed(38, "right_speed", timeout=500, rqueue=self.speedqueue)
        self.move = move.Car(31, 33, 35, 37, queue=self.movequeue)
        self.speed_left.start()
        self.speed_right.start()
        self.move.start()

    def run(self):
        self.speed_left.go()
        self.speed_right.go()
        self.move.go()

        while not self.exit.is_set():
            time.sleep(1)
        return

    def __shutdown_subprocess(self, process):
        process.shutdown()
        while process.is_alive():
            print "wait for %s" %(process.name)
            time.sleep(0.5)
        print "shutdowned: %s" %(process.name)
        return

    def shutdown(self):
        self.__shutdown_subprocess(self.speed_left)
        self.__shutdown_subprocess(self.speed_right)
        self.__shutdown_subprocess(self.move)
        self.speedqueue.close()
        self.movequeue.close()
        self.exit.set()
        GPIO.cleanup()
        return


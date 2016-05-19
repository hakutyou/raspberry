#!/bin/python
import RPi.GPIO as GPIO

import multiprocessing
import Queue
import time

class Wheel(object):
    def __init__(self, in_pin1, in_pin2):
        self.__pin1 = in_pin1
        self.__pin2 = in_pin2

        GPIO.setup(in_pin1, GPIO.OUT)
        GPIO.setup(in_pin2, GPIO.OUT)

    def forward(self):
        GPIO.output(self.__pin1, True)
        GPIO.output(self.__pin2, False)
        return

    def backward(self):
        GPIO.output(self.__pin1, False)
        GPIO.output(self.__pin2, True)
        return

    def shutdown(self):
        GPIO.output(self.__pin1, False)
        GPIO.output(self.__pin2, False)
        return

class Car(multiprocessing.Process):
    def __init__(self, lpin1, lpin2, rpin1, rpin2, queue, timeout=2):
        multiprocessing.Process.__init__(self)
        self.name = "move"
        self.queue = queue
        self.stop = False
        self.exit = multiprocessing.Event()
        self.__go = multiprocessing.Event()
        self.__timeout = timeout
        self.__lwheel = Wheel(lpin1, lpin2)
        self.__rwheel = Wheel(rpin1, rpin2)
        self.still()
        print "process: move"

    def go(self):
        self.__go.set()
        return

    def run(self):
        self.__go.wait()
        print "move start"
        while not self.exit.is_set():
            try:
                msg = self.queue.get(block=True, timeout=self.__timeout)
                command = { 'f': self.forward,
                            'b': self.backward,
                            'l': self.left,
                            'r': self.right,
                            's': self.still,
                            'R': self.rround,
                            'L': self.lround
                }
                command.get(msg)()
            except Queue.Empty:
                continue
        return

    def shutdown(self):
        self.still()
        self.exit.set()
        return

    def forward(self):
        self.__lwheel.forward()
        self.__rwheel.forward()
        self.stop = False
        return

    def backward(self):
        self.__lwheel.backward()
        self.__rwheel.backward()
        self.stop = False
        return

    def left(self):
        self.__lwheel.backword()
        self.__rwheel.forward()
        self.stop = False
        return

    def right(self):
        self.__lwheel.forward()
        self.__rwheel.shutdown()
        self.stop = False
        return

    def still(self):
        self.__lwheel.shutdown()
        self.__rwheel.shutdown()
        self.stop = True
        return

    def rround(self):
        self.__lwheel.forward()
        self.__rwheel.backward()
        return

    def lround(self):
        self.__lwheel.backward()
        self.__rwheel.forward()
        return


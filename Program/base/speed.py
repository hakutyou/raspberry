#!/usr/bin/python
import RPi.GPIO as GPIO
import multiprocessing

# left = 40, right = 38
class Speed(multiprocessing.Process):
    def __init__(self, out_pin, name, timeout, rqueue):
        # make sure first letter of name
        multiprocessing.Process.__init__(self)
        self.name = name
        self.squeue = rqueue
        self.exit = multiprocessing.Event()
        self.__go = multiprocessing.Event()
        self.__timeout = timeout
        self.__pin = out_pin
        self.__stillwarn = True
        print "process: %s" %(name)
        GPIO.setup(self.__pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def go(self):
        self.__go.set()
        return

    def run(self):
        self.__go.wait()
        print "%s start" %(self.name)
        while not self.exit.is_set():
            channel = GPIO.wait_for_edge(self.__pin, GPIO.FALLING, timeout=self.__timeout)
            if channel is None:
                if self.__stillwarn == True:
                    self.__stillwarn = False
                    print "%s not move" %(self.name)
                    self.squeue.put(self.name[0])
            else:
                print "%s get" %(self.name)
                self.__stillwarn = True
        GPIO.cleanup()
        return

    def shutdown(self):
        self.exit.set()
        return


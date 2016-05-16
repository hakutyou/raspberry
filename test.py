#!/usr/bin/python
import base

import threading

if __name__ == '__main__':
    robot = base.Robot()
    robot.run()
    while True:
        try:
            pass
        except KeyboardInterrupt:
            robot.stop()
    robot.stop()

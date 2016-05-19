#!/usr/bin/python
import base

if __name__ == '__main__':
    robot = base.Robot()
    robot.start()
    while True:
        if not robot.speedqueue.empty():
            print robot.speedqueue.get()
        try:
            command = raw_input()
            if command == 'q':
                break
            else:
                robot.movequeue.put(command)
        except KeyboardInterrupt:
            robot.shutdown()

    robot.shutdown()


#    def auto(self):
#        while self.robotrun and self.autorun:
#            time.sleep(1)
#            if not self.speedqueue.empty():
#                self.movequeue.put('a')
#                while not self.speedqueue.empty():
#                    print self.speedqueue.get(block=False)
#        return
#
#    def ctrl(self):
#        return



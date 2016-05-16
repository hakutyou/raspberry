#!/usr/bin/python
# coding=utf-8
import RPi.GPIO as GPIO
import time
import signal
import atexit
import sys

atexit.register(GPIO.cleanup)

servopin = 3
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servopin, GPIO.OUT)
p = GPIO.PWM(servopin,50) # 50HZ
p.start(0)
time.sleep(2)

if len(sys.argv) >= 2:
    degree = float(sys.argv[1])
else:
    exit()

p.ChangeDutyCycle(2.5 + degree/18)
time.sleep(float(sys.argv[2]))
p.ChangeDutyCycle(0)

# turn to middle
#for i in range(90,180,1):
#  p.ChangeDutyCycle(2.5 + 10 * i / 180) # 设置转动角度
#  time.sleep(0.02)                      # 等该20ms周期结束
#  p.ChangeDutyCycle(0)                  # 归零信号
#  time.sleep(0.2)
#
#for i in range(180,0,-1):
#  p.ChangeDutyCycle(2.5 + 10 * i / 180)
#  time.sleep(0.02)
#  p.ChangeDutyCycle(0)
#  time.sleep(0.2)

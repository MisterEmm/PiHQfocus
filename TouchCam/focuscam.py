from guizero import App, PushButton, Text, Window
from time import sleep
import time
import datetime
import sys, os
import subprocess
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
FEED_SERVO_CONTROL_PIN = 18

GPIO.setup(FEED_SERVO_CONTROL_PIN, GPIO.OUT)
PWM_FREQUENCY = 100 # In Hertz, which means 100 pulses in 1secs (1000ms) --> 1 pulse = 10ms

FULL_SPEED_FORWARD_DC = 20
FULL_SPEED_BACKWARD_DC = 10
FULL_SPEED_PAUSE_DC = 13.6
pwm = GPIO.PWM(FEED_SERVO_CONTROL_PIN, PWM_FREQUENCY)

def FullRight():
    pwm.start(FULL_SPEED_FORWARD_DC)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(FULL_SPEED_PAUSE_DC)
    
def FineRight():
    pwm.start(FULL_SPEED_FORWARD_DC)
    time.sleep(0.1)
    pwm.ChangeDutyCycle(FULL_SPEED_PAUSE_DC)

def FullLeft():
    pwm.start(FULL_SPEED_BACKWARD_DC)
    time.sleep(0.5)
    pwm.ChangeDutyCycle(FULL_SPEED_PAUSE_DC)
  
def FineLeft():
    pwm.start(FULL_SPEED_BACKWARD_DC)
    time.sleep(0.1)
    pwm.ChangeDutyCycle(FULL_SPEED_PAUSE_DC)

     
app = App(layout="grid", title="Focus Control", bg="black", width=150, height=625)

button1 = PushButton(app, grid=[0,0], width=150, height=150, image="/home/pi/TouchCam/icon/fullleft.png", command=FullLeft)
button2 = PushButton(app, grid=[0,1], width=150, height=150, image="/home/pi/TouchCam/icon/fineleft.png", command=FineLeft)
button3 = PushButton(app, grid=[0,2], width=150, height=150, image="/home/pi/TouchCam/icon/fineright.png", command=FineRight)
button4 = PushButton(app, grid=[0,3], width=150, height=150, image="/home/pi/TouchCam/icon/fullright.png", command=FullRight)

app.display()
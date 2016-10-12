#! /usr/bin/python3
import RPi.GPIO as GPIO
import time
import tkinter as tk
from tkinter import ttk

enable_pin = 18
in1_pin = 23
in2_pin = 24


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(enable_pin,GPIO.OUT)
GPIO.setup(in1_pin,GPIO.OUT)
GPIO.setup(in2_pin,GPIO.OUT)


pwm = GPIO.PWM(enable_pin,500)
pwm.start(0)

def clickForward():
    #action.configure(text="** Motor Forward")
    aLabel.configure(text= "Motor forward",foreground='red')
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    pwm.ChangeDutyCycle(50)

def clickReverse():
    #action.configure(text="** Motor Reverse")
    aLabel.configure(text= "Motor reverse",foreground='blue')
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin,True)
    pwm.ChangeDutyCycle(50)

def clickStop():
    #action.configure(text="** Motor Stop")
    aLabel.configure(text= "Motor Stop",foreground='green')
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin,False)
    

win = tk.Tk()
win.title("Motor GUI")
#win.resizable(0,0)
# adding a label
aLabel = ttk.Label(win,text="Motor GUI")
aLabel.grid(column=0, row=0)

#Forward Motor
action = ttk.Button(win, text="Forward", command=clickForward)
action.grid(column=1,row=0)

action = ttk.Button(win, text="Reverse", command=clickReverse)
action.grid(column=1,row=1)

action = ttk.Button(win, text="Stop", command=clickStop)
action.grid(column=1,row=2)

win.mainloop()

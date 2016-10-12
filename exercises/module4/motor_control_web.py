from flask import Flask, render_template, request
import time
import RPi.GPIO as GPIO
import webbrowser
import datetime
import sys
app = Flask(__name__)

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
    #aLabel.configure(text= "Motor forward",foreground='red')
    GPIO.output(in1_pin, True)
    GPIO.output(in2_pin, False)
    pwm.ChangeDutyCycle(50)

def clickReverse():
    #action.configure(text="** Motor Reverse")
    #aLabel.configure(text= "Motor reverse",foreground='blue')
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin,True)
    pwm.ChangeDutyCycle(50)

def clickStop():
    #action.configure(text="** Motor Stop")
    #aLabel.configure(text= "Motor Stop",foreground='green')
    GPIO.output(in1_pin, False)
    GPIO.output(in2_pin,False)
    

@app.route("/")
def hello():
    
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
	'title' : 'HELLO!',
	'time': timeString
	}

    return render_template('button.html', **templateData)

@app.route("/motor/<int:post_id>")
def handle_motor(post_id):
       if post_id == 1:
	  print "forward"
          clickForward()
       if post_id == 2:
          print  "reverse"
          clickReverse()
       if post_id == 3:
          print "stop"
	  clickStop()
 
if __name__ == "__main__":
   app.run(host='192.168.0.111',port=8080,debug=True)


import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
led_pins = [18,23,24]

GPIO.setup(led_pins[0],GPIO.OUT)
GPIO.setup(led_pins[1],GPIO.OUT)
GPIO.setup(led_pins[2],GPIO.OUT)


while True:
	which_led= raw_input("Enter LED(red-0 ,green-1,white-2):")
  	if (which_led == "0"):
		print "red led"
		GPIO.output(led_pins[0],True)
		time.sleep(1)
		GPIO.output(led_pins[0],False)
	if (which_led == "1"):
		print "green led"
		GPIO.output(led_pins[1],True)
		time.sleep(1)
		GPIO.output(led_pins[1],False)
	if (which_led == "2"):
		print "white led"
		GPIO.output(led_pins[2],True)
		time.sleep(1)
		GPIO.output(led_pins[2],False)
	
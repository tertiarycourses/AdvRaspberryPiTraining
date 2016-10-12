
from bottle import route, run
import RPi.GPIO as GPIO

#fill in your ip address
# hint : use ifconfig
host='x.x.x.x'

# setup the GPIO mode
GPIO.setmode(XXX)

# setup the GPIO pins
led_pins = [X, X, X]
led_states = [0, 0, 0]
switch_pin = 25

setup the led pins
GPIO.setup(X, GPIO.OUT)
GPIO.setup(X, GPIO.OUT)
GPIO.setup(X, GPIO.OUT)
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def switch_status():
    state = GPIO.input(switch_pin)
    if state:
        return 'Up'
    else:
        return 'Down'

def html_for_led(led):
    l = str(led)
    result = " <input type='button' onClick='changed(" + l + ")' value='LED " + l + "'/>"
    return result

def update_leds():
    for i, value in enumerate(led_states):
        GPIO.output(led_pins[i], value)

@route('/')
@route('/<led>')
def index(led="n"):
    print(led)
    if led != "n":
        led_num = int(led)
        led_states[led_num] = not led_states[led_num]
        update_leds()
    response = "<script>"
    response += "function changed(led)"
    response += "{"
    response += "  window.location.href='/' + led"
    response += "}"
    response += "</script>"
    
    response += '<h1>GPIO Control</h1>'
    response += '<h2>Button=' + switch_status() + '</h2>'
    response += '<h2>LEDs</h2>'
    response += html_for_led(0) 
    response += html_for_led(1) 
    response += html_for_led(2) 
    return response

run(host=host,port=8080)

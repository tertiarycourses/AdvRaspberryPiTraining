# Display text
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello world")

# Color
from sense_hat import SenseHat
sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
sense.show_message("Hello world",text_colour=yellow,back_colour=blue)


# Changing speed
from sense_hat import SenseHat
sense = SenseHat()

blue = (0,0,255)
yellow = (255,255,0)
sense.show_message("Hello world",text_colour=yellow,back_colour=blue,scroll_speed=0.5)

# Display text continuousy
from sense_hat import SenseHat
sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)

while True:
  sense.show_message("Astro Pi is awesome!", text_colour=yellow, back_colour=blue, scroll_speed=0.05)


# Display single character
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# Generate a random colour
def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)

while True:
    sense.show_letter("1", pick_random_colour())
    sleep(1)
    sense.show_letter("2", pick_random_colour())
    sleep(1)
    sense.show_letter("3", pick_random_colour())
    sleep(1)

# Display single pixel
from sense_hat import SenseHat

sense = SenseHat()
sense.clear((0,0,0))

sense.set_pixel(2, 2, (0, 0, 255))
sense.set_pixel(4, 2, (0, 0, 255))
sense.set_pixel(3, 4, (100, 0, 0))
sense.set_pixel(1, 5, (255, 0, 0))
sense.set_pixel(2, 6, (255, 0, 0))
sense.set_pixel(3, 6, (255, 0, 0))
sense.set_pixel(4, 6, (255, 0, 0))
sense.set_pixel(5, 5, (255, 0, 0))



# Display multiple pixels
from sense_hat import SenseHat

sense = SenseHat()

# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
creeper_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, b, b, g, g, b, b, g,
    g, b, b, g, g, b, b, g,
    g, g, g, b, b, g, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, b, b, b, g, g,
    g, g, b, g, g, b, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(creeper_pixels)


# Rotation
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()


# Sense Pressure
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure)

# Sense Temperature
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

temp = sense.get_temperature()
print(temp)

# Sense Humidity
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

humidity = sense.get_humidity()
print(humidity)

# Sense Environment data
from sense_hat import SenseHat
sense = SenseHat()

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.15)


# Check background
from sense_hat import SenseHat
sense = SenseHat()

# Define the colours red and green
red = (255, 0, 0)
green = (0, 255, 0)

while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + " Pressure: " + str(p) + " Humidity: " + str(h)
  
  if t > 18.3 and t < 26.7:
    bg = green
  else:
    bg = red
  
  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05, back_colour=bg)

# Detecting Pitch, Roll, and Yaw 
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()

while True:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    print("pitch {0} roll {1} yaw {2}".format(pitch, roll, yaw))
    sleep(1)

# Detect IMU valuaes
from sense_hat import SenseHat

sense = SenseHat()

# Display the letter J
sense.show_letter("J")

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x=round(x, 0)
	y=round(y, 0)
	z=round(z, 0)
	
	print("x={0}, y={1}, z={2}".format(x, y, z))

  # Update the rotation of the display depending on which way up the Sense HAT is
	if x  == -1:
	  sense.set_rotation(180)
	elif y == 1:
	  sense.set_rotation(90)
	elif y == -1:
	  sense.set_rotation(270)
	else:
	  sense.set_rotation(0)

# Detect Motion
from sense_hat import SenseHat

sense = SenseHat()

red = (255, 0, 0)

while True:
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 1 or y > 1 or z > 1:
        sense.show_letter("!", red)
    else:
        sense.clear()

# Detect Motion and Display text
from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()
while True:
  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      
      # Check which direction
      if event.direction == "up":
        sense.show_letter("U")      # Up arrow
      elif event.direction == "down":
        sense.show_letter("D")      # Down arrow
      elif event.direction == "left": 
        sense.show_letter("L")      # Left arrow
      elif event.direction == "right":
        sense.show_letter("R")      # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M")      # Enter key
      
      # Wait a while and then clear the screen
      sleep(0.5)
      sense.clear()

# Trigger function using Joystock
from sense_hat import SenseHat

sense = SenseHat()

# Define the functions
def red():
  sense.clear(255, 0, 0)

def blue():
  sense.clear(0, 0, 255)

def green():
  sense.clear(0, 255, 0)
  
def yellow():
  sense.clear(255, 255, 0)

# Tell the program which function to associate with which direction
sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear    # Press the enter key

while True:
  pass  # This keeps the program running to receive joystick events


# Create a gam
 # IMPORT the required libraries (sense_hat, time, random) 
from sense_hat import SenseHat
from time import sleep
from random import choice

# CREATE a sense object
sense = SenseHat()

# Set up the colours (white, green, red, empty)

w = (150, 150, 150)
g = (0, 255, 0)
r = (255, 0, 0)
e = (0, 0, 0)

# Create images for three different coloured arrows

arrow = [
e,e,e,w,w,e,e,e,
e,e,w,w,w,w,e,e,
e,w,e,w,w,e,w,e,
w,e,e,w,w,e,e,w,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e,
e,e,e,w,w,e,e,e
]

arrow_red = [
e,e,e,r,r,e,e,e,
e,e,r,r,r,r,e,e,
e,r,e,r,r,e,r,e,
r,e,e,r,r,e,e,r,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e,
e,e,e,r,r,e,e,e
]

arrow_green = [
e,e,e,g,g,e,e,e,
e,e,g,g,g,g,e,e,
e,g,e,g,g,e,g,e,
g,e,e,g,g,e,e,g,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e,
e,e,e,g,g,e,e,e
]

# Set a variable pause to 3 (the initial time between turns)  
# Set variables score and angle to 0  
# Create a variable called play set to True (this will be used to stop the game later)  
pause = 3
score = 0
angle = 0
play = True

sense.show_message("Keep the arrow pointing up", scroll_speed=0.05, text_colour=[100,100,100])

# WHILE play == True 
while play:
  
    # CHOOSE a new random angle 
    last_angle = angle
    while angle == last_angle:
        angle = choice([0, 90, 180, 270])
        
    sense.set_rotation(angle)
    
    # DISPLAY the white arrow
    sense.set_pixels(arrow)
    
    # SLEEP for current pause length  
    sleep(pause)
    
    
    acceleration = sense.get_accelerometer_raw()
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = round(x, 0)
    y = round(y, 0)

    print(angle)
    print(x)
    print(y)

    # IF orientation matches the arrow...
    if x == -1 and angle == 180:
        # ADD a point and turn the arrow green  
        sense.set_pixels(arrow_green)
        score += 1
    elif x == 1 and angle == 0:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == -1 and angle == 90:
      sense.set_pixels(arrow_green)
      score += 1
    elif y == 1 and angle == 270:
      sense.set_pixels(arrow_green)
      score += 1
    else:
      # SET play to `False` and DISPLAY the red arrow
      sense.set_pixels(arrow_red)
      play = False

    # Shorten the pause duration slightly  
    pause = pause * 0.95
    
    # Pause before the next arrow 
    sleep(0.5)

# When loop is exited, display a message with the score  
msg = "Your score was %s" % score
sense.show_message(msg, scroll_speed=0.05, text_colour=[100, 100, 100])
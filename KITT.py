# Imports
import time
from machine import Pin
from neopixel import NeoPixel

# Define the strip pin number (28) and number of LEDs (15)
strip = NeoPixel(Pin(28), 15)

# Colour variable
red = 255,0,0

lightPos = 0
lightDir = 1
pressed = 0

while True: # Run forever
    
    time.sleep(0.07) # Delay
    
    for i in range(15):
        RGB = list(strip[i])  # We need to adjust existing values so have to convert the current NeoPixel colour to a list
        if RGB[0] != 0:
            RGB[0] = int(RGB[0]/1.7) # Fade the red value by a factor of 1.7, larger values shorten the trail
        strip[j] = tuple(RGB) # Convert the list back to a tuple for the NeoPixel functions
                
    lightPos = lightPos + lightDir    # Adjust the position of the light along the strip
    if lightPos == 14 or lightPos == 0:  # If it's reached either end of the strip
        lightDir = lightDir * -1  # change it's direction
        
    # Set the NeoPixel at the lightPos position to the current list index colour
    strip[lightPos] = (red)

    # Write the data to the LED strip
    strip.write()

from ws2812 import WS2812
import machine


# Defined colors
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)


# Turn on and initialize the LED
power = machine.Pin(11, machine.Pin.OUT)
power.value(1)
led = WS2812(12, 1)

# Transition from color to color with 1 second wait in between
led.color_solid(GREEN, 1)
led.color_solid(YELLOW, 1)
led.color_solid(RED, 1)
led.color_flash(RED, 1)

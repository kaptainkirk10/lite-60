import time

OFF = (0, 0, 0)

class WS2812():        
    def __init__(self, pin_num, led_count, brightness = 0.5):
        self.led_count = led_count
        self.brightness = brightness

    def pixels_show(self):
        print("pixels_show")
        time.sleep(10/1000)

    def pixels_set(self, i, color):
        print(f"pixels_set {i} {color}")

    def pixels_fill(self, color):
        print(f"pixels_fill {color}")

    def pixels_blink(self, color):
        print(f"pixels_blink {color}")

    def color_chase(self, color, wait):
        for i in range(self.led_count):
            self.pixels_set(i, color)
            time.sleep(wait)
            self.pixels_show()
        time.sleep(0.2)

    def wheel(self, pos):
        """Input a value 0 to 255 to get a color value.
        The colours are a transition r - g - b - back to r.
        """
        if pos < 0 or pos > 255:
            return (0, 0, 0)
        if pos < 85:
            return (255 - pos * 3, pos * 3, 0)
        if pos < 170:
            pos -= 85
            return (0, 255 - pos * 3, pos * 3)
        pos -= 170
        return (pos * 3, 0, 255 - pos * 3)

    def rainbow_cycle(self, wait):
        for j in range(255):
            for i in range(self.led_count):
                rc_index = (i * 256 // self.led_count) + j
                self.pixels_set(i, self.wheel(rc_index & 255))
            self.pixels_show()
            time.sleep(wait)

    def color_solid(self, color, wait):
        print(f"color_solid {color}")
        self.pixels_fill(color)
        self.pixels_show()
        time.sleep(wait)

    def color_flash(self, color, wait, blink_interval=1):
        print(f"color_flash {color} {wait} {blink_interval}")
        iterations = round(wait / blink_interval)
        print(f"iterations: {iterations}")
        for i in range(iterations):
            print(i)
            if i % 2 == 0:
                self.pixels_fill(color)
            else:
                self.pixels_fill(OFF)
            self.pixels_show()
            time.sleep(blink_interval)

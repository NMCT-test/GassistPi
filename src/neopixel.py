import time
from rpi_ws281x import PixelStrip, Color


class PixelRing(PixelStrip):
    def __init__(self, num=24, pin=12, *args, **kwargs):
        super().__init__(num, pin, *args, **kwargs)

    def loop(self, color, wait_ms=50):
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)
            self.show()
            time.sleep(wait_ms / 1000.0)
            self.setPixelColor(i, 0)
            self.setPixelColor(i - 1, 0)

        for i in range(self.numPixels() - 1, -1, -1):
            self.setPixelColor(i, color)
            self.show()
            time.sleep(wait_ms / 1000.0)
            self.setPixelColor(i, 0)
            self.setPixelColor(i + 1, 0)

    def wipe(self, color, wait_ms=50):
        """Wipe color across display a pixel at a time."""
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)
            self.show()
            time.sleep(wait_ms / 1000.0)

    def chase(self, color, wait_ms=50, iterations=10):
        """Movie theater light style chaser animation."""
        for j in range(iterations):
            for q in range(3):
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i + q, color)
                self.show()
                time.sleep(wait_ms / 1000.0)
                for i in range(0, self.numPixels(), 3):
                    self.setPixelColor(i + q, 0)

    def reset(self, color, wait_ms=10):
        for i in range(self.numPixels()):
            self.setPixelColor(i, color)
            self.show()

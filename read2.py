#http://levi.etn.fm/blog/2014/06/02/how-to-increase-spi-clock-speed-in-python-for-the-raspberry-pi/

import spidev

self.spi = spidev.SpiDev()
self.spi.open(0, 0)
self.spi.max_speed_hz = 25000000

final_buf = []
for i in range(0, self.leds):
    final_buf.append(self.buffer[i][0])
    final_buf.append(self.buffer[i][1])
    final_buf.append(self.buffer[i][2])
    final_buf.append(0)
self.spi.xfer(final_buf)
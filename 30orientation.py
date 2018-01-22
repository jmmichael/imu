#https://www.element14.com/community/community/raspberry-pi/raspberrypi_projects/blog/2015/09/24/foginator-2000-003-raspberry-pi-sense-hat-integration-with-initial-state

from sense_hat import SenseHat
import time
import sys

sense = SenseHat()
sense.clear()

var = 30

while var > 0:
  orientation = sense.get_orientation_degrees()
  print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))
  time.sleep(1)
  var = var -1
  if var == 0:
    sys.exit()

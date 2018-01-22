from sense_hat import SenseHat
import time
import sys


sense = SenseHat()
sense.clear()

var = 30

while var > 0:
	gyro_only = sense.get_gyroscope()
	print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))
	time.sleep(1)
	var = var -1
	if var == 0:
		sys.exit()

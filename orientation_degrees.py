from sense_hat import SenseHat

sense = SenseHat()
orientation_rad = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation_rad))

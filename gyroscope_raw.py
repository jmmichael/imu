from sense_hat import SenseHat

sense = SenseHat()
raw = sense.get_gyroscope_raw()
print("x: {x}, y: {y}, z: {z}".format(**raw))

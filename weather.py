from sense_hat import SenseHat
from time import time
from time import sleep

sense = SenseHat()

temp = round(sense.get_temperature()*1.8 +32)
humidity = round(sense.get_humidity())
pressure = round(sense.get_pressure())
message = 'Temperature is %d F Humidity is %d percent Pressure is %d mbars' %(temp,humidity,pressure)


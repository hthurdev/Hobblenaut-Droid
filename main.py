from adafruit_servokit import ServoKit

import time
kit = ServoKit(channels=16)
kit.servo[0].angle = 0
time.sleep(1)
for angle in range(0,180):
	kit.servo[0].angle = angle
	print(angle)
	time.sleep(0.3)

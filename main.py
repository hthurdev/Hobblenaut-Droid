from adafruit_servokit import ServoKit

import time
kit = ServoKit(channels=16)
#Body Servo Assignments
#KNEES
LKnee = kit.servo[11]
RKnee = kit.servo[12]
#HIPS
LHipFB = kit.servo[2]
RHipFB = kit.servo[3]
LHipLR = kit.servo[4]
RHipLR = kit.servo[5]
#FEET
LFootFB = kit.servo[6]
RFootFB = kit.servo[7]
LFootLR = kit.servo[8]
RFootLR = kit.servo[9]
#WAIST
Waist = kit.servo[10]

position = "standing"

if position == "standing":
	print("Now Standing")
	LKnee.angle = 110
	RKnee.angle = 85
	LHipFB.angle = 15
	RHipFB.angle = 165
	LHipLR.angle = 30
	RHipLR.angle = 165
	LFootFB.angle = 30
	RFootFB.angle = 160
	LFootLR.angle = 150
	RFootLR.angle = 50
	
	







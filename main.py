from adafruit_servokit import ServoKit

import time
kit = ServoKit(channels=16)
#Body Servo Assignments
#KNEES

LKnee = kit.servo[11]
LKnee.actuation_range = 60
LKnee.set_pulse_width_range(1650,2300)
RKnee = kit.servo[12]
RKnee.actuation_range = 60
RKnee.set_pulse_width_range(800,1450)
#HIPS
LHipFB = kit.servo[2]
LHipFB.actuation_range = 90
LHipFB.set_pulse_width_range(700,1700)
RHipFB = kit.servo[3]
RHipFB.actuation_range = 90
RHipFB.set_pulse_width_range(1300,2300)
LHipLR = kit.servo[4]
LHipLR.actuation_range = 60
LHipLR.set_pulse_width_range(900,1566)
RHipLR = kit.servo[5]
RHipLR.actuation_range = 60
RHipLR.set_pulse_width_range(1583,2250)
#FEET
LFootFB = kit.servo[6]
LFootFB.actuation_range = 117
LFootFB.set_pulse_width_range(700,2000)
RFootFB = kit.servo[7]
RFootFB.actuation_range = 117
RFootFB.set_pulse_width_range(1050,2350)
##TODO \/ \/ \/
LFootLR = kit.servo[8]
LFootLR.set_pulse_width_range(500,2500)
RFootLR = kit.servo[9]
RFootLR.set_pulse_width_range(500,2500)
#WAIST
Waist = kit.servo[10]
#Testing
TestServo = kit.servo[15]

position = "testing"

"""
# Obsolete, kept for reference

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
"""

#Soon to be the default standing position
if position == "testing": 
	LKnee.angle = 0
	RKnee.angle = 60
	LHipFB.angle = 15
	RHipFB.angle = 75
	LHipLR.angle = 0
	RHipLR.angle = 60
	LFootFB.angle = 0 + 25 
	RFootFB.angle = 117 - 25
	
	#TODO - Tune PWM Range of LFoot and RFoot LR
	
	







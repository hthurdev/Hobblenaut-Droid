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
LFootLR.actuation_range = 99
LFootLR.set_pulse_width_range(1250,2350)
RFootLR = kit.servo[9]
RFootLR.actuation_range = 90
RFootLR.set_pulse_width_range(850,1850)
#WAIST
Waist = kit.servo[10]
#Testing
TestServo = kit.servo[15]

position = "testing"

"""
Ranges:
LKnee: 0-60, default 0
RKnee: 0-60, default 60
LHipFB: 0-90, default 15
RHipFB: 0-90, default 75
LHipLR: 0-60, default 0
RHipLR: 0-60, default 60
LFootFB: 0-117, default 25
RFootFB: 0-117, default 92
LFootLR: 0-99, default 77
RFootLR: 0-90, default 18

"""

#Soon to be the default standing position
if position == "testing": 
	LKnee.angle = 0
	RKnee.angle = 60
	LHipFB.angle = 0 + 15
	RHipFB.angle = 90 - 15
	LHipLR.angle = 0
	RHipLR.angle = 60
	LFootFB.angle = 0 + 25 
	RFootFB.angle = 117 - 25
	LFootLR.angle = 99 - 22
	RFootLR.angle = 0 + 18
	

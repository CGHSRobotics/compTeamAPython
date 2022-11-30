# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Robotics1                                                    #
# 	Created:      11/30/2022, 10:21:18 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

import sys # import all of these!
import vex
from vex import *
import math
import util
from util import *

import inputHandler
from inputHandler import *
import userController
from userController import *

ALLOW_DEBUG = True # True: Displays Debug info/ runs usercontrol, False: normal program operation
AUTONOMOUS_PROGRAM = "3-Side" # Options are: "3-Side", "2-Side", "Debug"

# you can make your own functions and classes used in the below three functions here.

brain = Brain() # Brain object
controller = Controller() # controller object
input = Input(controller) # input object

motorFrontLeft = Motor()



def pre_auton(): # place pre-auto code here
    pass

def autonomous(): # place autonomous code here
    pass

def drivercontrol(): # place main control code here
    while True:
        pass


competition = vex.Competition(drivercontrol, autonomous) # competition object

# check if in actual competition
if not competition.is_competition_switch() or not competition.is_field_control():
    if ALLOW_DEBUG:
        drivercontrol()

pre_auton()
        

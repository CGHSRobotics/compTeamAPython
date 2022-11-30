# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       Robotics1                                                    #
# 	Created:      11/30/2022, 10:21:18 AM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

import vex

from inputHandler import *
from userController import *
from vexDevices import *

# Global Control Variables
ALLOW_DEBUG = True  # True: Displays Debug info/ runs usercontrol
AUTONOMOUS_PROGRAM = "3-Side"  # Options are: "3-Side", "2-Side", "Debug"


def pre_auton():  # place pre-auto code here
    pass


def autonomous():  # place autonomous code here
    pass


def drivercontrol():  # place main control code here
    thread_UpdateMotors = Thread(user_updateMotors)


competition = vex.Competition(drivercontrol, autonomous)  # competition object

# check if in actual competition
if not competition.is_competition_switch() or not competition.is_field_control():
    if ALLOW_DEBUG:
        drivercontrol()

pre_auton()

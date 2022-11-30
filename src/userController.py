
from vex import *
from util import *

from inputHandler import *
from vexDevices import *


def spinMotorAtSpeed():
    pass

# Applies input from user to motors


def user_updateMotors():
    while True:
        # Check input form Axis
        input.getAxis(controller, 5)

        brain.screen.set_cursor(1, 1)
        brain.screen.print("Axis1: " + str(input.axis1))

        sleep(20)

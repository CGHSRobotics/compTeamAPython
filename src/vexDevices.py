import sys  # import all of these!
import vex
from vex import *
import math
import util
from util import *

import inputHandler
from inputHandler import *

# Vex Device Declarations
# Brain, Controller, Input, Motors etc...

brain = Brain()  # Brain object
controller = Controller()  # controller object
input = Input(controller)  # input object

# Drive Motors
motorFrontLeft = Motor(Ports.PORT1, 18_1, False)
motorBackLeft = Motor(Ports.PORT2, 18_1, False)
motorFrontRight = Motor(Ports.PORT3, 18_1, False)
motorBackRight = Motor(Ports.PORT4, 18_1, False)
# Other Motors
motorIntake = Motor(Ports.PORT1, 18_1, False)
motorRoller = Motor(Ports.PORT2, 18_1, False)
# Pneumatics
pneuEndgame = Pneumatics(brain.three_wire_port.a)
# Gyroscope
gyro = Gyro(brain.three_wire_port.b)

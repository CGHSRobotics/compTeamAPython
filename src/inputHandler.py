
from vex import *
from util import *

# Custom Button Class that is created for every button


class Button:
    def __init__(self, isToggled) -> None:
        self.isToggled = isToggled

    isPressed = False
    raw_pressed = False
    isToggled = False

    # Callback for when is pressed
    def pressed(self):
        pass

    # Callback for when is released
    def released(self):
        pass


class Input:
    def __init__(self, __controller) -> None:
        self.y = Button(False)
        self.x = Button(False)
        self.a = Button(False)
        self.b = Button(False)

        self.left = Button(False)
        self.up = Button(False)
        self.right = Button(False)
        self.down = Button(False)

        self.l1 = Button(False)
        self.l2 = Button(False)
        self.r1 = Button(False)
        self.r2 = Button(False)

        self.setupCallbacks(__controller)

    def setupCallbacks(self, __controller):
        try:
            # Press/Release Callbacks for Letter Buttons
            __controller.buttonY.pressed(self.y.pressed)
            __controller.buttonY.released(self.y.released)
            __controller.buttonX.pressed(self.x.pressed)
            __controller.buttonX.released(self.x.released)
            __controller.buttonA.pressed(self.a.pressed)
            __controller.buttonA.released(self.a.released)
            __controller.buttonB.pressed(self.b.pressed)
            __controller.buttonB.released(self.b.released)
            # Press/Release Callbacks for Arrow Buttons
            __controller.buttonLeft.pressed(self.left.pressed)
            __controller.buttonLeft.released(self.left.released)
            __controller.buttonUp.pressed(self.up.pressed)
            __controller.buttonUp.released(self.up.released)
            __controller.buttonRight.pressed(self.right.pressed)
            __controller.buttonRight.released(self.right.released)
            __controller.buttonDown.pressed(self.down.pressed)
            __controller.buttonDown.released(self.down.released)
            # Press/Release Callbacks for L1/L2/R1/R2
            __controller.buttonL1.pressed(self.l1.pressed)
            __controller.buttonL1.released(self.l1.released)
            __controller.buttonL2.pressed(self.l2.pressed)
            __controller.buttonL2.released(self.l2.released)
            __controller.buttonR1.pressed(self.r1.pressed)
            __controller.buttonR1.released(self.r1.released)
            __controller.buttonR2.pressed(self.r2.pressed)
            __controller.buttonR2.released(self.r2.released)
        except:
            # ERROR HAS OCCURED
            print("hi")

    def getAxis(self, __controller, cutoff):
        self.axis1 = processAxis(__controller.axis1.position(), cutoff)
        self.axis2 = processAxis(__controller.axis1.position(), cutoff)
        self.axis3 = processAxis(__controller.axis1.position(), cutoff)
        self.axis4 = processAxis(__controller.axis1.position(), cutoff)


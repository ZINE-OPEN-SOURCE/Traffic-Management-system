import time
import os

os.system("cls")


class TrafficLight:

    def __init__(self, Number):

        self.green = 0
        self.red = 1
        self.yellow = 0
        self.Number = Number

    def RedToYellow(self, *args):

        print("Switching Traffic Light", self.Number, "from Red to Red + Yellow")
        self.yellow = 1
        self.red = 1
        self.green = 0
        display()

    def YellowToGreen(self, *args):

        print("Switching Traffic Light", self.Number, "from Yellow to Green")
        self.yellow = 0
        self.green = 1
        self.red = 0
        display()

    def GreenToYellow(self, *args):

        print("Switching Traffic Light", self.Number, "from Green to Yellow")
        self.yellow = 1
        self.green = 0
        self.red = 0
        display()

    def YellowToRed(self, *args):

        print("Switching Traffic Light", self.Number, "from Yellow to Red")
        self.red = 1
        self.yellow = 0
        self.green = 0
        display()

        # def Green(self, *args):

        #     self.green = 1

    # def Red(self, *args):

    #     self.red = 1


# def AllRed():

#     Tr1.Red()
#     Tr2.Red()
#     Tr3.Red()
#     Tr4.Red()


def FirstPass():

    Tr1.RedToYellow()
    Tr4.GreenToYellow()
    time.sleep(2)
    Tr1.YellowToGreen()
    Tr4.YellowToRed()
    time.sleep(5)

    # AllRed()
    # time.sleep(1)


def SecondPass():

    Tr2.RedToYellow()
    Tr1.GreenToYellow()
    time.sleep(2)
    Tr2.YellowToGreen()
    Tr1.YellowToRed()
    time.sleep(5)


def ThirdPass():

    Tr3.RedToYellow()
    Tr2.GreenToYellow()
    time.sleep(2)
    Tr3.YellowToGreen()
    Tr2.YellowToRed()
    time.sleep(5)


def FourthPass():

    Tr4.RedToYellow()
    Tr3.GreenToYellow()
    time.sleep(2)
    Tr4.YellowToGreen()
    Tr3.YellowToRed()
    time.sleep(5)


def display():

    print("\t", Tr2.Number, end=" ")
    if Tr2.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr2.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr2.green == 1:
        print("\u001b[32;1mG\u001b[0m", end=" ")
    print("\n")
    print(Tr1.Number, end=" ")
    if Tr1.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr1.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr1.green == 1:
        print(" \u001b[32;1mG\u001b[0m", end=" ")
    print("\t\t", Tr3.Number, end=" ")
    if Tr3.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr3.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr3.green == 1:
        print("\u001b[32;1mG\u001b[0m", end=" ")
    print("\n")
    print("\t", Tr4.Number, end=" ")
    if Tr4.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr4.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr4.green == 1:
        print("\u001b[32;1mG\u001b[0m", end=" ")
    print("\n")


# ------------main -------------------------
Tr1 = TrafficLight(1)
Tr2 = TrafficLight(2)
Tr3 = TrafficLight(3)
Tr4 = TrafficLight(4)

while True:
    FirstPass()
    print("\n")
    display()
    print("\n")
    SecondPass()
    print("\n")
    display()
    print("\n")
    ThirdPass()
    print("\n")
    display()
    print("\n")
    FourthPass()
    print("\n")
    display()
    print("---------------------------------------------------------------------------")
    print("\n")
import time
import os

os.system("cls")


class TrafficLight:

    def __init__(self, Number):

        self.green = 0
        self.red = 1
        self.yellow = 0
        self.Number = Number

    def RedToYellow(self, *args):

        print("Switching Traffic Light", self.Number, "from Red to Red + Yellow")
        self.yellow = 1
        self.red = 1
        self.green = 0
        display()

    def YellowToGreen(self, *args):

        print("Switching Traffic Light", self.Number, "from Yellow to Green")
        self.yellow = 0
        self.green = 1
        self.red = 0
        display()

    def GreenToYellow(self, *args):

        print("Switching Traffic Light", self.Number, "from Green to Yellow")
        self.yellow = 1
        self.green = 0
        self.red = 0
        display()

    def YellowToRed(self, *args):

        print("Switching Traffic Light", self.Number, "from Yellow to Red")
        self.red = 1
        self.yellow = 0
        self.green = 0
        display()

        # def Green(self, *args):

        #     self.green = 1

    # def Red(self, *args):

    #     self.red = 1


# def AllRed():

#     Tr1.Red()
#     Tr2.Red()
#     Tr3.Red()
#     Tr4.Red()


def FirstPass():

    Tr1.RedToYellow()
    Tr4.GreenToYellow()
    time.sleep(2)
    Tr1.YellowToGreen()
    Tr4.YellowToRed()
    time.sleep(5)

    # AllRed()
    # time.sleep(1)


def SecondPass():

    Tr2.RedToYellow()
    Tr1.GreenToYellow()
    time.sleep(2)
    Tr2.YellowToGreen()
    Tr1.YellowToRed()
    time.sleep(5)


def ThirdPass():

    Tr3.RedToYellow()
    Tr2.GreenToYellow()
    time.sleep(2)
    Tr3.YellowToGreen()
    Tr2.YellowToRed()
    time.sleep(5)


def FourthPass():

    Tr4.RedToYellow()
    Tr3.GreenToYellow()
    time.sleep(2)
    Tr4.YellowToGreen()
    Tr3.YellowToRed()
    time.sleep(5)


def display():

    print("\t", Tr2.Number, end=" ")
    if Tr2.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr2.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr2.green == 1:
        print("\u001b[32;1mG\u001b[0m", end=" ")
    print("\n")
    print(Tr1.Number, end=" ")
    if Tr1.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr1.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr1.green == 1:
        print(" \u001b[32;1mG\u001b[0m", end=" ")
    print("\t\t", Tr3.Number, end=" ")
    if Tr3.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr3.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr3.green == 1:
        print("\u001b[32;1mG\u001b[0m", end=" ")
    print("\n")
    print("\t", Tr4.Number, end=" ")
    if Tr4.red == 1:
        print("\u001b[31;1mR\u001b[0m", end=" ")
    if Tr4.yellow == 1:
        print("\u001b[33;1mY\u001b[0m", end=" ")
    if Tr4.green == 1:
        print("\u001b[32;1mG\u001b[0m", end=" ")
    print("\n")


# ------------main -------------------------
Tr1 = TrafficLight(1)
Tr2 = TrafficLight(2)
Tr3 = TrafficLight(3)
Tr4 = TrafficLight(4)

while True:
    FirstPass()
    print("\n")
    display()
    print("\n")
    SecondPass()
    print("\n")
    display()
    print("\n")
    ThirdPass()
    print("\n")
    display()
    print("\n")
    FourthPass()
    print("\n")
    display()
    print("---------------------------------------------------------------------------")
    print("\n")

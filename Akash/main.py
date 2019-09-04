import time


class TrafficLight:

    def __init__(self, Number):

        self.green = 0
        self.red = 1
        self.yellow = 0
        self.Number = Number

    def RedToYellow(self, *args):

        print("Switching Traffic Light", self.Number, "from Red to Yellow")
        self.yellow = 1
        self.display()
        
    def YellowToGreen(self, *args):
        
        print("Switching Traffic Light", self.Number, "from Yellow to Green")
        self.yellow = 0
        self.green = 1
        self.red = 0
        self.display()

    def GreenToYellow(self, *args):

        print("Switching Traffic Light", self.Number, "from Green to Yellow")
        self.yellow = 1
        self.green = 0
        self.display()
    def YellowToRed(self, *args):
    
        print("Switching Traffic Light", self.Number, "from Yellow to Red")
        self.red = 1
        self.yellow = 0
        self.display()

    def display(self, *args):

        print(self.Number, "R :", self.red, "Y :",
              self.yellow, "G :", self.green)

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


# ------------main -------------------------
Tr1 = TrafficLight(1)
Tr2 = TrafficLight(2)
Tr3 = TrafficLight(3)
Tr4 = TrafficLight(4)

FirstPass()
Tr1.display()
Tr2.display()
Tr3.display()
Tr4.display()
SecondPass()
Tr1.display()
Tr2.display()
Tr3.display()
Tr4.display()
ThirdPass()
Tr1.display()
Tr2.display()
Tr3.display()
Tr4.display()
FourthPass()
Tr1.display()
Tr2.display()
Tr3.display()
Tr4.display()

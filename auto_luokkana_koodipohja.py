"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Code template for a simplified car assignment
implementation using a class.
zannatul.2.ferdous@tui.fi
name:zannatul ferdous
"""

class Car:
    """
    Class Car: Implements a car that moves a certain distance and
    whose gas tank can be filled. The class defines what a car is:
    what information it contains and what operations can be
    carried out for it.
    """

    def __init__(self, tank_size, gas_consumption,gas=0, odometer=0):
        """
        Constructor, initializes the newly created object.

        :param tank_size: float, the size of this car's tank.
        :param gas_consumption: float, how much gas this car consumes
                   when it drives a 100 kilometers
        """

        self.__tank_volume = tank_size
        self.__consumption = gas_consumption
        self.__gas=gas  #the amount of gas
        self.__odometer=odometer  #no of km in car's odometer


        # TODO:
        # create and initialize the rest of the attributes.

    def fill(self, amount):
        if (amount < 0):
            print('You cannot remove gas from the tank')
            return
        if (amount <= self.__tank_volume ):
            self.__gas += amount
            if (self.__gas > self.__tank_volume):
                self.__gas=self.__tank_volume


    def drive(self,drivenKm):
       # print('before self.__gas',self.__gas)
        #print('self.__odometer',self.__odometer)
        drivenAble = self.__gas * self.__consumption
        if (drivenAble<drivenKm):

            consume = drivenAble / self.__consumption
            #print(self.__consumption)
            #print(consume)
            rest = (consume - consume)
            self.__gas = rest
           # print('drivenAble',drivenAble)
            self.__odometer+=drivenAble

        else:
            self.__odometer += drivenKm
            #print(self.__odometer)
            consume = drivenKm / self.__consumption
           # consume = self.__odometer / self.__consumption
            #print(self.__consumption)
            #print(consume)
            rest = (self.__gas - consume)
           # rest = (self.__consumption - consume)

            self.__gas = rest
            #print('after', self.__gas)
            #if (self.__odometer > self.__tank_volume):
             #   self.__gas = self.__tank_volume

    def print_information(self):
        print(
            f'The tank contains {self.__gas:.1f} liters of gas and the odometer shows {self.__odometer:.1f} kilometers.')

    #
    #    f"The tank contains {:.1f} liters of gas and the odometer shows {:.1f} kilometers."
    #                         ^                                           ^
    #
    # You need to add the correct attributes to points marked with carets "^".

def main():
    tank_size = read_number("How much does the vehicle's gas tank hold?")
    gas_consumption = read_number("How many liters of gas does the car "
                                  "consume per hundred kilometers?")
    car = Car(tank_size, gas_consumption)
    while True:
        car.print_information()
        choice = input("1) Fill 2) Drive 3) Quit\n-> ")
        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up?")
            car.fill(to_fill)
        elif choice == "2":
            distance = read_number("How many kilometers to drive?")
            car.drive(distance)

            # TODO:
            # call the drive-method for the car-object here (task c)
             
        elif choice == "3":
            print("Thank you and bye!")
            break


def read_number(prompt, error_message="Incorrect input!"):
    """
    **** DO NOT MODIFY THIS FUNCTION ****

    This function is used to read input (float) from the user.

    :param prompt: str, prompt to be used when asking user input.
    :param error_message: str, what error message to print
        if the entered value is not a float.
    """

    while True:
        try:
            return float(input(prompt + " "))

        except ValueError:
            print(error_message)


if __name__ == "__main__":
    main()

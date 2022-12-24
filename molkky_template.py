"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
class Player():
    def __init__(self,name,points=0,points_list=[],total_throws=0,total_hits=0):
        self.__name=name
        self.__points=points
        self.__list=points_list
        self.__totalThrows=total_throws
        self.__totalHits=total_hits

    def get_name(self):
        return self.__name

    def add_points(self,point):
        self.__totalThrows += 1

        if (self.__points > 0):
            self.__totalHits += 1
        # print(self.__totalThrows,self.__totalHits)

        print(self.__totalHits, self.__totalThrows)
        self.__points+=point
        if self.__points < 50 and self.__points >= 40:
            print(
                f"{self.__name} needs only {50 - self.__points} points. It's better to avoid knocking down the pins with higher points.")

    def get_points(self):
        return self.__points
    def hit_percentage(self):

        if self.__totalThrows == 0:
            return 0.0
        else:
            return (self.__totalHits / self.__totalThrows) * 100


    def calculate(self,new_points):

        if(self.__points not in self.__list):
            self.__list.append(self.__points)
        sum=0
        for point in self.__list:
            sum+=point
        if(new_points> sum/len(self.__list) and self.__list[-2]!=0):
            print('previous point is:' ,self.__list[-2])
            print(f'Cheers {self.get_name()}!')
        return  sum/len(self.__list)





    #if(40<<=49):
        #    print(f"{self.__name} needs only {self.points} points. It's better to avoid knocking down the pins with higher points.")

    def has_won(self):
        if self.__points == 50:
            return True
        elif self.__points>50:
            print(f'{self.__name} gets penalty points!')
            print('')
            self.__points = 25
            return False


# a) Implement the class Player here.


def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        in_turn.calculate(pts)

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p" ,'hit percentage', player1.hit_percentage())
        print(player2.get_name() + ":", player2.get_points(), "p",'hit percentage', player1.hit_percentage())
        print("")

        throw += 1


if __name__ == "__main__":
    main()

"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

This program models a character adventuring in a video game.
"""
import random


class Character:
    def __init__(self, player, hitpoints):
        self.player=player
        self.list=[]
        self.__no_of_item=0
        self.__countedItem={}
        self.__hitpoints=hitpoints
    def get_name(self):
        return  self.player

    def give_item(self, item):
        self.list.append(item)

    def remove_item(self,del_item):
        self.list.remove(del_item)
        #print('list of weapons:',self.player ,self.list)

    def how_many(self,count_item):
        self.__no_of_item=self.list.count(count_item)
        return  self.__no_of_item

    def printout(self):
        print(f"Name: {self.player}")
        print(f"Hitpoints: {self.__hitpoints}")

        if self.list == []:
            print('  --nothing--')
        for item in sorted(self.list):
            self.__no_of_item=self.list.count(item)
            self.__countedItem[item]=self.__no_of_item
        #print(self.__countedItem)
        for keys in self.__countedItem:
            print(f"  {self.list.count(keys)} {keys}")



    def has_item(self,item):
        if item in self.list:
            return True
        else:
            return False



    """
    This class defines what a character is int he game and what
    he or she can do.
    """

    # TODO: copy your Character class implementation from
    #       the previous assignment here and implement the
    #       following new methods.
    #
    #       Also note, that you have to modify at least
    #       __init__ and printout methods to conform with
    #       the new bahavior of the class.

    def pass_item(self, item, target):
        if item in self.list:
            target.list.append(item)
            self.list.remove(item)
            return True
        elif item not in self.list:
            return False


        """
        Passes (i.e. transfers) an item from one person (self)
        to another (target).

        :param item: str, the name of the item in self's inventory
                     to be given to target.
        :param target: Character, the target to whom the item is to
                     to be given.
        :return: True, if passing the item to target was successful.
                 False, it passing the item failed for any reason.
        """

        # TODO: implementation of the method


    def attack(self, target, weapon):
        if weapon in WEAPONS:
                #error statements:
            if weapon not in self.list:
                 print(f"Attack fails: {self.player}"+" doesn't have "+ f'"{weapon}".')
            elif self.player== target.player:
                print(f"Attack fails: {self.player} can't attack him/herself.")
            else:
                print(f"{self.player} attacks {target.player} delivering {WEAPONS[weapon]} damage.")
                if self.player != target.player:
                    target.__hitpoints -= WEAPONS[weapon]
                    if target.__hitpoints <= 0:
                        print(f"{self.player} successfully defeats {target.player}.")
        elif weapon not in WEAPONS:
            print(f'Attack fails: unknown weapon "{weapon}".')
              #print(WEAPONS[weapon])
        #print(target.player,target.__hitpoints)
        """
        A character (self) attacks the target using a weapon.
        This method will also take care of all the printouts
        relevant to the attack.

        There are three error conditions:
          (1) weapon is unknown i.e. not a key in WEAPONS dict.
          (2) self does not have the weapon used in the attack
          (3) character tries to attack him/herself.
        You can find the error message to printed in each case
        from the example run in the assignment.

        The damage the target receives if the attack succeeds is
        defined by the weapon and can be found as the payload in
        the WEAPONS dict. It will be deducted from the target's
        hitpoints. If the target's hitpoints go down to zero or
        less, the target is defeated.

        The format of the message resulting from a successful attack and
        the defeat of the target can also be found in the assignment.

        :param target: Character, the target of the attack.
        :param weapon: str, the name of the weapon used in the attack
                       (must be exist as a key in the WEAPONS dict).
        :return: True, if attack succeeds.
                 False, if attack fails for any reason.
        """

        # TODO: the implementation of the method


WEAPONS = {
    # Weapon          Damage
    #--------------   ------
    "elephant gun":     15,
    "gun":               5,
    "light saber":      50,
    "sword":             7,
}


def main():
    conan = Character("Conan the Barbarian", 10)
    deadpool = Character("Deadpool", 45)
    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        conan.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        deadpool.give_item(test_item)

    conan.pass_item("sword", deadpool)
    deadpool.pass_item("hero outfit", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)
    conan.pass_item("sausage", deadpool)
    deadpool.pass_item("gun", conan)

    print("-" * 5, "How are things after passing items around", "-" * 20)
    conan.printout()
    deadpool.printout()
    print("-" * 5, "Let's see how a fight proceeds", "-" * 32)

    # Conan's turn
    conan.attack(deadpool, "sword") # Conan doesn't have a sword.
    conan.attack(conan, "gun")      # A character is not allowed to attack himself.
    conan.attack(conan, "pen")      # Pen is not a known weapon in WEAPONS dict.
    conan.attack(deadpool, "gun")   # Attack with a gun.

    # Deadpool retaliates
    deadpool.attack(conan, "sword") # Deadpool has a sword.

    # Conan's 2nd turn
    conan.attack(deadpool, "gun")   # Attack with a gun again.

    # Deadpool strikes back again and Conan drops "dead".
    deadpool.attack(conan, "sword")

    print("Are You Not Entertained?!")

    print("-" * 5, "How are things after beating each other up", "-" * 20)

    conan.printout()
    deadpool.printout()


if __name__ == "__main__":
    main()

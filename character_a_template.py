"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
zannatul.2.ferdous@tuni.fi
1501646
This program models a character adventuring in a video game,
or more like, the stuff that the character carries around.
"""

class Character:
    def __init__(self, player):
        self.player=player
        self.list=[]
        self.__no_of_item=0
        self.__countedItem={}
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





    # TODO: the class implementation goes here.



def main():
    character1 = Character("Conan the Barbarian")
    character2 = Character("Deadpool")

    for test_item in ["sword", "sausage", "plate armor", "sausage", "sausage"]:
        character1.give_item(test_item)

    for test_item in ["gun", "sword", "gun", "sword", "hero outfit"]:
        character2.give_item(test_item)

    character1.remove_item("sausage")
    character2.remove_item("hero outfit")

    character1.printout()
    character2.printout()

    for hero in [character1, character2]:
        print(f"{hero.get_name()}:")

        for test_item in ["sausage", "sword", "plate armor", "gun", "hero outfit"]:
            if hero.has_item(test_item):
                print(f"  {test_item}: {hero.how_many(test_item)} found.")
            else:
                print(f"  {test_item}: none found.")


if __name__ == "__main__":
    main()

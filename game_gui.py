"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name    Zannatul Ferdous
Mail    zannatul.2.ferdous@tuni.fi
Student Number: 150164676

Make A Meaningful Word GAME PROJECT
"""
# Project Details
import random

"""
there will be 28 boxes, 7 rows,4 columns, 7*4=28, From A-Z , 26 letters will remain on those boxes as label, 
i have to create 5 meaningful word within 2 minutes, sliding the letters, if i can't ,i ll loose.  
so i'll just borrow the concept of boxes from '15 end game' example to set the boxes as gui, rest idea is mine
"""
"""
Game Rules:
There are 26 letter boxes with 2 empty boxes, Total 28 boxes for 7rows and 4columns(7*4=28).
Player has to make 5 meaningfull word within 120seconds, 
There are two players in the game. Player has to choose the correct fruit continuously 5 times and the goal is to score 10 points.
"""

"""
Fruit guessing game: A player has to guess the fruit name. The goal is to score 10 points within 120 seconds.
Player can play as many times a he can within the time limit but he has 2 life. If he fails twice he will loose his life 1.
"""

from tkinter import *
from tkinter import messagebox

WINPOINTS = 10


class GameGUI:
    def __init__(self):
        self.__mainw = Tk()
        self.__mainw.title(f"Fruit Game")  # window title
        self.__mainw.option_add("*Font", "Verdana 14")
        self.__mainw.geometry("600x400")  # window geometry
        self.__mainw.configure(bg="black")  # window background

        question_list = ['medium size and round. I can be red, green or yellow.',
                         'long and slightly curved with my taste being sweet.',
                         'small and red. People like me',
                         'yellow and medium size. I taste sour.',
                         'juicy and sweet. My name sounds as a colour']

        fruits = {'watermelon': 'green,big,juicy, eaten in summer',
                  'apple': 'medium size and round. I can be red, green or yellow',
                  'strawberry': 'small and red. People like me',
                  'blueberry': 'dark blue, small in size, i am very healthy',
                  'banana': 'long and slightly curved with my taste being sweet.',
                  'orange': 'juicy and sweet. My name sounds as a colour.'}
        index_fruit = random.randrange(len(fruits))  # index of a random fruit
        print(index_fruit)
        list = []
        for key in fruits:
            list.append(key)
            #print(key)
        fruit = list[index_fruit]
        #print(fruit)

        button_list = []

        # for i in range(len(fruits)):
        # self.__text_label = Label(self.__mainw, text=f'I am {question_list[0]}')
        # self.__text_label.grid(row=0, column=0, sticky=E)
        radio_button = IntVar()
        q_label = Label(text=f'What I am?{question_list[0]}', foreground='red', background='black')
        q_label.grid(row=0, column=0, columnspan=2, sticky=W)

        for i in range(1, 4):
            index_fruit = random.randrange(len(list))
            print(index_fruit)
            #print(i)
            r = Radiobutton(self.__mainw, text=list[index_fruit], variable=radio_button, value=i,
                            command=self.selection, foreground='red', background='black')
            r.grid(row=i, sticky=W)

        # self.__buttons=Radiobutton(self.__mainw,text=fruits.keys(),foreground='red',background='black')
        # self.__buttons.grid(row=1,column=0,sticky=W)

        # self.__buttons = Radiobutton(self.__mainw, text='apple',foreground='red',background='black')
        # self.__buttons.grid(row=2, column=0,sticky=W)

        """  for y in range(ROW):
            for x in range(COLUMN):
                button=Button(self.__mainw,text=chr(65+count),width=5,relief=RAISED,borderwidth=4)
                button.grid(row=y,column=x)
                count+=1
                print(65+count)
                if(65+count) >=91:
                    #print('hi')
                    break"""

    def selection(self):
        selection = "You selected the option "

    def stop(self):
        '''This method distroy the main window when pressed the exit button'''

        self.__mainw.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainw.mainloop()


def main():
    '''Starts the program'''

    gui = GameGUI()
    gui.start()


if __name__ == '__main__':
    main()

"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       zannatul Ferdous
Email:      xxxx.yyyyyy@tuni.fi

Code template for counter program.
"""

from tkinter import *



class Counter:
    def __init__(self):
        self.__mw=Tk()
        self.__value=0
        self.__current_value_label=Label(self.__mw,text=f"{self.__value}",borderwidth=2, relief=GROOVE)
        self.__current_value_label.grid(row=0,column=0,columnspan=4,sticky=W+E)
        self.__reset_button=Button(self.__mw,text="Reset",command=self.reset)
        self.__reset_button.grid(row=1,column=0)
       # self.__reset_button.grid(row=1,column=0,borderwidth=2, relief=GROOVE)
        self.__increase_button=Button(self.__mw,text='Increase',command=self.increase)
        self.__increase_button.grid(row=1,column=1)
        self.__decrease_button=Button(self.__mw,text='Decrease',command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)
        self.__quit_button=Button(self.__mw,text='Quit',command=self.quit)
        self.__quit_button.grid(row=1,column=3)

        self.__mw.mainloop()


        # TODO: You have to create one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value_label  # Label displaying the current value of the counter.
        #       self.__reset_button         # Button which resets counter to zero.
        #       self.__increase_button      # Button which increases the value of the counter by one.
        #       self.__decrease_button      # Button which decreases the value of the counter by one.
        #       self.__quit_button          # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.

    # TODO: Implement the rest of the needed methods here.
    def reset(self):

        self.__value=0
        self.__current_value_label.configure(text=f'{self.__value}')


    def increase(self):
        self.__value+=1
        self.__current_value_label.configure(text=f'{self.__value}')

    def decrease(self):
        self.__value-=1
        self.__current_value_label.configure(text=f"{self.__value}")
    def quit(self):
        self.__mw.destroy()



def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()

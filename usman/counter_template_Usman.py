"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 0123456
Name:       Muhammad Usman
Email:      muhammad.usman@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        self.__main_window = Tk()
        self.__value=0
        self.__current_value_label=Label(self.__main_window, text=f"{self.__value}")
        self.__current_value_label.grid(row=0, columnspan=3)  # Label displaying the current value of the counter.
        self.__reset_button= Button(self.__main_window, text="Reset", command=self.reset)
        self.__reset_button.grid(row=1, column=0)        # Button which resets counter to zero.
        self.__increase_button =Button(self.__main_window, text="Increase", command=self.increase)
        self.__increase_button.grid(row=1, column=1)     # Button which increases the value of the counter by one.
        self.__decrease_button  =Button(self.__main_window, text="Decrease", command=self.decrease)
        self.__decrease_button.grid(row=1, column=2)    # Button which decreases the value of the counter by one.
        self.__quit_button =Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=1, column=3)         # Button which quits the program.
        self.__main_window.mainloop()
    # TODO: Implement the rest of the needed methods here.
    def quit(self):
        self.__main_window.destroy()
    def increase(self):
        self.__value +=1
        self.__current_value_label.configure(text=f'{self.__value}')

    def decrease(self):
        self.__value -=1
        self.__current_value_label.configure(text=f'{self.__value}')

    def reset(self):
        self.__value=0
        self.__current_value_label.configure(text=f'{self.__value}')

def main():
    gui=Counter()
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()

from tkinter import *

class GUI:
  def __init__(self):
    self.__main_window = Tk()

    self.__time_24 = Entry()
    self.__time_24.pack()

    self.__convert_button = Button(self.__main_window, text="Convert",
                                 command=self.convert)
    self.__convert_button.pack()

    self.__time_12 = Entry()
    self.__time_12.pack()

    self.__quit_button = Button(self.__main_window, text="Quit",
                                 command=self.quit)
    self.__quit_button.pack()

    self.__main_window.mainloop()

  def convert(self):
    time_24_hour_clock = self.__time_24.get()

    # To save space the error checks for time_24_hour_clock's
    # value have been removed from here.

    (hours, minutes) = time_24_hour_clock.split(".")
    hours = int(hours)

    if hours < 1:           # 00.00-00.59 -> 12.00 AM-12.59 AM
        hours += 12
        suffix = "AM"

    elif hours < 12:        # 01.00-11.59 ->  1.00 AM-11.59 AM
        suffix = "AM"

    elif 12 <= hours < 13:  # 12.00-12.59 -> 12.00 PM-12.59 PM
        suffix = "PM"

    else:                    # 13.00-23.59 ->  1.00 PM-11.59 PM
        hours -= 12
        suffix = "PM"

    result = f"{hours}:{minutes} {suffix}"

    self.__time_12.delete(0, END)
    self.__time_12.insert(0, result)

  def quit(self):
    self.__main_window.destroy()



def main():
    GUI()
if __name__ == '__main__':
    main()
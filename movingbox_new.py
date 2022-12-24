from tkinter import *

class Game:
    def __init__(self):

        '''Main Window'''

        self.__mainwindow = Tk(className='Python Tkinter Scoring Game')
        self.__mainwindow.geometry("1000x200")
        self.__mainwindow.configure(bg="black")
        self._alarm_id = None
        self._paused = False
        self._starttime = 25 * 60

    def countdown(self, timeInSeconds, start=True):
        if start:
            self._starttime = timeInSeconds
        if self._paused:
            self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds, False)
        else:
            mins, secs = divmod(timeInSeconds, 60)
            timeformat = "{0:02d}:{1:02d}".format(mins, secs)
            app.labelvariable.set(timeformat)
            self._alarm_id = self.master.after(1000, self.countdown, timeInSeconds-1, False)

def main():
    gui=Game()

if __name__ == "__main__":
    main()
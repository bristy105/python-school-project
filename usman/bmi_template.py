"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name    Muhammad Usman
Mail    muhammad.usman@tuni.fi

Body Mass Index template
"""

from tkinter import *
NAN = float("NaN")

class Userinterface:
    """
            This class calculates the BMI of a prseon regarding weight and height.
            """

    def __init__(self):
        self.__float_result = NAN
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_lable = Label(self.__mainwindow, text="Enter Weight:")
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_lable = Label(self.__mainwindow, text="Enter Height:")
        self.__height_value = Entry(self.__mainwindow)


        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text="BMI-Value", command=self.calculate_BMI)

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_label = Label(self.__mainwindow, text="Result:")
        self.__result_text = Label(self.__mainwindow, text=NAN)

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow, text=f"")

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text="Stop", command=self.stop)


        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__weight_lable.grid(row=0)                  #remove in cas
        self.__weight_value.grid(row=1)
        self.__height_lable.grid(row=2)                   #remove in case
        self.__height_value.grid(row=3)
        self.__calculate_button.grid(row=4)
        self.__stop_button.grid(row=5)
        self.__result_label.grid(row=6)
        self.__result_text.grid(row=7)                   #remove in case
        self.__explanation_text.grid(row=8)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        try:
            w= float(self.__weight_value.get())
            h = float(self.__height_value.get())
            if w > 0 and h >0:
                self.__float_result = w / (h / 100) ** 2
                self.__result_text.configure(text=f'{self.__float_result:.2f}')
                if self.__float_result > 25:
                    self.__explanation_text["text"] = "You are overweight."

                elif self.__float_result < 18.5:
                    self.__explanation_text["text"] = "You are underweight."

                else:
                    self.__explanation_text["text"] = "Your weight is normal."
            elif w < 0 or h <0:
                self.__float_result = ''
                self.__result_text.configure(text=self.__float_result)
                self.__explanation_text["text"] = "Error: height and weight must be positive."
        except:
            w=0.0
            h=0.0
            self.__float_result=''
            self.__result_text.configure(text=self.__float_result)
            self.__explanation_text["text"] = "Error: height and weight must be numbers."

    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """
        try:
            w= float(self.__weight_value.get())
            h = float(self.__height_value.get())
            if w < 0 or h < 0:
                self.__result_text.configure(text='')
                self.__weight_value.delete(0,'end')
                self.__height_value.delete(0,'end')
        except:
            w = 0.0
            h = 0.0
            self.__float_result = 0.0
            self.__result_text.configure(text='')
            self.__weight_value.delete(0, 'end')
            self.__height_value.delete(0, 'end')


        #self.__current_value_label.configure(text=f'{self.__value}')






    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()

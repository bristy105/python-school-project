"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Zannnatul Ferdous
zannatul.2.ferdous@tuni.fi
150164676

Body Mass Index template
"""

from tkinter import *
NAN = float("NaN")


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        self.__float_result = NAN


        # Creating the components of the GUI
        # TODO: Create an Entry-component for the weight.

        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.

        self.__height_value = Entry(self.__mainwindow)

        self.__weight_label = Label(self.__mainwindow, text='Weight(kg):')
        self.__height_label = Label(self.__mainwindow, text='Height(cm):')

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow,text='BMI',command=self.calculate_BMI)


        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text_label = Label(self.__mainwindow,text='Result:')
        self.__result_text = Label(self.__mainwindow,text=self.__float_result)


        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow)

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow,text='Stop',command=self.stop)

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__height_label.grid(row=1,column=0,sticky=E)
        self.__weight_label.grid(row=0,column=0,sticky=E)
        self.__weight_value.grid(row=0,column=2,columnspan=3)
        self.__height_value.grid(row=1,column=2,columnspan=3)
        self.__calculate_button.grid(row=2,column=2)
        self.__stop_button.grid(row=2,column=3)
        self.__result_text_label.grid(row=3,column=0)
        self.__result_text.grid(row=3,column=1)
        self.__explanation_text.grid(row=3,column=2,columnspan=3)



    # TODO: Implement this method.
    def calculate_BMI(self):
        try:
            #print(type(self.__height_value))
            height = float(self.__height_value.get())

            weight =float(self.__weight_value.get())

            if height <=0 or weight<=0:
                self.__result_text.configure(text='')

                self.__explanation_text.configure(text='Error: height and weight must be positive.')
                self.__height_value.delete(0,END)
                self.__weight_value.delete(0,END)

            else:
                result = weight / (height * height * 0.0001)
               # print(result)
                self.__result_text.configure(text=f"{result:0.2f}")
                if 18.5< result < 25:
                    self.__explanation_text.configure(text='Your weight is normal.')
                elif result > 25:
                    self.__explanation_text.configure(text='You are overweight.')
                else:
                    self.__explanation_text.configure(text='You are underweight.')


        except ValueError:
            self.__height_value.delete(0,END)
            self.__weight_value.delete(0,END)
            self.__explanation_text.configure(text='Error: height and weight must be numbers.')
            self.__result_text.configure(text='')


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



    # TODO: Implement this method.
    def reset_fields(self):
        try:
            height = float(self.__height_value.get())

            weight = float(self.__weight_value.get())

            if weight<=0 or height<=0:

                self.__height_value.delete(0,END)
                self.__weight_value.delete(0,END)
                self.__result_text.configure(text='')

        except:
            self.__height_value=0.0
            self.__weight_value = 0.0
            self.__result_text.configure(text='')

        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """



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

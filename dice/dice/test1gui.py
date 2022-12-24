import tkinter as tk
str_int_lst = list()

class Creation(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master

        self.master.title('Creation')
        self.frame_test()

    def frame_test(self):

        data_frame = tk.Frame(self, bg='Gold', height=122, width=200)

        self.rowconfigure(0, weight=5)
        for i in range(1, 13):
            self.rowconfigure(i, weight=1)

        data_frame.grid(row=2, rowspan=10, sticky='W' + 'E' + 'N' + 'S')


        entry = list()
        entry = list()
        radio_vars = []
        for j in range(10):
            ...
            check_radio = tk.StringVar()
            radio_vars.append(check_radio)
            #check_radio = tk.StringVar()

            global lst

            tk.Label(data_frame, text=f'enter key {j + 1}', bg='Gold', font=('Times New Roman', 10)).grid(row=2 + j,
                                                                                                          padx=(50, 0))
            check_radio = tk.StringVar()
            radio_vars.append(check_radio)
            entry[j].grid(row=2 + j, column=1, padx=(10, 10))

            radio_int = tk.Radiobutton(data_frame, text='Integer', variable=check_radio, value=1,
                                       command=str_int_lst.append((j, check_radio.get())))
            radio_int.deselect()
            radio_int.grid(row=2 + j, column=2)

            radio_str = tk.Radiobutton(data_frame, text='String', variable=check_radio, value=2,
                                       command=str_int_lst.append((j, check_radio.get())))
            radio_str.deselect()
            radio_str.grid(row=2 + j, column=3)

if __name__ == '__main__':
    root = tk.Tk()
    program = Creation(root)
    program.grid()
    program.mainloop()
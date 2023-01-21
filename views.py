import tkinter as tk


class StartPage(tk.Tk):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: self.controller.change_view("PageOne"))
        button1.place(x=500, y=100)
        print("si")
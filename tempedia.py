from tkinter import *
from PIL import ImageTk, Image

class Tempedia():

    def startApp(self):
        self.width = 800
        self.height = 450
        self.title = "Tempedia"

        self.activewidgets = []

        self.root = Tk()
        self.root.resizable(False,False)
        self.root.title(self.title)
        self.root.geometry(str(self.width) + 'x' + str(self.height))

        self.goMain()

        self.root.mainloop()

    def resetActualView(self):
        for x in self.activewidgets:
            x.destroy()
        self.root.update()

    def goMain(self):
        self.resetActualView()

        self.bg = ImageTk.PhotoImage(Image.open("menu2.jpg"))
        l1 = Label(self.root, image = self.bg)
        l1.place(x=0,y=0)
        self.activewidgets.append(l1)
        print("dale")

        btn = Button(self.root, text='Click me !', command=lambda:self.goTempedia())
        btn.place(x=100, y=20)
        self.activewidgets.append(btn)

        self.root.update()

    def goTempedia(self):
        self.resetActualView()
        btn = Button(self.root, text='Click me !', command=lambda:self.goMain())
        self.activewidgets.append(btn)
        btn.place(x=10, y=10)
        self.root.update()



tempedia = Tempedia()
tempedia.startApp()
import tkinter
import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
from data import Data

class Tempedia():

    def __init__(self):
        self.data = Data()
        self.data.loadData()

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

        self.bg = ImageTk.PhotoImage(Image.open("resources/images/background/menu.jpg"))
        background = Label(self.root, image = self.bg)
        background.place(x=0,y=0)
        self.activewidgets.append(background)

        btn = Button(self.root, text='Tempedia', command=lambda:self.goTempedia("Mimit"))
        btn.place(x=350, y=200)
        self.activewidgets.append(btn)


    def goTempedia(self, temtemName):
        self.resetActualView()

        # SELECT TEMTEM
        newTemtem = self.data.getTemtemByName(temtemName)
        if newTemtem != None:
            self.temtem = newTemtem

        #self.bg = ImageTk.PhotoImage(Image.open("resources/images/menu.jpg"))
        #background = Label(self.root, image=self.bg)
        #background.place(x=0, y=0)
        #self.activewidgets.append(background)

        # INPUT TEMTEM
        entry = Entry(self.root, justify=tkinter.LEFT, width=10, font=('Arial 12'))
        entry.place(x=40, y=60)
        self.activewidgets.append(entry)
        btnSearch = Button(self.root, text='Search', command=lambda: self.goTempedia(entry.get()))
        btnSearch.place(x=150, y=58)
        self.activewidgets.append(btnSearch)

        # IMAGEN
        self.temtemImage = ImageTk.PhotoImage(Image.open("resources/images/temtem/"+self.temtem['name']+".webp").resize((80,80),Image.LANCZOS))
        temtemImageLabel = Label(self.root, image=self.temtemImage)
        temtemImageLabel.place(x=40, y=100)
        self.activewidgets.append(temtemImageLabel)

        # NAME TEMTEM
        nameTemtemLabel = Label(self.root, text = self.temtem['name'], font='Helvetica 18 bold' )
        nameTemtemLabel.place(x=130, y=100)
        self.activewidgets.append(nameTemtemLabel)

        # IMAGEN TIPO 1
        self.temtemType1 = ImageTk.PhotoImage(Image.open("resources/images/types/" + self.temtem['types'][0] + ".webp").resize((40,40),Image.LANCZOS))
        temtemType1Label = Label(self.root, image=self.temtemType1)
        temtemType1Label.place(x=130, y=140)
        self.activewidgets.append(temtemType1Label)
        # IMAGEN TIPO 2
        if len(self.temtem['types'])>1:
            self.temtemType2 = ImageTk.PhotoImage(Image.open("resources/images/types/" + self.temtem['types'][1] + ".webp").resize((40, 40), Image.LANCZOS))
            temtemType2Label = Label(self.root, image=self.temtemType2)
            temtemType2Label.place(x=170, y=140)
            self.activewidgets.append(temtemType2Label)

        #STATS



        btn = Button(self.root, text='Back', command=lambda:self.goMain())
        self.activewidgets.append(btn)
        btn.place(x=10, y=10)

        self.root.update()





tempedia = Tempedia()
tempedia.startApp()
from tkinter import *
import src.constants as const

class DictList(Frame):

    currList = []

    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller
        self.parent = parent

        self.presetButton = Button(self, text="Preset", width=10, command=lambda: self.showDicts(True))
        self.presetButton.pack()

        self.originalButton = Button(self, text="Original", width=10, command=lambda: self.showDicts(False))
        self.originalButton.pack()

    def listADict(self, name):
        label = Label(self, text=name)
        label.pack()
        self.currList.append(label)
        playButton = Button(self, text="Play", width=10, command= lambda: self.playDict(name))
        playButton.pack()
        self.currList.append(playButton)
        editButton = Button(self, text="Edit", width=10)
        editButton.pack()
        self.currList.append(editButton)

    def showDicts(self, preset):
        for widget in self.currList:
            widget.destroy()
        dictNames = const.Db.getDictNames(preset)
        for name in dictNames:
            self.listADict(name)

    def playDict(self, name):
        const.CURRDICT = name
        self.parent.master.showGame()
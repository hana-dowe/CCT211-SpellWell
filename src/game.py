from tkinter import *
import tkinter
import re
import random
from src.constants import CURRDICT, DB

class Game(Frame):

    dictionary = DB.getDict(CURRDICT)
    remainingKeys = list(dictionary)
    currKey = ""
    
    def __init__(self, parent, controller, width, height):
        Frame.__init__(self, parent, width=width, height=height)
        self.controller = controller
        
        self.definition = tkinter.Label(self, text="")
        self.definition.pack()

        self.wordValue = StringVar()
        self.wordValue.trace('w', self.limitInputLength)
        valCommand = (self.register(self.isText), '%S')
        self.entry = tkinter.Entry(self, validate="all", validatecommand=valCommand, textvariable=self.wordValue)
        self.entry.pack()
        
        self.button = tkinter.Button(self, text="Check", width=10, command=self.checkEntry)
        self.button.pack()

        self.statusLabel = tkinter.Label(self, text="", width= 20)
        self.statusLabel.pack()

        self.randomKey()

    def checkEntry(self):
        if self.entry.get().lower() == self.currKey.lower():
            self.statusLabel.configure(text="")
            self.entry.delete(0, END)
            if (len(self.remainingKeys) == 0) :
                self.gameWin()
            else:
                self.randomKey()
        else:
            if (len(self.remainingKeys) != 0) :            
                self.statusLabel.configure(text="try again")
        

    def randomKey(self):
        self.currKey = random.choice(self.remainingKeys)
        self.remainingKeys.remove(self.currKey)
        self.definition.configure(text=self.dictionary[self.currKey])
        self.limitInputLength()


    def isText(self, text):
        alphabetRule = re.compile("[a-zA-Z]+")
        if (re.match(alphabetRule, text)):
            return True
        else:
            return False 

    # source : https://stackoverflow.com/questions/33518978/python-how-to-limit-an-entry-box-to-2-characters-max
    def limitInputLength(self, *args):
        value = self.wordValue.get()
        i = len(self.currKey)
        if len(value) > i: 
            self.wordValue.set(value[:i])

    def newGame(self):
        # TODO call this from other scenes before switching to this scene
        # OR call this every time scene is shown (if that's an existing thing)
        self.dictionary = DB.getDict(CURRDICT)
        self.remainingKeys = list(self.dictionary)
        self.currKey = ""
        self.button["state"] = "normal"
        self.statusLabel.configure(text="")
        self.randomKey()

    def gameWin(self):
        self.definition.configure(text="")
        self.statusLabel.configure(text="you win!")
        # TODO disable button 
        self.button["state"] = "disabled"
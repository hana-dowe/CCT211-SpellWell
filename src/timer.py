from tkinter import *

# source: https://www.geeksforgeeks.org/create-countdown-timer-using-python-tkinter/

class Timer(Frame):

    stop = False

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, width=100, height=50)
        self.parent = parent
        self.controller = controller
        
        # Declaration of variables
        self.minute=StringVar()
        self.second=StringVar()
        
        # setting the default value as 0
        self.minute.set("00")
        self.second.set("00")
        
        # Use of Entry class to take input from the user
        minuteLabel= Label(self, width=3, textvariable=self.minute)
        minuteLabel.pack()
        
        secondLabel= Label(self, width=3, textvariable=self.second)
        secondLabel.pack()

        self.pack()


    def setTimer(self, minute, second):
        temp =  int(minute)*60 + int(second)
        if temp >-1:
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            mins,secs = divmod(temp,60)
    
            # using format () method to store the value up to
            # two decimal places
            self.minute.set("{0:2d}".format(mins))
            self.second.set("{0:2d}".format(secs))
    
            # updating the GUI window 
            self.update()

            if secs == 0:
                mins -= 1
                secs = 59
            else:
                secs -= 1

            if not self.stop:
                self.after(1000, self.setTimer, mins, secs)
        else:
            self.parent.gameEnd(False)

    def startTimer(self, minute, second):
        self.stop = False
        self.setTimer(minute, second)

    def stopTimer(self):
        self.stop = True
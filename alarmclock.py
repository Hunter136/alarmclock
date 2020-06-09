from tkinter import *
import datetime
from datetime import datetime
import winsound
import time

class alarmclock():#makes a gui alarm clock
    def __init__(self, alarmtime = None, entry1 = None, datetime = None, check = None, gui = None , frametop = None, framebot = None):
        self.gui = gui
        self.label = []
        self.frametop = frametop
        self.framebot = framebot
        self.button = []
        self.check = check
        self.datetime = datetime
        self.entry1 = entry1
        self.alarmtime = alarmtime
    def openWindow(self):
        self.gui = Tk()

    def looper(self):#can use pack but grid is better pack is like pack(fill = BOTH
        self.gui.mainloop()

    def labelmaker(self):
        self.label.append(Label(self.frametop, text = 'ALARM CLOCK: '))
        self.entrytime = Entry(self.gui)#making entry for time
        self.entrytime.grid(row = 0, column =1)#placing entry

    def frame(self):
        try:
            self.frametop = Frame(self.gui, width = 300, height = 250)#, bg ='cyan', width= 450, height = 50
            self.frametop.grid(row = 0, sticky ="ew")#use direcitons for teh sticky north east west south
            self.framebot = Frame(self.gui, width = 300, height = 250)
            self.framebot.grid(row = 1, sticky = "ew")
        except ValueError:
            print(ValueError, 'the gui is messed up')

    def settime(self, event):#setting time for alarm
        self.label.append(Label(self.gui, text = "Setting Time"))
        self.label[1].grid(row =4, column =0)
        try:
            time = self.entrytime.get()
            print(time)
            print(datetime.now())
            self.alarmtime = datetime.strptime(time, '%m/%d/%Y %H:%M:%S')
        except ValueError:
            print(ValueError, 'Their is no entry to get')
        #date = int(input("type year,month, day, hour, minute, and second").split())
        #self.datetime = datetime.datetime(date)
        
    def setalarm(self, event):#setting alarm to countdown to settime
        self.label.append(Label(self.gui, text = "Alarm Set"))
        self.label[2].grid(row = 5, column =0 )
        value = self.alarmtime - datetime.now()
        print(value)
        while value.total_seconds() > 0:
            value = self.alarmtime - datetime.now()
            print(value)
            print("SLEEPING")
            time.sleep(5)
        #duration = 1000  # milliseconds
       # freq = 440  # Hz
        #winsound.Beep(freq, duration)
        print("WAKEUP")
        #put flashing screen on gui

    def buttonmaker(self):
        button1 = Button(self.frametop, text = "set this alarm", fg = "red")#fg is forground
        button2 = Button(self.frametop, text = "set alarm Time", fg = "blue")
        quitter = Button(self.framebot, text = "quit", fg = "green", command = self.gui.quit)
        self.button.append(button1)
        self.button.append(button2)
        self.button.append(quitter)

    def checker(self):
        self.check = Checkbutton(self.gui, text="continuous alarm")

    def grid(self):
        try:
            self.label[0].grid(row=0, sticky = "ew")
            self.framebot.grid(row=1, sticky="ew")
            self.gui.grid_rowconfigure(1, weight=1)
            self.gui.grid_columnconfigure(0, weight=1)
            self.button[0].grid(row=1, column=0)
            self.button[1].grid(row=2, column=0)
            self.button[2].grid(row=3, column =0)
            self.button[0].bind("<Button-1>", self.setalarm)
            self.button[1].bind("<Button-1>", self.settime)
       # self.button[2].bind("<Button-1>")
            self.check.grid(columnspan=2)
        except ValueError:
            print(ValueError, "these grids are messed up!")

def main():
        print(type(datetime.now()))
        obj = alarmclock()
        obj.openWindow()
        obj.checker()
        obj.frame()
        obj.labelmaker()
        obj.buttonmaker()

        obj.grid()
        obj.looper()
main()

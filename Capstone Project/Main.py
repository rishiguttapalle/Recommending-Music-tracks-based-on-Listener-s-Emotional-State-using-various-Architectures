import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm

import TrainVGG16 as esvgg
import Train_resnet50 as esresnet
import TrainDENSENET as esdensenet
import TrainMobilenet as esmobilnet
import Trainxceptionnet as esxception


import real_time_video as real


bgcolor="#16576F"
bgcolor1="#16576F"
fgcolor="#FFFFFF"

window = tk.Tk()
window.title("Emotion Based Music prediction")
filename = ImageTk.PhotoImage(Image.open("1.jpg"))
background_label = tk.Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.pack()

window.geometry('1280x720')
window.configure(background=bgcolor)
#window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
	

message1 = tk.Label(window, text="Emotion Based Music prediction" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=2,font=('times', 25, 'italic bold underline')) 
message1.place(x=100, y=10)









def VGG16Training():
        esvgg.process()
        tm.showinfo("Input", "VGG16 Training Successfully Finished")
def RESNET50Training():
        esresnet.process()
        tm.showinfo("Input", "RESNET Training Successfully Finished")

def MOBILENETTraining():
        esmobilnet.process()
        tm.showinfo("Input", "MOBILENET Training Successfully Finished")
def DENSENETTraining():
        esdensenet.process()
        tm.showinfo("Input", "DENSENET Training Successfully Finished")
def XCEPTIONNETTraining():
        esxception.process()
        tm.showinfo("Input", "XCEPTION Training Successfully Finished")
def realpred():
        real.process()





	 
proc = tk.Button(window, text="VGG16", command=VGG16Training  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
proc.place(x=740, y=100)

proc2 = tk.Button(window, text="RESNET50", command=RESNET50Training  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
proc2.place(x=740, y=200)


proc4 = tk.Button(window, text="MOBILENET", command=MOBILENETTraining  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
proc4.place(x=740, y=300)

proc5 = tk.Button(window, text="DENSENET", command=DENSENETTraining  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
proc5.place(x=740, y=400)

proc6 = tk.Button(window, text="XCEPTIONNET", command=XCEPTIONNETTraining  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
proc6.place(x=1040, y=100)
proc7 = tk.Button(window, text="REALTIME PREDICTION", command=realpred ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=2 ,activebackground = "Red" ,font=('times', 15, ' bold '))
proc7.place(x=1040, y=200)


	
quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
quitWindow.place(x=1040, y=300)

window.mainloop()


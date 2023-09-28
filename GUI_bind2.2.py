# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:40:52 2023

@author:Xudoyberdiyev Jamshid
"""
from tkinter import *

window=Tk()
canvas=Canvas(window,width=500,height=500)
canvas.pack()
carimage=PhotoImage(file='C:\\Users\\User\\Desktop\\car.png')
myimage=canvas.create_image(0,0,carimage)
window.mainloop()

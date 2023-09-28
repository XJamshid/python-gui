# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 16:06:20 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import *
import time
window=Tk()
xvelocity=3
yvelocity=2
space=PhotoImage(file='C:\\Users\\User\\Desktop\\space.png')
ufo=PhotoImage(file='C:\\Users\\User\\Desktop\\ufo.png')
x=space.width()
y=space.height()

x1=ufo.width()/2
y1=ufo.height()/2
canvas=Canvas(window,width=x,height=y)
canvas.pack()
canvas.create_image(0,0,image=space,anchor=NW)
myimage=canvas.create_image(x1,y1,image=ufo)
while True:
    coordinates=canvas.coords(myimage)
    print(coordinates)
    if coordinates[0]>=x-x1 or coordinates[0]<0+x1:
        xvelocity=-xvelocity
    if coordinates[1]>=y-y1/2 or coordinates[1]<0+y1/2:
        yvelocity=-yvelocity
    canvas.move(myimage,xvelocity,yvelocity)
    window.update()
    time.sleep(0.01)
window.mainloop()

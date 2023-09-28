# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:15:55 2023

@author: Xudoyberdiyev Jamshid
"""

from tkinter import *
def move_up(event):
    canvas.move(myimage,0,-10)
    #y=label.winfo_y()-10
    #label.place(y=y)
def move_down(event):
    canvas.move(myimage,0,10)
    #y=label.winfo_y()+10
    #label.place(y=y)
def move_left(event):
    canvas.move(myimage,-10,0)
    #x=label.winfo_x()-10
    #label.place(x=x)
def move_right(event):
    canvas.move(myimage,10,0)
    #x=label.winfo_x()+10
    #label.place(x=x)
window=Tk()

window.bind('<w>',move_up)
window.bind('<s>',move_down)
window.bind('<a>',move_left)
window.bind('<d>',move_right)
carimage=PhotoImage(file='C:\\Users\\User\\Desktop\\car.png')
#x=carimage.width()/2
#y=carimage.height()/2
canvas=Canvas(window,width=500,height=500)
canvas.pack()
myimage=canvas.create_image(0,0,image=carimage,anchor=NW)
#label=Label(window,image=carimage)
#label.place(x=0,y=0)
window.mainloop()

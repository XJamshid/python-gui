# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 16:17:09 2023

@author: User
"""
from tkinter import *
#def do(event):
 #   label.config(text=event.keysym)

def drag_start(event):
    widget=event.widget
    widget.startX=event.x
    print(event.x)
    widget.startY=event.y
    #print(label1.startX)
def drag_motion(event):
    widget=event.widget
    x=widget.winfo_x()-widget.startX+event.x
    print(label1.winfo_x())
    y=widget.winfo_y()-widget.startY+event.y
    widget.place(x=x,y=y)
window=Tk()
#window.bind('<Key>',do)
#label=Label(window,text='Press any key',font=('Georgia',20,'bold'))
#label.pack()
label1=Label(window,bg='red',width=10,height=5)
label1.place(x=0,y=0)
label1.bind('<Button-1>',drag_start)
label1.bind('<B1-Motion>',drag_motion)
window.mainloop()

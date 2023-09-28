# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:23:05 2023

@author: Xudoyberdiyev Jamshid
"""

from tkinter import *
def new_window():
    #new_window=Toplevel()
    new_window=Tk()
    window.destroy()
    frame=Frame(new_window,bg='pink',bd=5,relief=SUNKEN,padx=15,pady=15)
    frame.pack()
    Button(frame,text='W',font=('Consolas',25),width=3).pack(side=TOP)
    Button(frame,text='A',font=('Consolas',25),width=3).pack(side=LEFT)
    Button(frame,text='S',font=('Consolas',25),width=3).pack(side=LEFT)
    Button(frame,text='D',font=('Consolas',25),width=3).pack(side=LEFT)
    new_window.mainloop()
    
window=Tk()
Button(window,text='create new window',command=new_window).pack()
window.mainloop()
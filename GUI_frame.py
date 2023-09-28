# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 10:07:27 2023

@author: Xudoyberdiyev Jamshid
"""

from tkinter import *
window=Tk()
frame=Frame(window,bg='pink',bd=5,relief=SUNKEN,padx=15,pady=15)
frame.place(x=0,y=0)
Button(frame,text='W',font=('Consolas',25),width=3).pack(side=TOP)
Button(frame,text='A',font=('Consolas',25),width=3).pack(side=LEFT)
Button(frame,text='S',font=('Consolas',25),width=3).pack(side=LEFT)
Button(frame,text='D',font=('Consolas',25),width=3).pack(side=LEFT)
window.mainloop()

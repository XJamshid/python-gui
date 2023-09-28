# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 09:57:17 2023

@author: Xdoyberdiyev Jamshid
"""
from tkinter import *
from tkinter import colorchooser as cch
def choosingcolor():
    color=cch.askcolor()
    colorHex=color[1]
    text.config(bg=colorHex)
def submit():
    info=text.get('1.0',END)
    print(info)
window=Tk()

text=Text(window,
          font=('Impact',25),
          height=10,
          width=20,
          padx=20,
          pady=20)
text.pack()
colorchoosingbutton=Button(window, text="Choosing color",command=choosingcolor)
colorchoosingbutton.pack()
submit=Button(window,text="submit",command=submit)
submit.pack()

window.mainloop()
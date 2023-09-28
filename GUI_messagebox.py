# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:35:35 2023

@author: XUdoyberdiyev Jamshid
"""
from tkinter import *
from tkinter import messagebox as mb

def click():
    answer=mb.askyesnocancel(title="Ask yes no cancel",message="Do you continue",icon='warning')
    if answer:
        print('You continued')
    elif answer==None:
        print('Thanks')
    else:
        print('You didn\'t continue')
window=Tk()

button=Button(window,text='Click me!' , command=click)
button.pack()

window.mainloop()
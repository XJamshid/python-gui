# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 16:13:47 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import *
from time import*
def update():
    time=strftime('%I:%M:%S:%p')
    time_label.config(text=time)
    window.after(1000,update)
window=Tk()
time_label=Label(window,
                 bg='black',
                 fg='#00FF00',
                 font=('Times New Roman',100),
                 relief=RAISED,
                 bd=5,
                 padx=10,
                 pady=10)
time_label.pack()
update()
window.mainloop()

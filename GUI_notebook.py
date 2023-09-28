# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 16:37:45 2023

@author: User
"""

from tkinter import *
from tkinter import ttk

window=Tk()

notebook=ttk.Notebook(window)
tab1=Frame(notebook,bg='pink')
tab2=Frame(notebook,bg='black')
notebook.add(tab1, text='Tab1')
notebook.add(tab2, text='Tab2')
notebook.pack(expand=True,fill='both')
Label(tab1,text='Hello, this is tab#1',width=50,height=25,fg='green').pack()
Label(tab2,text='Hello, this is tab#2',width=50,height=25,fg='green').pack()
window.mainloop()
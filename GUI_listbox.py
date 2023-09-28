# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 15:40:25 2023

@author:    xudoyberdiyev Jamshid
"""

from tkinter import *

def submit():
    food=[]
    if listbox.curselection():
        for index in listbox.curselection():
            food.insert(index,listbox.get(index))
        print('You ordered: ')
        for index in food:
            print(index)
        
def add():
    a=entry.get()
    if a:
        listbox.insert(listbox.size(),a)
        listbox.config(height=listbox.size())
def delete():
    if listbox.curselection():
        for index in reversed(listbox.curselection()):
            listbox.delete(index)
            listbox.config(height=listbox.size())
window=Tk()
listbox=Listbox(window,
                width=18,
                font=('Aharoni',20),
                bg="black",
                fg='green',
                selectbackground='black',
                selectforeground="red",
                selectmode=MULTIPLE)
food=['pizza','pasta','garlick bread','soup','salad']
for i in range(len(food)):
    listbox.insert(i,food[i])

listbox.config(height=listbox.size())
listbox.pack()

entry=Entry(window)
entry.pack()
submitbutton=Button(window,
                    text='submit',
                    command=submit)
submitbutton.pack()
addbutton=Button(window,
                    text='add',
                    command=add)
addbutton.pack()
deletebutton=Button(window,
                    text='delete',
                    command=delete)
deletebutton.pack()

window.mainloop()
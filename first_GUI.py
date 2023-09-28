# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 15:42:40 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import*

def submit():
    username=entry.get()
    print('Hello '+ username.title())
def delete():
    entry.delete(0,END)
def backspace():
    entry.delete(len(entry.get())-1,END)
window=Tk()

window.geometry('800x400')
window.title('My first GUI program ')
window.config(background='#9ad6d2')
icon=PhotoImage(file='C:\\Users\\User\\Desktop\\logo.png')
window.iconphoto(False,icon)
photo=PhotoImage(file='C:\\Users\\User\\Desktop\\doc.png')
label=Label(window,
            text='My first GUI programm',
            font=('Georgia',20,'bold'),
            fg='#42858c',
            bg='#86d179',
            relief=RAISED,
            bd=4,
            padx=20,
            pady=20,
            image=photo,
            compound='bottom')
label.pack(side=TOP)
entry=Entry(window,
            font=('Arial',20),
            fg='#00FF00',
            bg='black',
            relief=RAISED,
            bd=3
            )
entry.pack(side=LEFT)
submit_button=Button(window,
                     text='submit',
                     fg='#00FF00',
                     bg='black',
                     relief=RAISED,
                     bd=3,
                     activebackground='black',
                     activeforeground='#00FF00',
                     state=ACTIVE,
                     command=submit)
submit_button.pack(side=RIGHT)
delete_button=Button(window,
                     text='delete',
                     fg='#00FF00',
                     bg='black',
                     relief=RAISED,
                     bd=3,
                     activebackground='black',
                     activeforeground='#00FF00',
                     state=ACTIVE,
                     command=delete
                     )

delete_button.pack(side=RIGHT)
backspace_button=Button(window,
                     text='backspace',
                     fg='#00FF00',
                     bg='black',
                     relief=RAISED,
                     bd=3,
                     activebackground='black',
                     activeforeground='#00FF00',
                     state=ACTIVE,
                     command=backspace
                     )

backspace_button.pack(side=RIGHT)

window.mainloop()

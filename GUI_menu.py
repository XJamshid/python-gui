# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 18:53:44 2023

@author:Xudoyberdiyev Jamshid
"""
from tkinter import *
from tkinter import filedialog as fd
def  openfile():
    filename=fd.askopenfilename(initialdir='C:\\Users\\User\\Documents\\Python Scripts',
                             filetypes=(('Text files','*.txt'),('All files','*.*')),
                             title='Open file okay?')
    with open(filename,'r') as file:
        string=file.read()
    print(string)
def savefile():
    filename=fd.asksaveasfilename(initialdir='C:\\Users\\User\\Documents\\Python Scripts',
                               defaultextension='.txt',
                               filetypes=[('Text files','*.txt'),('All files','*.*')],
                               title='Save file okay?')
    string=str(text.get('1.0',END))
    with open(filename,'a') as file:
        file.write(string)
def copy():
    print('This file copied')
def paste():
    print('This file pasted')
def edit():
    print('This file edited')
window=Tk()
openphoto=PhotoImage(file='C:\\Users\\User\\Desktop\\open.png')
savephoto=PhotoImage(file='C:\\Users\\User\\Desktop\\save.png')
exitphoto=PhotoImage(file='C:\\Users\\User\\Desktop\\exit.png')
copyphoto=PhotoImage(file='C:\\Users\\User\\Desktop\\copy.png')
pastephoto=PhotoImage(file='C:\\Users\\User\\Desktop\\paste.png')
editphoto=PhotoImage(file='C:\\Users\\User\\Desktop\\edit.png')
menubar=Menu(window)
window.config(menu=menubar)
fileMenu=Menu(menubar,
              tearoff=0,
              font=('Constantia',10))
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open',command=openfile,image=openphoto,compound='left')
fileMenu.add_command(label='Save',command=savefile,image=savephoto,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',image=exitphoto,compound='left')
editMenu=Menu(menubar,tearoff=0,font=('Constantia',10))
menubar.add_cascade(label='Edit',menu=editMenu)
editMenu.add_command(labe='Copy',command=copy,image=copyphoto,compound='left')
editMenu.add_command(labe='Paste',command=paste,image=pastephoto,compound='left')
editMenu.add_command(labe='Edit',command=edit,image=editphoto,compound='left')
button=Button(window,
              text="openfile",
              command=openfile)
button.pack()
save=Button(window,
            text='save',
            command=savefile)
save.pack()

text=Text(window)
text.pack()

window.mainloop()
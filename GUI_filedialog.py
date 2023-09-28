# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:24:13 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import *
from tkinter import filedialog

def openfile():
    file=filedialog.askopenfilename(initialdir='C:\\Users\\User\\Documents\\Python Scripts',
                                        title='Open file',
                                        filetypes=(('Text files','*.txt'),('All files','*.*')))
    with open(file) as files:
        s=files.read()
    print(s)
def save():
    file=filedialog.asksaveasfilename(title='Save this',
                                      initialdir='C:\\Users\\User\\Documents\\Python Scripts',
                                      defaultextension='.txt',
                                      filetypes=[
                                          ('Text files','.txt'),
                                          ('HTML files','.html'),
                                          ('All files','.*')])
    filetext=str(text.get('1.0',END))
    with open(file,'a') as files:
        files.write(filetext)
    #file.write(filetext)
    #file.close()
window=Tk()

button=Button(window,
              text="openfile",
              command=openfile)
button.pack()
save=Button(window,
            text='save',
            command=save)
save.pack()

text=Text(window)
text.pack()
window.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 18:11:44 2023

@author: Xudoyberdiyev Jamshid
"""

from tkinter import *

def check():
    if x.get():
        print('You are agree!')
    else:
        print('You aren\'t agree :)')
def order():
    if y.get()==0:
        print('You order a pizza')
    elif y.get()==1:
        print('You order a hotdog')
    elif y.get()==2:
        print('You order a hamburger')
    else:
        print('You don\'t order!')

foods=['pizza','hotdog','hamburger']

window=Tk()

x=BooleanVar()

check_button = Checkbutton(window,
                           text='Are you agree this?',
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=check,
                           fg="#00FF00",
                           bg="black",
                           activeforeground="#00FF00",
                           activebackground="black",
                           font=('Arial',20),
                           padx=25,
                           pady=5)
check_button.pack(side=LEFT)

y=IntVar()

for index in range(len(foods)):
    radio_button=Radiobutton(window,
                             text=foods[index],
                             variable=y,
                             value=index,
                             command=order,
                             fg="#00FF00",
                             bg="black",
                             activeforeground="#00FF00",
                             activebackground="black",
                             font=('Arial',20),
                             padx=25,
                             pady=5,
                             indicatoron=False,
                             relief=RAISED,
                             bd=3
                             )
    radio_button.pack(anchor=W)
window.mainloop()
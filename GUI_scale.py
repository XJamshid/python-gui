# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 20:01:53 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import *

def submit():
    temperature=scale.get()
    print(f"Temperature is {temperature} degrees C")

window=Tk()
#hotImage=PhotoImage(file='C:\\Users\\User\Desktop\\hot.png'
                    
#coldImage=PhotoImage(file='C:\\Users\\User\\Desktop\\cold.png')      
#label_hot=Label(window,image=hotImage)
#label_hot.pack()
scale=Scale(window,
            from_=100,
            to=0,
            length=600,
            tickinterval=10,
            resolution=1,
            #showvalue=1,
            troughcolor='#7ae6cc',
            bg='black',
            fg='#00FF00',
            activebackground='black',
            font=('Arial',20))
scale.set((scale['from']+scale['to'])/2)
scale.pack()
#label_cold=Label(window,image=coldImage)
#label_cold.pack()
submit_button=Button(window,
                     text='submit',
                     command=submit)
submit_button.pack()
window.mainloop()
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:07:04 2023

@author: Xudoyberdiyev Jamshid
"""
from tkinter import *
import time 
from GUI_ball_class import *
WIDTH=500
HEIGHT=500
window=Tk()
canvas=Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()
volley_ball=Ball(0,0,100,canvas,'orange',2,1)
tennis_ball=Ball(0,0,25,canvas,'green',3,2)
foot_ball=Ball(0,0,123,canvas,'blue',7,5)
basket_ball=Ball(0,0,150,canvas,'red',10,8)
while True:
    volley_ball.move()
    tennis_ball.move()
    foot_ball.move()
    basket_ball.move()
    window.update()
    time.sleep(0.01)
window.mainloop()

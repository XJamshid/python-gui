# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 15:21:53 2023

@author: User
"""

class Ball():
    def __init__(self,x,y,diametr,canvas,color,xvelocity,yvelocity):
        self.x=x
        self.y=y
        self.diametr=diametr
        
        self.canvas=canvas
        self.color=color
        self.xvelocity=xvelocity
        self.yvelocity=yvelocity
        self.image=self.canvas.create_oval(self.x,self.y,self.diametr,self.diametr,fill=self.color)
    def move(self):
        coordinates=self.canvas.coords(self.image)
        if coordinates[2]>=self.canvas.winfo_width() or coordinates[0]<0:
            self.xvelocity=-self.xvelocity
        if coordinates[3]>=self.canvas.winfo_height() or coordinates[1]<0:
            self.yvelocity=-self.yvelocity
        self.canvas.move(self.image,self.xvelocity,self.yvelocity)
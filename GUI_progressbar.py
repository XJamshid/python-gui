# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:56:01 2023

@author: User
"""

from tkinter import *
from tkinter.ttk import *
import time
def start():
    GB=100
    download=0
    speed=int(1)
    while download<GB:
        time.sleep(0.05)
        bar['value']+=speed
        download+=speed
        window.update_idletasks()
window=Tk()
bar=Progressbar(window,orient=HORIZONTAL,length=300).pack(pady=10)
Button(window,text="download",command=start).pack()
window.mainloop()
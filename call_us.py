# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 22:40:43 2020

@author: Lenovo
"""
from tkinter import *
from tkinter import ttk

def met_call_us(frm):
    global root
    root=frm
    root.geometry("500x500") 
    root.title("RATE US")

        
    frame_header = ttk.Frame(root)
    frame_header.pack()
    headerlabel = ttk.Label(frame_header, text='Contact US', foreground='orange',
                        font=('Arial', 24))
    headerlabel.grid(row=0, column=1)
    messagelabel = ttk.Label(frame_header,
                         text='Give a miscall on this number:7905295216',
                         foreground='purple', font=('Arial', 10))
    messagelabel.grid(row=4, column=1)
    return
    
    
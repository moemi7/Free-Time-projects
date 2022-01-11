import tkinter as tk
from tkinter import ttk
from tkinter import *
import lijn
root = Tk()


canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
entry2 = 1
ch1 = Radiobutton(root, text="aanwezig", variable=entry2, value=True)
ch2 = Radiobutton(root,text="afwezig",variable=entry2,value=False) 
canvas1.create_window(200, 140, window=entry1)
canvas1.create_window(200, 160, window=ch1)
canvas1.create_window(200, 180, window=ch2)

label2 = tk.Label(root, text= 'Breedte')
canvas1.create_window(100, 140, window=label2)


def getval():
    lengte = int(entry1.get())
    q = entry2
    lijn.main(lengte,q)


button1 = tk.Button(text='maak de ligger', command=getval)
canvas1.create_window(200, 200, window=button1)



root.mainloop()

from tkinter import *
import tkinter as tk
from tkinter import ttk
import Test
root = Tk()
root.title("Grid_maker")
root.wm_iconbitmap('Data\Icons8-Windows-8-Data-Grid.ico')
frm = ttk.Frame(root, padding=10)

canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
entry2 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry1)
canvas1.create_window(200, 100, window=entry2)
label2 = tk.Label(root, text= 'Breedte')
canvas1.create_window(100, 140, window=label2)
label3 = tk.Label(root, text= 'Lengte')
canvas1.create_window(100, 100, window=label3)

def make_shape ():  

    x = int(entry1.get())
    y = int(entry1.get())
    
    label1 = tk.Label(root, text= 'Aan het maken')
    canvas1.create_window(200, 230, window=label1)
    Test.autocad_grid(x,y)
    
button1 = tk.Button(text='Make the shape', command=make_shape)
canvas1.create_window(200, 180, window=button1)


root.mainloop()



"""frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
"""

import sys
import os
from tkinter import *

window=Tk()

window.title("Running Python Script")
window.geometry('550x200')

def run():
    os.system('demo.py')

mb =  Menubutton ( window, text = 'text') 
mb.grid(column=0, row=0) 

btn = Button(window, text="Click Me", bg="black", fg="white",command=run)
btn.grid(column=0, row=0)
mb.pack()
window.mainloop()

import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Python GUI")



	
aLabel = tk.Label(win, text="Motor GUI")
aLabel.grid(column=0, row=0)


def clickMe():
    action.configure(text = " click")
    aLabel.configure(foreground='red')
    aLabel.configure(test='red')



action = tk.Button(win, text="Click me", command = clickMe)
action.grid(column=1,row=0)

win.mainloop()

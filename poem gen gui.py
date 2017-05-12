import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

"""One box with project description,
one box with the generated poem window,
one box with a slider from 1-10 for how how many lines,
one button that says "generate"""

class user_gui:
        def __init__(self):
                self.window = tk.Tk()
                self.create_widgets()
                
        def create_widgets(self):
                s = ttk.Style()
                s.configure('.', font=('Helvetica', 12))
                label = ttk.Label(self.window, text="Hello World")
                self.label_text = label.grid(row=0,column=0)

                """Generate button"""
                generate = ttk.Button(self.window, text="Generate", )
                generate.grid(row=1,column=0)
                #generate['command'] = self.function()

                """Quit button"""
                quit_button = ttk.Button(self.window, text="Quit")
                quit_button.grid(row=2,column=0)
                quit_button['command'] = self.window.destroy


program = user_gui()
program.window.mainloop()


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
                self.root= tk.Tk() #root is window
                self.create_widgets() #inits the gui with the create_widgets function
                
        def create_widgets(self):
                """Textbox"""
                s = ttk.Style() #using ttk style!
                s.configure('.', font=('Helvetica', 12), sticky=tk.N+tk.E+tk.S+tk.W, padx=10) #'.' is a root style; this line is used to configure an overall style
                label = ttk.Label(self.root, text="""ABOUT
This is a random poem generator created by Charlie Carlson, Iain Irwin, and Nic Hubig for the CSCI121 final project.""")
                self.label_text = label.grid(row=1, column=1, columnspan=2,)

                """Slider scale"""
                #This decides how many lines of a poem to generate
                scale = ttk.Scale(self.root, from_=1, to=100)
                scale.grid(row=2, column=1, columnspan=2, sticky=tk.N+tk.E+tk.S+tk.W, padx=10)

                """Generate button"""
                generate = ttk.Button(self.root, text="Generate poetry")
                generate.grid(row=3, column=1)
                #generate['command'] = self.function()

                """Quit button"""
                quit_button = ttk.Button(self.root, text="Quit")
                quit_button.grid(row=3, column=2)
                quit_button['command'] = self.root.destroy


program = user_gui()
program.root.mainloop()

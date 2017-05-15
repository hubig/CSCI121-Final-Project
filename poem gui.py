import tkinter as tk
from tkinter import ttk
import os

class user_gui:
        def __init__(self):
                self.create_window() #creates window with title
                self.create_widgets() #creates widgets
                
        def open_file(self):
                """opens and returns poem text"""
                f = open("Poem_Generator.txt", "r")
                poems = f.read()
                return poems

        def create_window(self):
                """creates the window."""
                self.root= tk.Tk() #creating window
                self.root.title("Poem Generator")
                
        def create_widgets(self):
                """creates all the widgets and their frames."""
                s = ttk.Style() #using ttk style
                s.configure('.', font=('Helvetica', 12), sticky=tk.N+tk.E+tk.S+tk.W)

                """ABOUT"""
                about_frame = ttk.Frame(self.root, width = 240, height = 300)
                about_frame.grid(row = 1, column = 1, sticky=tk.N+tk.E, ipadx = 10, ipady = 10)
                about_frame.columnconfigure(0, weight = 1)
                about_frame.rowconfigure(0, weight = 1)

                about_text = """ABOUT
This is a random poem generator created by Charlie Carlson, Iain Irwin, and Nic Hubig for the CSCI121 final project."""

                about_label = ttk.Label(about_frame, wraplength = 240, text = about_text)
                about_label.grid(row = 0, column = 0, sticky=tk.N+tk.E, ipadx = 10, ipady = 10)
                about_label.columnconfigure(0, weight = 1)
                about_label.rowconfigure(0, weight = 1)

                """POETRY"""
                poetry_frame = ttk.Frame(self.root, width = 240, height = 300)
                poetry_frame.grid(row = 1, column = 2)
                poetry_text = self.open_file()
                poetry_label = ttk.Label(poetry_frame, wraplength = 240, text = poetry_text)
                poetry_label.grid(row = 0, column = 0, sticky=tk.N+tk.E, ipadx = 10, ipady = 10)
                poetry_label.columnconfigure(0, weight = 1)
                poetry_label.rowconfigure(0, weight = 1)

                """GENERATE BUTTON"""
                generate = ttk.Button(self.root, text="Generate poetry")
                generate.grid(row=3, column= 1)
                generate.columnconfigure(0, weight = 1)
                generate.rowconfigure(0, weight = 1)
                #generate['command'] = self.function()

                """QUIT BUTTON"""
                quit_button = ttk.Button(self.root, text="Quit")
                quit_button.grid(row=3, column=2)
                quit_button['command'] = self.root.destroy
                
program = user_gui()
program.root.mainloop()

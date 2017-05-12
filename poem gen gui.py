import tkinter as tk
from tkinter import filedialog
import os

"""One box with project description,
one box with the generated poem window,
one box with a slider from 1-10 for how how many lines,
one button that says "generate"""

#create app window
window = tk.Tk()

#Build a list of tuples for each file type the file dialog should display
my_filetypes = [('all files', '.*'), ('text files', '.txt')]

#Ask user to select a file
#answer = filedialog.askopenfilename(parent=window, initialdir=os.getcwd(),title="Please select a file:",filetypes=my_filetypes)


#create user interface
#my_label = tk.Label(window, text="Hello World!")
#my_label.grid(row=1, column=1)

generate = tk.Button(window, text="Generate")
generate.grid(row=1, column= 0)
#generate['command'] =

quit_button = tk.Button(window, text="Quit")
quit_button.grid(row=2,column=0)
quit_button['command'] = window.destroy

#Start GUI loop
window.mainloop()

import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

bg_colour = "#FBE870"

# window
root = tk.Tk()
root.title("Recipe Picker")

# place app in center of the screen
root.eval("tk::PlaceWindow . center") 

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)

# run app
root.mainloop()

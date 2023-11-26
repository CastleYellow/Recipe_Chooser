import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random
import Functions
import Database

bg_colour = "#FBE870"
button_colour = "#1f5b22"

# window
root = tk.Tk()
root.title("Recipe Picker")

# place app in center of the screen
root.eval("tk::PlaceWindow . center") 

# create a frame widget
frame1 = tk.Frame(root, width=500, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)
frame3 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0)

button_add_recipe = tk.Button(
        frame3,
        text="ADD RECIPE",
        font=("TkHeadingFont", 20),
        bg=button_colour,
        fg="white",
        cursor="hand2",
        activebackground="#badee2",
        activeforeground="black",
        command=lambda:Functions.open_enter_window()
        ).pack(pady=10)

# run app
root.mainloop()

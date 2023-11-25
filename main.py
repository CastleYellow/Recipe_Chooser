import tkinter as tk
from PIL import ImageTk
import sqlite3
from numpy import random

bg_colour = "#FBE870"
button_colour = "#1f5b22"

# window
root = tk.Tk()
root.title("Recipe Picker")

def open_enter_window():
    enter_Window = tk.Toplevel(root)
    enter_Window.title("Enter new Recipes")
    
    frame_eW1 = tk.Frame(enter_Window, width=400, height=600,bg=bg_colour)
    frame_eW1.grid(row=0,column=0)

    label_title = tk.Label(frame_eW1,
                           text="Enter a new recipe to the database!",
                           font=("TkHeadingFont", 15),
                           fg="black",
                           bg=bg_colour
                           ).grid(row=0, column=0, pady=15)

    label_recipe = tk.Label(frame_eW1,
                            text="Recipe Name:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=1, column=0, padx=5,pady=5, sticky="W")
    label_ingredient1 = tk.Label(frame_eW1,
                            text="Ingredient 1:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=2, column=0, padx=5,pady=5, sticky="W")
    label_ingredient2 = tk.Label(frame_eW1,
                            text="Ingredient 2:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=3, column=0, padx=5,pady=5, sticky="W")
    label_ingredient3 = tk.Label(frame_eW1,
                            text="Ingredient 3:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=4, column=0, padx=5,pady=5, sticky="W")
    label_ingredient4 = tk.Label(frame_eW1,
                            text="Ingredient 4:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=5, column=0, padx=5,pady=5, sticky="W")
    label_ingredient5 = tk.Label(frame_eW1,
                            text="Ingredient 5:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=6, column=0, padx=5,pady=5, sticky="W")
    label_ingredient6 = tk.Label(frame_eW1,
                            text="Ingredient 6:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=7, column=0, padx=5,pady=5, sticky="W")
    label_recipe_book = tk.Label(frame_eW1,
                            text="Recipe Book\n(incl. page):",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=8, column=0, padx=5,pady=5, sticky="W")
    label_recipe_link = tk.Label(frame_eW1,
                            text="Link to Recipe:",
                            font=("TkMenuFont", 10),
                            fg="black",
                            bg=bg_colour).grid(row=9, column=0, padx=5,pady=5, sticky="W")



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
        command=lambda:open_enter_window()
        ).pack(pady=10)

# run app
root.mainloop()

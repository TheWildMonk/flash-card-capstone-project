# Libraries
from tkinter import *

# Color
BACKGROUND_COLOR = "#B1DDC6"

# Font
LANGUAGE_FONT = ("Raleway", 40, "italic")
WORD_FONT = ("Raleway", 60, "bold")

# Window object definition
root = Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
root.resizable(width=False, height=False)

# Canvas object definition
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=bg_image)
canvas.grid(row=0, column=0, columnspan=2)

# Labels
language = Label(text="French", font=LANGUAGE_FONT, bg="white", highlightthickness=0)
word = Label(text="trouve", font=WORD_FONT, bg="white", highlightthickness=0)

# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0)
left_button_img = PhotoImage(file="images/wrong.png")
left_button = Button(image=left_button_img, highlightthickness=0)


# Grids
language.grid(row=0, column=0, columnspan=2, sticky="n", pady=150)
word.grid(row=0, column=0, columnspan=2, pady=263)
right_button.grid(row=1, column=1)
left_button.grid(row=1, column=0)

# Window mainloop
root.mainloop()
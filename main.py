# Libraries
from tkinter import *
from random import *
import pandas as pd

# Color
BACKGROUND_COLOR = "#B1DDC6"

# Font
LANGUAGE_FONT = ("Raleway", 40, "italic")
WORD_FONT = ("Raleway", 60, "bold")

# Read csv data
df_word = pd.read_csv("data/french_words.csv")
word_dict = df_word.to_dict(orient="records")


# Generate new word
def new_card():
    current_card = choice(word_dict)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"].title())


# Window object definition
root = Tk()
root.title("Flash Card")
root.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
root.resizable(width=False, height=False)

# Canvas object definition
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
bg_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=bg_image)
card_title = canvas.create_text(400, 150, text="Title", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="Word", font=WORD_FONT)

print()
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_button_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=new_card)
wrong_button_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=new_card)


# Grids
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

# Initial run of the app
new_card()

# Window mainloop
root.mainloop()
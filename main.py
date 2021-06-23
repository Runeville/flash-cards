from tkinter import *
from tkinter import messagebox
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("words.csv")
data = data.to_dict(orient='records')
new_word = choice(data)


def next_word(right_answer=False):
    global new_word
    try:
        new_word = choice(data)
    except IndexError:
        messagebox.showinfo(title='Message', message='No more words')
    else:
        if right_answer:
            data.remove(new_word)
        canvas.itemconfig(canvas_image, image=card_front_image)
        canvas.itemconfig(word_label, text=new_word['english'], fill='black')
        canvas.itemconfig(language_label, text="English", fill='black')
        window.after(3000, func=show_translation)


def wrong_answer():
    next_word()


def right_answer():
    next_word(True)


def show_translation():
    canvas.itemconfig(canvas_image, image=card_back_image)
    canvas.itemconfig(word_label, text=new_word['russian'], fill='white')
    canvas.itemconfig(language_label, text="Russian", fill='white')


# ------------------ GUI ------------------------------------ #
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_image = PhotoImage(file='./images/card_back.png')
card_front_image = PhotoImage(file='./images/card_front.png')

canvas_image = canvas.create_image(400, 260, image=card_front_image)
canvas.grid(column=0, row=0, columnspan=2)

# Labels
language_label = canvas.create_text(400, 150, text="English", fill='black', font=('ariel', 35, 'italic'))
word_label = canvas.create_text(400, 256, text="Word", fill='black', font=('ariel', 45, 'bold'))

# Buttons
wrong_image = PhotoImage(file='./images/wrong.png')
right_image = PhotoImage(file='./images/right.png')

wrong_button = Button(image=wrong_image, highlightthickness=0, borderwidth=0, command=wrong_answer)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, highlightthickness=0, borderwidth=0, command=right_answer)
right_button.grid(column=1, row=1)

next_word()
window.after(3000, func=show_translation)

window.mainloop()

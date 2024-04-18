from tkinter import *
from customtkinter import *
from tkinter import messagebox
import random
import time

root = CTk()
root.title('Color Game')
root.geometry('600x500')
root.resizable(False, False)

colors = ["blue", "green", "red", "yellow", "orange", "purple", "brown", "pink"]
text = ["red", "green", "blue", "yellow", "orange", "purple", "brown", "pink"]

time_left = 30
score = 0


def startgame():
    if time_left == 30:
        timer()
    colors_()


def colors_():
    global score
    global time_left

    if time_left > 0:
        input_entry.focus_set()
        if input_entry.get().lower() == colors[1].lower():
            score += 1
        input_entry.delete(0, END)
        random.shuffle(colors)
        text_label.configure(text_color=str(colors[1]), text=str(colors[0]))
        press_enter_label.configure(text="Score: " + str(score))
        input_entry_label.configure(text="Press Enter to Submit the color")


def timer():
    global time_left
    if time_left > 0:
        time_left -= 1
        time_left_label.configure(text=f"Time left: {time_left}")
        if time_left == 0:
            messagebox.showinfo("Game Over", f"Time is Over, your score was {score}")
        root.after(1000, timer)


hint_text_label = CTkLabel(root, text='Color game\nEnter color of the text not text itself!', font=('Helvetica', 20),
                           fg_color="#f1ef75", corner_radius=10)
hint_text_label.pack(padx=5, pady=10)

press_enter_label = CTkLabel(root, text='Press Space to Start', font=('Helvetica', 20))
press_enter_label.place(relx=0.5, rely=0.2, anchor='center')

time_left_label = CTkLabel(root, text='Time Left: 30', font=('Helvetica', 20))
time_left_label.place(relx=0.5, rely=0.28, anchor='center')

text_label = CTkLabel(root, text='', font=('Helvetica', 40))
text_label.place(relx=0.5, rely=0.55, anchor='center')

input_entry = CTkEntry(root, font=('Helvetica', 20), corner_radius=10, placeholder_text='Color of text', width=250,
                       border_color="#57adcc")
input_entry.place(relx=0.5, rely=0.8, anchor='center')

input_entry_label = CTkLabel(root, text='', font=('Helvetica', 15))
input_entry_label.place(relx=0.5, rely=0.87, anchor='center')

input_entry.bind("<Return>", lambda e: colors_())

root.bind("<space>", lambda e: startgame())

input_entry.focus_set()

root.mainloop()

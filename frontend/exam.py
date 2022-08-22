from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime
from solutions.answers import Answers as data


win = Tk()
win.title("Basic Circuit Quiz")
win.minsize(width=500, height=370)
win.maxsize(width=500, height=370)
win.config(padx=50, pady=50)

def display_exam_one():
    start_button.destroy()
    given = data.answers_for_problem_one()
    

# START EXAM BUTTON
start_button = Button(win, text="Start Exam", style="W.TButton", command=display_exam_one)
start_button.pack(pady=(20, 0), ipadx=10, ipady=10)

win.mainloop()
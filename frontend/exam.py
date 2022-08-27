from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime
from solutions.answers import Answers as data
# from PIL import Image, ImageTk


win = Tk()
win.title("Basic Circuit Quiz")
win.minsize(width=1200, height=680)
win.state('zoomed')
win.configure(bg='white')
win.config(padx=50, pady=50)

def display_exam_one():
    start_button.destroy()

    #DISPLAY IMAGE FOR CIRCUIT 1
    canvas.grid(column=0, row=0, columnspan = 2, sticky="n")
    
    given = data.answers_for_problem_one()

    
    
    given_label.config(text=f"GIVEN:\n\tV1: {given['voltage']} Volts\n\tR1: {given['res_one']} Ohms\n\tR2: {given['res_two']} Ohms\n\tR3: {given['res_three']} Ohms")
    given_label.grid(column=2, row=0, sticky="w")

    question.grid(column=0, row=1, sticky="nw", pady=(5,30))
    question_one.grid(column=0, row=2, sticky="w")
    question_two.grid(column=0, row=3, sticky="w")
    question_three.grid(column=0, row=4, sticky="w")
    question_four.grid(column=0, row=5, sticky="w")
    question_five.grid(column=0, row=6, sticky="w")


# SET IMAGE FOR CIRCUIT 1
canvas = Canvas(width=630, height=226, highlightthickness=0)
img_one = PhotoImage(file="1.png")
canvas.create_image(315, 113, image=img_one)

# CIRCUIT 1 QUESTION LABEL
given_label = Label(font=("Courier", 12), background="white")
question = Label(text="1.) Determine the following quantities for the given circuit above.", 
    font=("Courier", 12), 
    background="white",
    wraplength=500)
question_one = Label(text="a.) the equivalent resistance", 
    font=("Courier", 12), 
    background="white",
    wraplength=500)
question_two = Label(text="b.) the current from the power supply", 
    font=("Courier", 12), 
    background="white",
    wraplength=500)
question_three = Label(text="c.) the current through each resistor", 
    font=("Courier", 12), 
    background="white",
    wraplength=500)
question_four = Label(text="d.) the voltage drop across each resistor", 
    font=("Courier", 12), 
    background="white",
    wraplength=500)
question_five = Label(text="e.) the power dissipated in each resistor", 
    font=("Courier", 12), 
    background="white",
    wraplength=500)



# START EXAM BUTTON
start_button = Button(win, text="Start Exam", style="W.TButton", command=display_exam_one)
start_button.pack(pady=(20, 0), ipadx=10, ipady=10)


win.mainloop()
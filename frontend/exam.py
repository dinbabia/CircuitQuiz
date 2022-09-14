from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime
from turtle import bgcolor
from solutions.answers import Answers as data
from functools import partial

TIME_LIMIT = 5 # Time in Decimal Format
timer = None

win = Tk()
win.title("Basic Circuit Quiz")
win.minsize(width=1200, height=680)
win.state('zoomed')
win.configure(bg='white')
win.config(padx=50, pady=50)

class QuestionLabel(Label):
    '''
    A customized Label from Tkinter specific for questions label.
    '''
    def __init__(self, text=None) -> None:
        super().__init__(text=text, 
            font = ("Courier", 12),
            background="white",
            wraplength=500)


       
      
    

def display_timer(count):
    minute = int(count/60)
    seconds = int(count  % 60)
    min_format = minute if minute >= 10 else f"0{minute}"
    secs_format = seconds if seconds >= 10 else f"0{seconds}"
    timer_label.config(text = f"{min_format}:{secs_format}")
    if count > 0:
        global timer
        timer = win.after(1000, display_timer, count -1)

def display_exam_one():
    start_button.destroy()
    # DISPLAY TIME
    display_timer(TIME_LIMIT * 60)
    timer_label.grid(column=4, row=0, sticky="e")

    # DISPLAY IMAGE FOR CIRCUIT 1
    canvas.grid(column=0, row=1, columnspan = 4, sticky="n")
    
    answers = data.answers_for_problem_one()
    given_label.config(text=f"GIVEN:\n\tV1: {answers['given']['voltage']} Volts\n\tR1: {answers['given']['res_one']} Ω\n\tR2: {answers['given']['res_two']} Ω\n\tR3: {answers['given']['res_three']} Ω")
    given_label.grid(column=5, row=1, sticky="w")

    exam_one_question.grid(column=0, row=2, sticky="nw", pady=(5,30))

    # QUESTION 1
    exam_one_question_one.grid(column=0, row=3, sticky="w")
    exam_one_answer_one.grid(column=1, row=3, sticky="w", padx=0)
    exam_one_check_one_btn.config(command=lambda: check_answer(exam_one_answer_one, correct_ans=answers['res_total'], btn=exam_one_check_one_btn))
    exam_one_check_one_btn.grid(column=2, row=3, sticky="w", padx=0)

    # QUESTION 2
    exam_one_question_two.grid(column=0, row=4, sticky="w")
    exam_one_answer_two.grid(column=1, row=4, sticky="w", padx=0)
    exam_one_check_two_btn.config(command=lambda: check_answer(exam_one_answer_two, correct_ans=answers['current_total'], btn=exam_one_check_two_btn))
    exam_one_check_two_btn.grid(column=2, row=4, sticky="w", padx=0)

    # QUESTION 3
    exam_one_question_three.grid(column=0, row=5, sticky="w")
    exam_one_answer_three_i.grid(column=1, row=6, sticky="w", padx=0)
    exam_one_answer_three_ii.grid(column=1, row=7, sticky="w", padx=0)
    exam_one_answer_three_iii.grid(column=1, row=8, sticky="w", padx=0)

    exam_one_question_three_i.grid(column=0, row=6, sticky="e", padx=10)
    exam_one_question_three_ii.grid(column=0, row=7, sticky="e", padx=10)
    exam_one_question_three_iii.grid(column=0, row=8, sticky="e", padx=10)

    exam_one_check_three_btn_i.config(command=lambda: check_answer(exam_one_answer_three_i, correct_ans=answers['current_total'], btn=exam_one_check_three_btn_i))
    exam_one_check_three_btn_i.grid(column=2, row=6, sticky="w", padx=0)
    exam_one_check_three_btn_ii.config(command=lambda: check_answer(exam_one_answer_three_ii, correct_ans=answers['current_total'], btn=exam_one_check_three_btn_ii))
    exam_one_check_three_btn_ii.grid(column=2, row=7, sticky="w", padx=0)
    exam_one_check_three_btn_iii.config(command=lambda: check_answer(exam_one_answer_three_iii, correct_ans=answers['current_total'], btn=exam_one_check_three_btn_iii))
    exam_one_check_three_btn_iii.grid(column=2, row=8, sticky="w", padx=0)

    # QUESTION 4
    # exam_one_question_four.grid(column=0, row=6, sticky="w")

    
    # exam_one_question_five.grid(column=0, row=7, sticky="w")
    

def check_answer(input, correct_ans,btn):
    test = input.get()
    if test == str(correct_ans):
        btn.config(text="Correct", style="G.TButton",state="disabled")
        input.config(state="disabled")
    else:
        btn.config(text="Wrong", style="R.TButton",state="disabled")
        input.config(state="disabled")
      
        
    
        
# Button STYLES
st = Style()
st.configure('G.TButton',  background="green", font=('Arial', 8 ,'bold', 'underline'))
st.configure('R.TButton',  background="red", font=('Arial', 8 ,'bold', 'underline'))

# TIMER LABEL
timer_label = Label(text="00:00", 
    font=("Courier", 14, "bold"), 
    background="white",
    wraplength=500)


# SET IMAGE FOR CIRCUIT 1
canvas = Canvas(width=630, height=226, highlightthickness=0)
img_one = PhotoImage(file="1.png")
canvas.create_image(315, 113, image=img_one)

# CIRCUIT 1 QUESTION LABELS
given_label = Label(font=("Courier", 12), background="white")
exam_one_question = QuestionLabel(text="1.) Determine the following quantities for the given circuit above.")
exam_one_question_one = QuestionLabel(text="a.) the equivalent resistance(Ω):")
exam_one_question_two = QuestionLabel(text="b.) the current from the power supply(A):")
exam_one_question_three = QuestionLabel(text="c.) the current through each resistor(A)")
exam_one_question_three_i = QuestionLabel(text="i.) Current 1 (A):")
exam_one_question_three_ii = QuestionLabel(text="ii.) Current 2 (A):")
exam_one_question_three_iii = QuestionLabel(text="iii.) Current 3 (A):")
exam_one_question_four = QuestionLabel(text="d.) the voltage drop across each resistor(V):")
exam_one_question_five = QuestionLabel(text="e.) the power dissipated in each resistor(W)")

# CIRCUIT 1 QUESTION INPUTS

exam_one_answer_one = Entry(width=10)
exam_one_answer_two = Entry(width=10)
exam_one_answer_three_i = Entry(width=10)
exam_one_answer_three_ii = Entry(width=10)
exam_one_answer_three_iii = Entry(width=10)




# Check Button
exam_one_check_one_btn = Button(win, text="Check")
exam_one_check_two_btn = Button(win, text="Check")
exam_one_check_three_btn_i = Button(win, text="Check")
exam_one_check_three_btn_ii = Button(win, text="Check")
exam_one_check_three_btn_iii = Button(win, text="Check")


# START EXAM BUTTON
start_button = Button(win, text="Start Exam", command=display_exam_one)
start_button.pack(pady=(20, 0), ipadx=10, ipady=10)


win.mainloop()
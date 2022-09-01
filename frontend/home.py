from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from datetime import datetime
import settings



def check_form_input()-> None:
    """
    Validates the form if there are lacking inputs.
    """
    if user_name_input.get() == "" or instructors_name_input.get() == "" or year_and_section_input.get() == "":
        messagebox.showerror(title="Basic Circuit Quiz | Incomplete Form", message="Please fill up the form completely.")
    else:
        answer = messagebox.askyesno('Basic Circuit Quiz | Complete Form', f"""Do you want to proceed and take the quiz with this information?\n
\t{date["text"]}\n
Student's Name:       {user_name_input.get()}
Instructor's Name:    {instructors_name_input.get()}
Year and Section:      {year_and_section_input.get()}""")
        if answer:
            win.destroy()
            # START EXAM
            settings.init()
            import frontend.exam
            
    
    
win = Tk()
win.title("Basic Circuit Quiz")
win.minsize(width=500, height=370)
win.maxsize(width=500, height=370)
win.configure(background='white')
win.config(padx=50, pady=50)


    
# STYLES
st = Style()
st.configure('W.TButton', background='#345', foreground='green', font=('Arial', 14 ))

# WELCOME NOTE
welcome_note = Label(text="Fill up the form before starting the quiz.", font=("Times New Roman", 15, "bold"), background="white")
welcome_note.grid(column=2, row=4, columnspan = 2, pady=(0, 30))

# DATE
date = Label(text=f"Date: {datetime.now().strftime('%B %d, %Y')}", font=("Courier", 12, "bold"), background="white")
date.grid(column=2, row=5,  columnspan = 2,pady=(0, 20))

# USER NAME
user_name_label = Label(text="Student's Name:", font=("Courier", 12, "bold"), background="white")
user_name_label.grid(column=2, row=6, sticky = "w")

user_name_input = Entry( width=30)
user_name_input.grid(column=3, row=6, padx=(20, 0))


# INSTRUCTOR'S NAME
instructors_name_label = Label(text="Instructor's Name:", font=("Courier", 12, "bold"), background="white")
instructors_name_label.grid(column=2, row=7 , pady=(20, 0), sticky = "w")

instructors_name_input = Entry(width=30)
instructors_name_input.grid(column=3, row=7, padx=(20, 0), pady=(10, 0))

# YEAR AND SECTION
year_and_section_label = Label(text="Year and Section:", font=("Courier", 12, "bold"), background="white")
year_and_section_label.grid(column=2, row=8 , pady=(20, 0), sticky = "w")

year_and_section_input = Entry(width=30)
year_and_section_input.grid(column=3, row=8, padx=(20, 0), pady=(10, 0))

# START BUTTON
start_button = Button(win, text="Start", style="W.TButton", command=check_form_input)
start_button.grid(column=2, row=9, columnspan = 2, pady=(20, 0), ipadx=10, ipady=10)


win.mainloop()
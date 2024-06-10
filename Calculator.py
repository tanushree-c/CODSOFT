from tkinter import *
from tkinter import messagebox


top = Tk()
top.title("ARITHMETIC CALCULATOR")
top.geometry("400x400")
top.resizable(0, 0)

def addition():
    try:
        number1 = float(txt_number1.get())
        number2 = float(txt_number2.get())
        answer = number1 + number2
        ln_answer.config(text=f"Sum is {answer}.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")


def subtraction():
    try:
        number1 = float(txt_number1.get())
        number2 = float(txt_number2.get())
        answer = number1 - number2
        ln_answer.config(text=f"Difference is {answer}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")



def multiplication():
    try:
        number1 = float(txt_number1.get())
        number2 = float(txt_number2.get())
        answer = number1 * number2
        ln_answer.config(text=f"Product is {answer}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")


def division():
    try:
        number1 = float(txt_number1.get())
        number2 = float(txt_number2.get())
        answer = number1 / number2
        ln_answer.config(text=f"Quotient is {answer}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")


lbl_number1 = Label(top, text="First number:", font=('Sans Serif', 11))
txt_number1 = Entry(top, font=('Sans Serif', 11))

lbl_number2 = Label(top, text="Second number:", font=('Sans Serif', 11))
txt_number2 = Entry(top, font=('Sans Serif', 11))

btn_click_add = Button(top, text="Add", font=('Sans Serif', 11), command=addition)
btn_click_sub = Button(top, text="Subtract", font=('Sans Serif', 11), command=subtraction)
btn_click_mul = Button(top, text="Multiply", font=('Sans Serif', 11), command=multiplication)
btn_click_div = Button(top, text="Divide", font=('Sans Serif', 11), command=division)

ln_answer = Label(top, font=('Sans Serif', 14))


lbl_number1.grid(row=0, column=0, columnspan=2 ,padx=10, pady=10, sticky='w')
txt_number1.grid(row=0, column=2, columnspan=2 ,padx=10, pady=10, sticky='e')
lbl_number2.grid(row=1, column=0, columnspan=2 ,padx=10, pady=10, sticky='w')
txt_number2.grid(row=1, column=2, columnspan=2 ,padx=10, pady=10, sticky='e')

btn_click_add.grid(row=2, column=0, padx=10, pady=10, sticky='e')
btn_click_sub.grid(row=2, column=1, padx=10, pady=10, sticky='e')
btn_click_mul.grid(row=2, column=2, padx=15, pady=10, sticky='we')
btn_click_div.grid(row=2, column=3, padx=3, pady=10, sticky='w')

ln_answer.grid(row=3, column=0, columnspan=4, padx=10, sticky='w')

mainloop()
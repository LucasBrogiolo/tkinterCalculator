# first import tkinter
from tkinter import *

# here we create the main wndow
calc = Tk()
calc.title("Calculator")
calc.configure(background="#ffffcc")

# here to show the numbers
e = Entry(calc, width=35, borderwidth=2)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=15)


# create the functions:
def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number)) # we have to pass the string to concatenate, otherwise we will add the number with "+" operator

def button_clear():
    e.delete(0, END)

def button_dotted(dot="."):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(dot))

def button_plus():
    num1 = e.get()
    global Num
    global math
    math = "add"
    Num = float(num1)
    e.delete(0, END)

def button_sub():
    num1 = e.get()
    global Num
    global math
    math = "sub"
    Num = float(num1)
    e.delete(0, END)

def button_mul():
    num1 = e.get()
    global Num
    global math
    math = "mul"
    Num = float(num1)
    e.delete(0, END)

def button_div():
    num1 = e.get()
    global Num
    global math
    math = "div"
    Num = float(num1)
    e.delete(0, END)

def button_percent():
    num1 = e.get()
    global Num
    global math
    math = "per"
    Num = (float(num1) / 100)
    e.delete(0, END)
    e.insert(0, Num)

def button_result():
    num2 = e.get()
    global secondNumber
    secondNumber = float(num2)
    if math == "add":
        result = Num + secondNumber
    elif math == "sub":
        result = Num - secondNumber
    elif math == "div":
        result = Num / secondNumber
    elif math == "mul":
        result = Num * secondNumber
    elif math == "per":
        result = Num * secondNumber
    e.delete(0, END)
    e.insert(0, str(result))

# define buttons
# we have to pass a lambda function to pass a parameter into a function
button_1 = Button(calc, text="1", padx=40, pady=20, command=lambda: button_add(1))
button_2 = Button(calc, text="2", padx=40, pady=20, command=lambda: button_add(2))
button_3 = Button(calc, text="3", padx=40, pady=20, command=lambda: button_add(3))
button_4 = Button(calc, text="4", padx=40, pady=20, command=lambda: button_add(4))
button_5 = Button(calc, text="5", padx=40, pady=20, command=lambda: button_add(5))
button_6 = Button(calc, text="6", padx=40, pady=20, command=lambda: button_add(6))
button_7 = Button(calc, text="7", padx=40, pady=20, command=lambda: button_add(7))
button_8 = Button(calc, text="8", padx=40, pady=20, command=lambda: button_add(8))
button_9 = Button(calc, text="9", padx=40, pady=20, command=lambda: button_add(9))
button_0 = Button(calc, text="0", padx=40, pady=20, command=lambda: button_add(0))
button_dot = Button(calc, text=".", padx=42, pady=20, command=lambda: button_dotted("."))
# functions without parameters we pass without "()"
button_sum = Button(calc, text="+", padx=40, pady=20, command=button_plus)
button_equal = Button(calc, text="=", padx=86, pady=20, command=button_result)
button_delete = Button(calc, text="Clear", padx=78 , pady=20, command=button_clear, foreground="red")
button_minus = Button(calc, text="-", padx=40 , pady=20, command=button_sub)
button_mult = Button(calc, text="*", padx=40 , pady=20, command=button_mul)
button_divd = Button(calc, text="/", padx=42 , pady=20, command=button_div)
button_per = Button(calc, text="%", padx=39, pady=20, command=button_percent)

# put the buttons on the screen:
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)
button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)
button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)
button_0.grid(row=5, column=1)
button_dot.grid(row=5, column=0)
button_equal.grid(row=5, column=2, columnspan=2)
button_delete.grid(row=1, column=0, columnspan=2)
button_minus.grid(row=2, column=3)
button_sum.grid(row=3, column=3)
button_mult.grid(row=1, column=3)
button_divd.grid(row=4, column=3)
button_per.grid(row=1, column=2)

# the loop to run the calculator
calc.mainloop()

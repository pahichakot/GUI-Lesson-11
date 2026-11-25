#Multiplication Table
from tkinter import *
from tkinter.ttk import *

#Set up
root = Tk()
root.title("Multiplication Table")

#Mathematical Table - Label
math_table = Label(root, text = "Mathematical Table", font = ("Times New Roman", 12, "normal"))
math_table.grid(row = 0, column = 0, columnspan = 3, pady = 20)

#Number and Range - Label
num_and_range = Label(root, text = "Number and Range: ", font = ("Times New Roman", 14, "normal"))
num_and_range.grid(row = 1, column = 0, padx = 10)

#Dropdown - Combo box

#All values must be integers
theNum = IntVar()

#Create widget
numbers = Combobox(root, textvariable = theNum, width = 5)

#Articulate possible values
numbers["values"] = tuple(range(101))
numbers.grid(row = 1, column = 1)

#Multiples range - Radio Button
endVal = IntVar()

#10
r10 = Radiobutton(root, text = "10", variable = endVal, value = 10)
r10.grid(row = 1, column = 2, padx = 30)

#20
r20 = Radiobutton(root, text = "20", variable = endVal, value = 20)
r20.grid(row = 2, column = 2, padx = 30)

#30
r30 = Radiobutton(root, text = "30", variable = endVal, value = 30)
r30.grid(row = 3, column = 2, padx = 30)

#Product - Function
def product():
    table = ""

    num = theNum.get()
    value = endVal.get()

    for i in range(value + 1):
        table += str(num) + " X " + str(i) + " = " + str(num*i) + "\n"

    answer.config(text = table)

#Generate - Button
generate = Button(root, text = "Generate", command = product)
generate.grid(row = 4, column = 1)

#Answer - Label
answer = Label(root, anchor = "center")
answer.grid(row = 5, column = 1, pady = 20)

root.mainloop()
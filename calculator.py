                                         
# -*- coding: utf-8 -*-
import math
from tkinter import *

s = Tk()
s.title("calculator.com")
#s.geometry("720x600")


exp = StringVar()
exp.set("")

#text widget
txt = Entry(s, textvariable = exp, font=("Arial",14))
txt.grid(row=0, column=0, columnspan=6)
txt.focus()

#handling button clicks
def press(clicked):
    exp.set(exp.get()+clicked)
    
#clearing text box
def clear():
    exp.set("")
#backspacebutton
def bs():
    exp.set(exp.get()[:-1])
#square root
def sq():
    exp.set(math.sqrt(float(exp.get())))
#evaluating expression
def result():
    try:
        exp.set(str(eval(exp.get())))
    except:
        exp.set("ERROR: Syntax ERROR")
        
# creating number buttons
num_0 = Button(s, text="0",bg="cyan",activebackground="lightyellow",cursor="hand2", command=lambda : press("0"))
num_1 = Button(s, text="1", bg="cyan",activebackground="lightyellow" ,cursor="hand2", command=lambda : press("1"))
num_2 = Button(s, text="2", bg="cyan",activebackground="lightyellow", cursor="hand2", command=lambda : press("2"))
num_3 = Button(s, text="3", bg="cyan",activebackground="lightyellow" ,cursor="hand2", command=lambda : press("3"))
num_4 = Button(s, text="4", bg="cyan",activebackground="lightyellow", cursor="hand2", command=lambda : press("4"))
num_5 = Button(s, text="5", bg="cyan",activebackground="lightyellow" ,cursor="hand2", command=lambda : press("5"))
num_6 = Button(s, text="6", bg="cyan",activebackground="lightyellow", cursor="hand2", command=lambda : press("6"))
num_7 = Button(s, text="7", bg="cyan",activebackground="lightyellow", cursor="hand2", command=lambda : press("7"))
num_8 = Button(s, text="8", bg="cyan",activebackground="lightyellow", cursor="hand2", command=lambda : press("8"))
num_9 = Button(s, text="9", bg="cyan",activebackground="lightyellow", cursor="hand2", command=lambda : press("9"))


num_7.grid(row = 1, column = 0, sticky = N+S+W+E, padx=2, pady=2)
num_8.grid(row = 1, column = 1, sticky = N+S+W+E, padx=2, pady=2)
num_9.grid(row = 1, column = 2, sticky = N+S+W+E, padx=2, pady=2)
num_4.grid(row = 2, column = 0, sticky = N+S+W+E, padx=2, pady=2)
num_5.grid(row = 2, column = 1, sticky = N+S+W+E, padx=2, pady=2)
num_6.grid(row = 2, column = 2, sticky = N+S+W+E, padx=2, pady=2)
num_1.grid(row = 3, column = 0, sticky = N+S+W+E, padx=2, pady=2)
num_2.grid(row = 3, column = 1, sticky = N+S+W+E, padx=2, pady=2)
num_3.grid(row = 3, column = 2, sticky = N+S+W+E, padx=2, pady=2)
num_0.grid(row = 4, column = 0, columnspan=3,rowspan=5,sticky = N+S+W+E, padx=2, pady=2)

#operator  buttons
add_b = Button(s, text="+", bg="skyblue", command=lambda : press("+"))
add_b.grid(row = 4, column = 3,rowspan=5, sticky = N+S+W+E, padx=2, pady=2)
sub_b = Button(s, text="-", bg="skyblue", command=lambda : press("-"))
sub_b.grid(row = 3, column = 3, sticky = N+S+W+E, padx=2, pady=2)
mul_b = Button(s, text="x", bg="skyblue", command=lambda : press("*"))
mul_b.grid(row = 2, column = 3, sticky = N+S+W+E, padx=2, pady=2)
div_b = Button(s, text="/", bg="skyblue",command=lambda : press("/"))
div_b.grid(row = 1, column = 3, sticky = N+S+W+E, padx=2, pady=2)
mod_b = Button(s, text="mod", bg="skyblue",command=lambda : press("%"))
mod_b.grid(row = 4, column = 4,rowspan=5, sticky = N+S+W+E, padx=2, pady=2)
dot_b = Button(s, text=".", bg="skyblue",command=lambda : press("."))
dot_b.grid(row = 1, column = 4, sticky = N+S+W+E, padx=2, pady=2)
sq_b = Button(s, text="√", bg="skyblue",command=sq)
sq_b.grid(row = 2, column = 4, sticky = N+S+W+E, padx=2, pady=2)
par_b = Button(s, text=")", bg="skyblue", command=lambda : press(")"))
par_b.grid(row = 2, column = 5, sticky = N+S+W+E, padx=2, pady=2)
par_b = Button(s, text="(", bg="skyblue", command=lambda : press("("))
par_b.grid(row = 3, column = 5, sticky = N+S+W+E, padx=2, pady=2)

# Clear button
clr = Button(s, text="C", bg="red", fg="white", command = clear)
clr.grid(row = 1, column = 5, sticky = N+S+W+E, padx=2, pady=2)

#backspace button
bs_b = Button(s, text="<--", bg="skyblue", cursor="mouse",command=bs)
bs_b.grid(row = 3, column = 4, sticky = N+S+W+E, padx=2, pady=2)



# Result button
eq_b = Button(s, text="=", bg="lightgreen", fg="white", font=("Arial",12), command = result)
eq_b.grid(row = 4, column = 5,rowspan=5,sticky = N+S+W+E, padx=2, pady=2)

s.mainloop()



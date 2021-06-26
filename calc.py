###** calculator **###



from tkinter import *


root = Tk()
root.geometry("600x400")
root.title("Calculator")
#root.config(bg = "white")
root.iconbitmap('calculator.ico')
value=""

def click_button(number):
    global value
    value = value + str(number)
    var.set(value)

def equal():
    global value
    ans=str(eval(value))
    var.set(ans)
    value = ""



#Background

L01 = PhotoImage(file = "back.png")
l1 = Label(root,image = L01)
l1.pack()

#Entrybar
var= StringVar()
e1=Entry(root,font =("arial 20"),textvariable = var)
e1.place(x=120 , y=70)

#Button

##line 1
one = PhotoImage(file = "1.png")
b1 = Button(root,image = one, font = ("arial 10"),command = lambda : click_button(1))
b1.place(x=100 , y=120)

two = PhotoImage(file = "2.png" )
b2 = Button(root,image = two,font = ("arial 10"),command = lambda : click_button(2))
b2.place(x=150 , y=120)

three = PhotoImage(file = "3.png")
b3 = Button(root,image = three, font = ("arial 10"),command = lambda : click_button(3))
b3.place(x=200 , y=120)

plus = PhotoImage(file = "+.png")
bp = Button(root,image = plus,font = ("arial 10"),command = lambda : click_button("+"))
bp.place(x=250 , y=120) 

mul = PhotoImage(file = "mul.png")
bm = Button(root,image = mul,font = ("arial 10"),command = lambda : click_button("*"))
bm.place(x=300 , y=120) 

## line 2
four = PhotoImage(file = "4.png" )
b4 = Button(root,image = four,font = ("arial 10"),command = lambda : click_button(4))
b4.place(x=100 , y=170)

five = PhotoImage(file = "5.png" )
b5 = Button(root,image = five,font = ("arial 10"),command = lambda : click_button(5))
b5.place(x=150 , y=170)

six = PhotoImage(file = "6.png" )
b6 = Button(root,image = six,font = ("arial 10"),command = lambda : click_button(6))
b6.place(x=200 , y=170)

minus = PhotoImage(file = "-.png")
bm = Button(root,image = minus,font = ("arial 10"),command = lambda : click_button("-"))
bm.place(x=250 , y=170) 

div = PhotoImage(file = "div.png")
bd = Button(root,image = div,font = ("arial 10"),command = lambda : click_button("/"))
bd.place(x=300 , y=170) 

## line 3

seven = PhotoImage(file = "7.png")
b7 = Button(root,image = seven,font = ("arial 10"),command = lambda : click_button(7))
b7.place(x=100 , y=220)

eight = PhotoImage(file = "8.png")
b8 = Button(root,image = eight,font = ("arial 10"),command = lambda : click_button(8))
b8.place(x=150 , y=220)

nine = PhotoImage(file = "9.png")
b9 = Button(root,image = nine,font = ("arial 10"),command = lambda : click_button(9))
b9.place(x=200 , y=220)

equal_1 = PhotoImage(file = "equal.png")
be = Button(root,image = equal_1, command = equal)
be.place(x=250 , y=220) 

##line 4

zero = PhotoImage(file = "0.png")
b0 = Button(root,image = zero,font = ("arial 10"),command = lambda : click_button(0))
b0.place(x=150 , y=270)








root.mainloop()

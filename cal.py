from tkinter import *
import tkinter as tk
from tkinter import messagebox

frm=Tk()
frm.geometry('600x600')
frm.title("Calculator")

def add():
    try:
        a=int(txt1.get())
        b=int(txt2.get())
        c=a+b
        print("The Add values is = " , c)
        messagebox.showinfo("Add Answer is",c)
    except:
        messagebox.showinfo("Error" , "Enter The Values" )

def sub():
    try:
        a=int(txt1.get())
        b=int(txt2.get())
        c=a-b
        print("The Sub values is = " , c)
        messagebox.showinfo("Sub Answer is",c)
    except:
        messagebox.showinfo("Error" , "Enter The Values" )

def mul():
    try:
        a=int(txt1.get())
        b=int(txt2.get())
        c=a*b
        print("The Mul values is = " , c)
        messagebox.showinfo("Mul Answer is",c)
    except:
        messagebox.showinfo("Error" , "Enter The Values" )

def div():
    try:
        a=int(txt1.get())
        b=int(txt2.get())
        c=a/b
        print("The Div values is = " , c)
        messagebox.showinfo("Div Answer is",c)
    except:
        messagebox.showinfo("Error" , "Enter The Values" )

def addnew():
    a=int(txt1.get())
    b=int(txt2.get())
    txt1.delete(0,"end")
    txt2.delete(0,"end")

        

lb=Label(frm , text="Calculator" , fg='blue' , font=("Tahome",10))
lb.place(x=100 , y=10)
 
lb1= Label(frm, text="Enter A : ", fg="blue", font=("tahoma" , 10))
lb1.place(x=20 , y=50)

txt1=Entry(frm , text="" , bd=1 , fg="green")
txt1.place(x=140 , y=50)

lb2=Label(frm, text="Enter B : ", fg="blue", font=("tahoma" , 10))
lb2.place(x=20 , y=80 )

txt2=Entry(frm , text="" , bd=1 , fg="green")
txt2.place(x=140 , y=80)

btn=Button(frm, text="Add", fg="black", font=("Tahome", ),command= add)
btn.place(x=140 , y=120)

btn1=Button(frm, text="Sub", fg="black", font=("Tahome", ),command= sub)
btn1.place(x=200 , y=120)

btn2=Button(frm, text="Mul", fg="black", font=("Tahome", ),command=mul )
btn2.place(x=260 , y=120)

btn3=Button(frm, text="Div", fg="black", font=("Tahome", ),command=div )
btn3.place(x=320 , y=120)

btn4=Button(frm, text="Cler", fg="black", font=("Tahome", ),command=addnew )
btn4.place(x=380 , y=120)

frm.mainloop()

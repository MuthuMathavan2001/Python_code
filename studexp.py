
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql as con

frm=Tk()
frm.geometry("800x800")
frm.title("Student detail")

def stud():
    regno=txt.get()
    name=txt1.get()
    qualification=txt2.get()
    phoneno=txt3.get()
    address=txt4.get()
    nationality=menu.get()   
    sex = str(var.get())
    if sex=='1':
        gender="Male"
    elif sex=='2':
        gender="Female"
    else:
        gender="Other"
    #label.config(text = sex)
    '''
    values = {"Male" : "Male",
          "Female" : "Female",
          "Other" : "Other",
          }
    '''
    h1=CheckVar1.get()
    
    if h1==1:
        db=con.connect(host="localhost",user="root",password="",db="studexpdb")
        cursor=db.cursor()

        db.query("Insert into stud values('"+ regno +"','"+ name +"','"+ qualification +"','"+ nationality +"','"+ gender +"','"+ phoneno +"','"+ address +"')")
        db.commit()
        messagebox.showinfo("Saved","Successsful")
        db.close()
    else:
        messagebox.showinfo("Error","Click the box")
def find():
    regno=txt.get()

    db=con.connect(host="localhost",user="root",password="",db="studexpdb")
    cursor=db.cursor()

    db.query("SELECT * FROM emp WHERE reg_no =" +regno)
 


lb=Label(frm,text="Student Details ",fg='HotPink',font=("tahoma",15))
lb.place(x=200,y=10)

lb1=Label(frm,text="Reg No :",fg="blue",font=("tahoma",10))
lb1.place(x=20,y=70)

txt=Entry(frm,text="",bd=5,fg="green")
txt.place(x=100,y=70)

lb2=Label(frm,text="Name :",fg="blue",font=("tahoma",10))
lb2.place(x=20,y=120)

txt1=Entry(frm,text="",bd=5,fg="green")
txt1.place(x=100,y=120)

lb3=Label(frm,text="Qualification :",fg="blue",font=("tahoma",10))
lb3.place(x=20,y=170)

txt2=Entry(frm,text="",bd=5,fg="green")
txt2.place(x=100,y=170)

lb7=Label(frm,text="phone No :",fg="blue",font=("tahoma",10))
lb7.place(x=20,y=320)

txt3=Entry(frm,text="",bd=5,fg="green")
txt3.place(x=100,y=320)

lb8=Label(frm,text="Adderss :",fg="blue",font=("tahoma",10))
lb8.place(x=20,y=370)

txt4=Entry(frm,text="",bd=5,fg="green")
txt4.place(x=100,y=370)


lb5=Label(frm,text="Nationality :",fg="blue",font=("tahoma",10))
lb5.place(x=20,y=220)
menu= StringVar()
menu.set("Select the Nationality")
drop= OptionMenu(frm,menu ,"indian", "non-indian")
drop.pack()
drop.place(x=100,y=220)


var = IntVar()
lb6=Label(frm,text="Sex:",fg="blue",font=("tahoma",10))
lb6.place(x=20,y=270)

R1 = Radiobutton(frm, text="Male", variable=var, value=1)
                  #command=stud)
R1.pack()
R1.place(x=100,y=270)

R2 = Radiobutton(frm, text="Female", variable=var, value=2)
                  #command=stud)
R2.pack()
R2.place(x=150,y=270)


R3 = Radiobutton(frm, text="Other", variable=var, value=3)
                  #command=stud)
R3.pack()
R3.place(x=200,y=270)

#label = label(frm)
#label.pack()

btn=Button(frm,text="Save",fg='blue',font=("tahoma",10),command=stud)
btn.place(x=100,y=420)


CheckVar1 = IntVar()
h1 = Checkbutton(frm, text = " I Accept ", variable =CheckVar1, \
                 onvalue = 1, offvalue = 0)
h1.pack()
h1.place(x=20,y=396)



frm.mainloop()

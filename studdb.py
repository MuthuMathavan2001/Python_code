from tkinter import *
import tkinter as tk
from tkinter import messagebox
import pymysql as con
frm=Tk()
frm.geometry("800x800")
frm.title("Student details")

def stud():
    try:
        regno=int(reg.get())
        a=int(txt.get())
        b=int(txt1.get())
        c=int(txt2.get())
        d=int(txt3.get())
        e=int(txt4.get())
        r=str(regno)
        f=str(a)
        g=str(b)
        h=str(c)
        i=str(d)
        j=str(e)
        
        if(a<=100)&(b<=100)&(c<=100)&(d<=100)&(e<=100):
            total=a+b+c+d+e
            res1.config(text="Total : " + str(total))
        k=str(total)
        percentage=total/5
        res2.config(text=" percentage : "+ str(percentage))
        l=str(percentage)
            
        result="pass"
        res3.config(text="Result :" + str(result), fg="green")
        
        if(a<=35)or(b<=35)or(c<=35)or(d<=35)or(e<=35):
            result="fail"
            res3.config(text="Result : " + str(result),fg="red")
            Grade="Nill"
        
        elif(percentage>=90):
             Grade="O"
        elif(percentage>=80):
             Grade= "A+"
        elif(percentage>=70):
            Grade="A"
        elif(percentage>=60):
            Grade="B+"
        elif(percentage>=50):
            Grade= "B"
        elif(percentage>=40):
            Grade="C+"
        elif(percentage>=35):
            Grade="C"
        res4.config(text="Grade : " + str(Grade))    
    except:
        messagebox.showinfo("Error","Enter The Valid Number")

    db=con.connect(host ="localhost",user ="root",password="",db="studdb")
    cursor=db.cursor()

    db.query("Insert into stud values("+ r +",'"+ f + "','"+ g +"','"+ h +"','"+ i +"','"+ j +"','"+ k +"','"+ l +"','"+ result +"','"+ Grade +"' )")
    db.commit()
    messagebox.showinfo("Student","Successful")
    db.close()
    
lb=Label(frm, text=("Enter The Student Mark Details "),fg="blue",font=("Tahoma",14))
lb.place(x=100,y=10)

reg=Label(frm, text=("Roll No = "),fg="blue",font=("Tahoma",10))
reg.place(x=20,y=50)

reg=Entry(frm,text="" ,bd=1,fg="green" )
reg.place(x=200,y=50)


lb1=Label(frm,text=("Tamil Mark ="), fg="blue",font=("Tahoma",10))
lb1.place(x=20, y=100)


txt=Entry(frm,text="" ,bd=1,fg="green" )
txt.place(x=200,y=100)

lb2=Label(frm,text=("English Mark ="), fg="blue",font=("Tahoma",10))
lb2.place(x=20, y=150)

txt1=Entry(frm,text="" ,bd=1,fg="green" )
txt1.place(x=200,y=150)

lb3=Label(frm,text=("Maths Mark ="), fg="blue",font=("Tahoma",10))
lb3.place(x=20, y=200)

txt2=Entry(frm,text="" ,bd=1,fg="green" )
txt2.place(x=200,y=200)

lb4=Label(frm,text=("Science Mark ="), fg="blue",font=("Tahoma",10))
lb4.place(x=20, y=250)

txt3=Entry(frm,text="" ,bd=1,fg="green" )
txt3.place(x=200,y=250)

lb5=Label(frm,text=(" Social Science Mark ="), fg="blue",font=("Tahoma",10))
lb5.place(x=20, y=300)

txt4=Entry(frm,text="" ,bd=1,fg="green" )
txt4.place(x=200,y=300)

btn=Button(frm, text="Total", fg="red", font=("Tahoma",10),command=stud)
btn.place(x=50,y=350)

res1=Label(frm, text="Total:", fg='blue', font=("Tahoma", 14))
res1.place(x=20, y=400)

res2=Label(frm, text=" percentage :", fg='blue', font=("Tahoma", 14))
res2.place(x=20, y=450)

res3=Label(frm, text="Result:", fg='blue', font=("Tahoma", 14))
res3.place(x=20, y=500)

res4=Label(frm, text="Grade:", fg='blue', font=("Tahoma", 14))
res4.place(x=20, y=550)

frm.mainloop()

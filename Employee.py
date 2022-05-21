import mysql.connector
import pymysql as con
from tkinter import *
import tkinter as tk
from tkinter import messagebox

frm=Tk()
frm.geometry("800x800")
frm.title("Employee Details ")

def save():
    empid=txt.get()
    empname=txt1.get()
    degree=txt2.get()
    try:
        if len(empid)==0:
            print(empid)

    except:
        messagebox.showinfo("Erro","Enter The Number Values")

    db=con.connect(host="localhost",user="root",password="",db="empdb")
    cursor=db.cursor()
    db.query("Insert into emp values('"+ empid +"','"+ empname +"','"+ degree +"')")
    db.commit()
    messagebox.showinfo("saved","Successful")
    db.close()

def find():
    empid=txt.get()
    
    print(empid)

    #db=con.connect(host="localhost",user="root",password="",db="empdb")
    #cursor=db.cursor()
    my_connect = mysql.connector.connect(host="localhost",user="root",password="",db="empdb")
    my_cursor=my_connect.cursor()
    my_cursor.execute("SELECT * FROM emp WHERE emp_id ="+empid)
    r=my_cursor.fetchone()
    emp_id=r[0]
    emp_name=r[1]
    emp_degree=r[2]
    txt1.insert(INSERT,str(emp_name))
    txt2.insert(INSERT,str(emp_degree))
    #db.commit()
    messagebox.showinfo("Find","Successful")
    #db.close()

def delete():
    empid=txt.get()

    db=con.connect(host="localhost",user="root",password="",db="empdb")
    cursor=db.cursor()
    db.query("DELETE FROM emp WHERE emp_id="+empid)
    db.commit()
    messagebox.showinfo("Delete","Successful")
    db.close()

def addnew():
    empid=txt.get()
    empname=txt1.get()
    degree=txt2.get()
    txt.delete(0,"end")
    txt1.delete(0,"end")
    txt2.delete(0,"end")

def modify():
    empid=txt.get()
    empname=txt1.get()
    degree=txt2.get()
    db=con.connect(host="localhost",user="root",password="",db="empdb")
    cursor=db.cursor()
    db.query("update emp set emp_id='"+ empid +"',emp_name='"+ empname +"',emp_degree='"+ degree +"' where emp_id="+empid)
    db.commit()
    messagebox.showinfo("Modify","Successful")
    db.close()


lb=Label(frm,text="Employee",fg='blue',font=("tahoma",15))
lb.place(x=150,y=10)

lb1=Label(frm,text="Employee Id : ", fg='green',font=("tahoma",10))
lb1.place(x=10,y=50)

txt=Entry(frm,text="",bd=5,fg='black')
txt.place(x=150,y=50)

lb2=Label(frm,text="Employee Name : ", fg='green',font=("tahoma",10))
lb2.place(x=10,y=100)

txt1=Entry(frm,text="",bd=5,fg='black')
txt1.place(x=150,y=100)

lb1=Label(frm,text="Employee Degree : ", fg='green',font=("tahoma",10))
lb1.place(x=10,y=150)

txt2=Entry(frm,text="",bd=5,fg='black')
txt2.place(x=150,y=150)

btn=Button(frm,text="Save",fg='blue',font=("tahoma",10),command=save)
btn.place(x=50,y=200)

btn1=Button(frm,text="Find",fg='blue',font=("tahoma",10),command=find)
btn1.place(x=100,y=200)

btn2=Button(frm,text="Delete",fg='blue',font=("tahoma",10),command=delete)
btn2.place(x=150,y=200)

btn3=Button(frm,text="Cler",fg='blue',font=("tahoma",10),command=addnew)
btn3.place(x=220,y=200)

btn4=Button(frm,text="Modify",fg='blue',font=("tahoma",10),command=modify)
btn4.place(x=270,y=200)

frm.mainloop()










    

    

    

    

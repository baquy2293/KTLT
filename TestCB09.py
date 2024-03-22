from tkinter import *

import tkinter.messagebox as m

loginWindow = Tk()
loginWindow.title("tkinter")
loginWindow.geometry("400x400")
def Register():
    registerWindow = Tk()
    registerWindow.title("Register")
    registerWindow.geometry("400x400")
    bigText = Label(text="Registration",font="verdana 20 bold")
    bigText.pack()

    name = Label(registerWindow,text="Name")
    name.place(x=90,y=100)
    age = Label(registerWindow, text="Age")
    age.place(x=90,y=140)
    email = Label(registerWindow, text="Email")
    email.place(x=90,y=180)
    password = Label(registerWindow, text="Password")
    password.place(x=90,y=220)

    e1 = Entry(registerWindow)
    e1.place(x=180,y=100)
    e2 = Entry(registerWindow)
    e2.place(x=180, y=140)
    e3 = Entry(registerWindow)
    e3.place(x=180, y=180)
    e4 = Entry(registerWindow)
    e4.place(x=180, y=220)


    def insert():
        values = [e1.get(),e2.get(),e3.get(),e4.get()]
        print(values)
        registerWindow.destroy()
        m.showinfo("","dang ki thanh cong")
    register = Button(registerWindow,text="Register",fg="green",command=insert)
    register.place(x=175,y=260)
    btnExit = Button(registerWindow, text="Exit", bg="red", command=registerWindow.destroy)
    btnExit.place(x=350, y=350)



emai = Label(loginWindow, text="Email")
emai.place(x=100, y=150)
password = Label(loginWindow, text="Password")
password.place(x=100,y=180)

e1 = Entry(loginWindow)
e1.place(x=160,y=150)
e2 = Entry(loginWindow)
e2.place(x=160,y=180)

goToRegister = Button(loginWindow,text="Register",fg="green",font="verdana 10 bold",command=Register)
goToRegister.place(x=180,y=200)


loginWindow.mainloop()


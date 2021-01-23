from tkinter import *
def login():
    print("Login Successful")
    print(f"{EmailEnt.get(),PassEnt.get(),rem.get()}")
root = Tk()
root.geometry("550x800")
root.title("Login Form")
root.configure(background="SlateGray1")


Logo =Label(text="LOGIN",font="comicsanms 50 bold",fg="red",bg="SlateGray1")
Logo.grid(padx=55,pady= 40,row=0,column=5)



Email = Label(text="Email",font="comicsanms 20 ",fg="red",bg="SlateGray1")
Email.grid(row=1,column=4,padx=2,pady=40)

Pass = Label(text="Password",font="comicsanms 20 ",fg="red",bg="SlateGray1")
Pass.grid(row=2,column=4,padx=2,pady=10)


EmailEnt = StringVar()
PassEnt = StringVar()
rem = IntVar()


EmailEntry = Entry(root,textvariable=EmailEnt,font=90)
EmailEntry.grid(row=1,column=5)

PasswordEntry = Entry(root,textvariable=PassEnt,font=90)
PasswordEntry.grid(row=2,column=5)

b1 = Checkbutton(text="Remember me",font=10,fg="firebrick1",variable=rem)
b1.grid(row=3,column=5)



b2 = Button(text="LOGIN",font="lucida 15",fg="white",bg="SlateGray4",command=login,padx=160,pady=30)
b2.grid(row=6,column=5,pady=20)




root.mainloop()
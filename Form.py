from tkinter import *
root = Tk()
root.geometry("1250x850")
name = Label(root, text="Name", bg="red",font=200)
city = Label(root,text="City",bg="green",font=200)
state = Label(root, text="State" , bg="blue",font=200)
name.grid(padx=10)
city.grid(row=1)
state.grid(row=2)


username = StringVar()
usercity = StringVar()
userstate = StringVar()

name1 = Entry(root,textvariable=username,font=200)
city1 = Entry(root,textvariable=usercity,font=200)
state1 = Entry(root,textvariable=userstate,font=200)

name1.grid(row=0,column=1,padx=40,)
city1.grid(row=1,column=1,padx=40)
state1.grid(row=2,column=1,padx=40)

b1= Button(text="submit",bg="pink")
b1.grid()












root.mainloop()
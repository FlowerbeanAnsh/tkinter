from tkinter import *
root = Tk()
root.geometry("1250x850")
def getvals():
    print("sumbitting form")
    print(f"{name1.get(),rollno1.get(),section1.get(),course1.get(),branch1.get(),check.get()}")


    with open("informations.txt", "a") as f:
        f.write(f"{name1.get(),rollno1.get(),section1.get(),course1.get(),branch1.get(),check.get()}")
        pass
#main heading
Label(text="Welcome to GLA University Mathura",bg="cyan",fg="white",font="comicsanms 30 bold").grid(row=0,column=10,pady="50",padx=20)

#infos
name = Label(text="Student Name",font="comicsanms 20 bold",fg="green2")
rollno = Label(text="Univ. Roll no",font="comicsanms 20 bold",fg="green2")
section =  Label(text="Section",font="comicsanms 20 bold",fg="green2")
course = Label(text="Course",font="comicsanms 20 bold",fg="green2")
branch = Label(text="Branch",font="comicsanms 20 bold",fg="green2")

#packing of infos
name.grid(row=1,column=5)
rollno.grid(row=2,column=5)
section.grid(row=3,column=5)
course.grid(row=4,column=5)
branch.grid(row=5,column=5)

#declaration of var

name1= StringVar()
rollno1= StringVar()
section1 = StringVar()
course1 = StringVar()
branch1 = StringVar()
check = IntVar()

#entries
nameentry = Entry(root,textvariable=name1,font=20)
rollnoentry =  Entry(root,textvariable=rollno1,font=20)
sectionentry =  Entry(root,textvariable=section1,font=20)
couseentry =  Entry(root,textvariable=course,font=20)
branchentry =  Entry(root,textvariable=branch,font=20)

# packing of entries

nameentry.grid(row=1,column=10)
rollnoentry.grid(row=2,column=10)
sectionentry.grid(row=3,column=10)
couseentry.grid(row=4,column=10)
branchentry.grid(row=5,column=10)

#checkbutton

b1 = Checkbutton(text="i agree with all terms and conditions",variable=check,font="comicsanms 20 bold")
b1.grid(row=6,column=10)

b2 = Button(text="Submit",font="comicsanms 20 bold",bg="red2",command=getvals)
b2.grid(row=8,column=10)



root.mainloop()
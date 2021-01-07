from tkinter import *
root = Tk()
root.geometry("1250x850")
root.title("MY GUI")
def sum():
    print("sum of 2 +2 is = 4")

f1 = Frame(root,borderwidth=7,bg="grey",relief=SUNKEN)
f1.pack(anchor="nw",side="left")
b1 = Button(f1,fg="red",text="SUM",font="bold",command=sum)
b1.pack(side="left",padx=10)

b2 = Button(f1,fg="red",text="Minus",font="bold")
b2.pack(side="left",padx=10)

b3 = Button(f1,fg="red",text="Multiply",font="bold")
b3.pack(side="left",padx=10)

b4 = Button(f1,fg="red",text="Division",font="bold")
b4.pack(side="left",padx=10)







root.mainloop()
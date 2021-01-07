from tkinter import *
root = Tk()
root.geometry("1250x850")
root.title("MY GUI")
f1 = Frame(root, padx=10,borderwidth=9,bg="red",relief=SUNKEN)
f1.pack(side="top",fill="x")

label = Label(f1,text="Editor")
label.pack(padx=20,fill="y")







root.mainloop()
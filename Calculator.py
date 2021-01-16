from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")

    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                 value = eval(scvalue.get())
            except Exception as e:
                scvalue.set("Error")
                screen.update()


        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("444x950")
root.title("Calculator")
root.configure(background="cyan")



scvalue = StringVar()
scvalue.set("")
screen = Entry(root,text=scvalue,font ="lucida 50 bold",background="ghost white")
screen.pack(fill=Y,ipadx=8,padx=10,pady=10)

f = Frame(root,bg = "cyan")


b = Button(f,text="9",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="8",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="7",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,bg = "cyan")
b = Button(f,text="6",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="5",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="4",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "cyan")
b = Button(f,text="3",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="2",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f, text="1", font="lucida 30 bold", padx=21, pady=15,background="peach puff")
b.pack(side=LEFT, padx=10, pady=6)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "cyan")
b = Button(f,text="0",font="lucida 30 bold",padx=21,pady=15,background="peach puff")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)




b = Button(f,text="=",font="lucida 30 bold",padx=21,pady=15,background="deep pink")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)


b = Button(f,text="+",font="lucida 30 bold",padx=21,pady=15,background="deep pink")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg = "cyan")
b = Button(f,text="-",font="lucida 30 bold",padx=21,pady=15,background="deep pink")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)


b = Button(f,text="/",font="lucida 30 bold",padx=21,pady=15,background="deep pink")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="*",font="lucida 30 bold",padx=21,pady=15,background="deep pink")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root,bg = "cyan")

b = Button(f,text="%",font="lucida 30 bold",padx=21,pady=15)
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)


f = Frame(root,bg = "cyan")

b = Button(f,text="%",font="lucida 30 bold",padx=21,pady=15,background="deep pink")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)

b = Button(f,text="C",font="lucida 30 bold",padx=21,pady=15,background="red2")
b.pack(side=LEFT,padx=10,pady=6)
b.bind("<Button-1>",click)



f.pack()










root.mainloop()
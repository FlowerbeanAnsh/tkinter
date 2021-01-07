from tkinter import *

root = Tk()
root.geometry("1200x850")
root.title("My First GUI")
label = Label(text='''Although many of Aristophanes’ criticisms seem unfair,
                   \nSocrates cut a strange figure in Athens, going about barefoot, 
                   \nlong-haired and unwashed in a society with incredibly refined standards
                   \n of beauty. It didn’t help that he was by all accounts physically ugly, 
                   \nwith an upturned nose and bulging eyes. Despite his intellect and connections,
                   \n he rejected the sort of fame and power that Athenians were expected to strive for.
                   \n His lifestyle—and eventually his death—embodied his spirit of questioning every assumption
                   \n about virtue, wisdom and the good life.''',bg="blue",fg="white",font="comicsansms 20 bold",
              padx=60,pady=60,relief=SUNKEN)

#imortant pack options
# 1 anchor -- to move nw sw all areas
# 2 side -- left , bottom, right, top
# 3 fill -- kheechne k liye , fill =x fill=y

label.pack(anchor="nw",fill="x",side="top")




root.mainloop()